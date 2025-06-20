"""
Named Entity Recognition (NER) processor for technical documents.
This module provides functionality to extract entities, annotate text, and map concepts.
"""

import logging
import spacy
from typing import List, Dict, Any, Optional, Tuple, Set
from pathlib import Path
import json
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NERProcessor:
    """
    A processor for named entity recognition, annotation, and concept mapping.
    Uses spaCy for NER and supports custom entity types for technical documentation.
    """

    def __init__(self, model_name: str = "en_core_web_lg", custom_entities_file: Optional[str] = None):
        """
        Initialize the NER processor with a spaCy model.

        Args:
            model_name (str): Name of the spaCy model to use (default: en_core_web_lg)
            custom_entities_file (str, optional): Path to a JSON file with custom entities
        """
        logger.info(f"Loading spaCy model: {model_name}")
        try:
            self.nlp = spacy.load(model_name)
            logger.info(f"Loaded spaCy model: {model_name}")
        except OSError:
            logger.warning(f"Model {model_name} not found. Downloading...")
            spacy.cli.download(model_name)
            self.nlp = spacy.load(model_name)
            logger.info(f"Downloaded and loaded spaCy model: {model_name}")

        # Load custom entities if provided
        self.custom_entities = {}
        if custom_entities_file:
            self._load_custom_entities(custom_entities_file)

    def _load_custom_entities(self, file_path: str):
        """
        Load custom entities from a JSON file.

        Args:
            file_path (str): Path to the JSON file with custom entities
        """
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                logger.warning(f"Custom entities file not found: {file_path}")
                return

            with open(file_path, 'r', encoding='utf-8') as f:
                self.custom_entities = json.load(f)

            logger.info(f"Loaded {len(self.custom_entities)} custom entities")
        except Exception as e:
            logger.error(f"Error loading custom entities: {str(e)}")

    def add_custom_entity(self, entity_text: str, entity_type: str):
        """
        Add a custom entity to the processor.

        Args:
            entity_text (str): The text of the entity
            entity_type (str): The type of the entity
        """
        if entity_type not in self.custom_entities:
            self.custom_entities[entity_type] = []

        if entity_text not in self.custom_entities[entity_type]:
            self.custom_entities[entity_type].append(entity_text)
            logger.info(
                f"Added custom entity '{entity_text}' of type '{entity_type}'")

    def save_custom_entities(self, file_path: str):
        """
        Save custom entities to a JSON file.

        Args:
            file_path (str): Path to save the JSON file
        """
        try:
            file_path = Path(file_path)
            # Create directory if it doesn't exist
            os.makedirs(file_path.parent, exist_ok=True)

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.custom_entities, f, indent=2)

            logger.info(
                f"Saved {len(self.custom_entities)} custom entities to {file_path}")
        except Exception as e:
            logger.error(f"Error saving custom entities: {str(e)}")

    def extract_entities(self, text: str) -> List[Dict[str, Any]]:
        """
        Extract named entities from text using spaCy.

        Args:
            text (str): The text to process

        Returns:
            List[Dict[str, Any]]: List of extracted entities with their types and positions
        """
        doc = self.nlp(text)
        entities = []

        # Extract entities from spaCy
        for ent in doc.ents:
            entities.append({
                "text": ent.text,
                "start": ent.start_char,
                "end": ent.end_char,
                "type": ent.label_,
                "source": "spacy"
            })

        # Extract custom entities
        for entity_type, entity_list in self.custom_entities.items():
            for entity_text in entity_list:
                # Simple string matching - could be improved with regex or more complex matching
                for match in self._find_all_occurrences(text, entity_text):
                    entities.append({
                        "text": entity_text,
                        "start": match,
                        "end": match + len(entity_text),
                        "type": entity_type,
                        "source": "custom"
                    })

        # Sort entities by position
        entities.sort(key=lambda x: x["start"])

        return entities

    def _find_all_occurrences(self, text: str, substring: str) -> List[int]:
        """
        Find all occurrences of a substring in text.

        Args:
            text (str): The text to search in
            substring (str): The substring to search for

        Returns:
            List[int]: List of starting positions
        """
        start = 0
        positions = []

        while True:
            start = text.find(substring, start)
            if start == -1:
                break
            positions.append(start)
            start += 1

        return positions

    def annotate_text(self, text: str) -> Tuple[str, List[Dict[str, Any]]]:
        """
        Annotate text with entity information.

        Args:
            text (str): The text to annotate

        Returns:
            Tuple[str, List[Dict[str, Any]]]: Annotated text and entity information
        """
        entities = self.extract_entities(text)

        # Create annotated text with HTML-style markup
        annotated_text = text
        offset = 0

        for entity in sorted(entities, key=lambda x: x["start"], reverse=True):
            start = entity["start"] + offset
            end = entity["end"] + offset

            # Insert end tag
            annotated_text = annotated_text[:end] + \
                f"</entity:{entity['type']}>" + annotated_text[end:]

            # Insert start tag
            annotated_text = annotated_text[:start] + \
                f"<entity:{entity['type']}>" + annotated_text[start:]

            # Update offset for next iteration
            offset += len(f"<entity:{entity['type']}>") + \
                len(f"</entity:{entity['type']}>")

        return annotated_text, entities

    def extract_concepts(self, text: str) -> Dict[str, Set[str]]:
        """
        Extract concepts and group them by type.

        Args:
            text (str): The text to process

        Returns:
            Dict[str, Set[str]]: Dictionary of concept types and their instances
        """
        entities = self.extract_entities(text)

        # Group entities by type
        concepts = {}
        for entity in entities:
            entity_type = entity["type"]
            entity_text = entity["text"]

            if entity_type not in concepts:
                concepts[entity_type] = set()

            concepts[entity_type].add(entity_text)

        return concepts

    def extract_technical_terms(self, text: str) -> List[str]:
        """
        Extract technical terms from text.
        This combines NER with custom rules for identifying technical terms.

        Args:
            text (str): The text to process

        Returns:
            List[str]: List of extracted technical terms
        """
        doc = self.nlp(text)
        terms = set()

        # Extract noun phrases that might be technical terms
        for chunk in doc.noun_chunks:
            # Check if the chunk contains any technical indicators
            if any(token.pos_ in ["NOUN", "PROPN"] for token in chunk):
                terms.add(chunk.text)

        # Add custom technical entities
        if "TECH" in self.custom_entities:
            for term in self.custom_entities["TECH"]:
                if term.lower() in text.lower():
                    terms.add(term)

        # Extract acronyms and abbreviations using pattern matching
        acronyms = self._extract_acronyms(text)
        terms.update(acronyms)

        return list(terms)

    def _extract_acronyms(self, text: str) -> Set[str]:
        """
        Extract acronyms and abbreviations from text.

        Args:
            text (str): The text to process

        Returns:
            Set[str]: Set of extracted acronyms
        """
        doc = self.nlp(text)
        acronyms = set()

        # Simple rule-based extraction for uppercase acronyms
        for token in doc:
            if token.text.isupper() and len(token.text) >= 2 and token.text.isalpha():
                acronyms.add(token.text)

        return acronyms

    def create_concept_map(self, text: str) -> Dict[str, Dict[str, List[str]]]:
        """
        Create a concept map from text, showing relationships between entities.

        Args:
            text (str): The text to process

        Returns:
            Dict[str, Dict[str, List[str]]]: Concept map with entity relationships
        """
        doc = self.nlp(text)
        concept_map = {}

        # Extract entities
        entities = self.extract_entities(text)
        entity_texts = [e["text"] for e in entities]

        # Create concept map structure
        for entity in entities:
            entity_text = entity["text"]
            if entity_text not in concept_map:
                concept_map[entity_text] = {
                    "type": entity["type"],
                    "related_to": []
                }

        # Analyze entity relationships using spaCy's dependency parsing
        for sent in doc.sents:
            for token in sent:
                # Check if token is part of an entity
                token_text = token.text

                if token_text in entity_texts or token.head.text in entity_texts:
                    # If the token and its head are both entities, create a relationship
                    if token_text in entity_texts and token.head.text in entity_texts:
                        source = token.head.text
                        target = token_text

                        if target not in concept_map[source]["related_to"]:
                            concept_map[source]["related_to"].append(target)

        return concept_map
