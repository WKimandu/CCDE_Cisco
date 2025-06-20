#!/usr/bin/env python3
# Muranga County GIS Data Repository
# This script sets up a structured repository for GIS data for Muranga County
# and provides utilities to fetch, process, and visualize geospatial data.

import os
import json
import requests
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import folium
from shapely.geometry import Point, Polygon, shape
import osmnx as ox
import rasterio
from rasterio.plot import show
import contextily as ctx
from tqdm import tqdm
import configparser
import logging
import zipfile
import io
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("muranga_gis.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("MurangaGIS")


class MurangaGISRepo:
    """Main class for managing the Muranga County GIS repository."""

    # Muranga County bounding box coordinates (approximate)
    # Format: [min_lon, min_lat, max_lon, max_lat]
    MURANGA_BBOX = [36.7, -0.95, 37.35, -0.45]

    # Muranga County administrative boundary search string for OSM
    MURANGA_ADMIN_QUERY = "Muranga County, Kenya"

    def __init__(self, base_dir="muranga_gis_data"):
        """Initialize the GIS repository with directory structure."""
        self.base_dir = base_dir
        self.dirs = {
            "vector": os.path.join(base_dir, "vector"),
            "raster": os.path.join(base_dir, "raster"),
            "processed": os.path.join(base_dir, "processed"),
            "output": os.path.join(base_dir, "output"),
            "cache": os.path.join(base_dir, "cache"),
            "config": os.path.join(base_dir, "config")
        }

        # Create directory structure
        self._setup_directories()

        # Load or create config
        self.config_file = os.path.join(self.dirs["config"], "config.ini")
        self.config = self._load_config()

        # Initialize data holders
        self.admin_boundaries = None
        self.roads = None
        self.poi = None
        self.dem = None

        logger.info(
            f"Initialized Muranga GIS repository at {os.path.abspath(base_dir)}")

    def _setup_directories(self):
        """Create the directory structure for the GIS repository."""
        for dir_name, dir_path in self.dirs.items():
            os.makedirs(dir_path, exist_ok=True)
            # Create subdirectories for vector data
            if dir_name == "vector":
                os.makedirs(os.path.join(dir_path, "admin"), exist_ok=True)
                os.makedirs(os.path.join(dir_path, "transport"), exist_ok=True)
                os.makedirs(os.path.join(dir_path, "hydro"), exist_ok=True)
                os.makedirs(os.path.join(dir_path, "poi"), exist_ok=True)
                os.makedirs(os.path.join(dir_path, "landuse"), exist_ok=True)
            # Create subdirectories for raster data
            elif dir_name == "raster":
                os.makedirs(os.path.join(dir_path, "elevation"), exist_ok=True)
                os.makedirs(os.path.join(dir_path, "landcover"), exist_ok=True)
                os.makedirs(os.path.join(dir_path, "imagery"), exist_ok=True)

        logger.info("Directory structure created successfully")

    def _load_config(self):
        """Load configuration or create default if it doesn't exist."""
        config = configparser.ConfigParser()

        if os.path.exists(self.config_file):
            config.read(self.config_file)
            logger.info(
                f"Loaded existing configuration from {self.config_file}")
        else:
            # Create default configuration
            config["API_KEYS"] = {
                "google_maps": "",
                "bing_maps": ""
            }

            config["DATA_SOURCES"] = {
                "use_osm": "yes",
                "use_geofabrik": "yes",
                "use_gadm": "yes",
                "use_srtm": "yes",
                "use_sentinel": "no"  # Requires registration
            }

            config["MURANGA"] = {
                "bbox_min_lon": "36.7",
                "bbox_min_lat": "-0.95",
                "bbox_max_lon": "37.35",
                "bbox_max_lat": "-0.45",
                "admin_level": "4"  # County level in OSM
            }

            # Write the configuration file
            with open(self.config_file, 'w') as f:
                config.write(f)

            logger.info(
                f"Created new default configuration at {self.config_file}")

        return config

    def fetch_admin_boundaries(self, force_refresh=False):
        """Fetch administrative boundaries for Muranga County."""
        output_file = os.path.join(
            self.dirs["vector"], "admin", "muranga_boundary.geojson")

        # Check if we already have the data and aren't forcing a refresh
        if os.path.exists(output_file) and not force_refresh:
            logger.info(
                f"Loading existing admin boundaries from {output_file}")
            self.admin_boundaries = gpd.read_file(output_file)
            return self.admin_boundaries

        try:
            # Fetch county boundary from OSM
            logger.info(
                "Fetching Muranga County boundary from OpenStreetMap...")
            gdf = ox.geocode_to_gdf(self.MURANGA_ADMIN_QUERY)

            # Save to GeoJSON
            gdf.to_file(output_file, driver="GeoJSON")
            logger.info(f"Saved admin boundaries to {output_file}")

            self.admin_boundaries = gdf
            return gdf

        except Exception as e:
            logger.error(f"Error fetching admin boundaries: {str(e)}")

            # Fallback to GADM data if OSM fails
            try:
                logger.info("Attempting to fetch from GADM dataset...")
                # This would typically involve downloading from GADM.org
                # For now, we'll just log that this is a placeholder
                logger.info(
                    "GADM implementation is a placeholder - implement full download")

                # Return None as we don't have a real implementation yet
                return None

            except Exception as fallback_error:
                logger.error(
                    f"Fallback to GADM also failed: {str(fallback_error)}")
                return None

    def fetch_transport_network(self, network_type="all", force_refresh=False):
        """
        Fetch transportation network data for Muranga County.

        Parameters:
        -----------
        network_type : str
            Type of network to fetch. Options: "all", "roads", "railways"
        force_refresh : bool
            Whether to force refresh the data even if it exists
        """
        output_file = os.path.join(
            self.dirs["vector"], "transport", f"muranga_{network_type}.geojson")

        # Check if we already have the data and aren't forcing a refresh
        if os.path.exists(output_file) and not force_refresh:
            logger.info(
                f"Loading existing transport network from {output_file}")
            self.roads = gpd.read_file(output_file)
            return self.roads

        try:
            # Get the admin boundary to use as the query area
            if self.admin_boundaries is None:
                self.fetch_admin_boundaries()

            # Use the bounding box for now
            bbox = self.MURANGA_BBOX

            # Fetch roads from OSM
            logger.info(
                f"Fetching {network_type} network for Muranga County from OpenStreetMap...")

            # Determine network type
            if network_type == "roads" or network_type == "all":
                G = ox.graph_from_bbox(
                    bbox[3], bbox[1], bbox[2], bbox[0],
                    network_type="drive",
                    simplify=True
                )

                # Convert graph to GeoDataFrame
                gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

                # Save to GeoJSON
                output_edges = os.path.join(
                    self.dirs["vector"], "transport", "muranga_roads_edges.geojson")
                output_nodes = os.path.join(
                    self.dirs["vector"], "transport", "muranga_roads_nodes.geojson")

                gdf_edges.to_file(output_edges, driver="GeoJSON")
                gdf_nodes.to_file(output_nodes, driver="GeoJSON")

                logger.info(
                    f"Saved road network to {output_edges} and {output_nodes}")

                self.roads = gdf_edges
                return gdf_edges

            # Add support for railways if needed

        except Exception as e:
            logger.error(f"Error fetching transport network: {str(e)}")
            return None

    def fetch_elevation_data(self, force_refresh=False):
        """Fetch digital elevation model (DEM) data for Muranga County."""
        output_file = os.path.join(
            self.dirs["raster"], "elevation", "muranga_dem.tif")

        # Check if we already have the data and aren't forcing a refresh
        if os.path.exists(output_file) and not force_refresh:
            logger.info(f"Loading existing elevation data from {output_file}")
            self.dem = rasterio.open(output_file)
            return self.dem

        # This is a placeholder - in a real implementation, you would:
        # 1. Download SRTM or other DEM data (e.g. from USGS Earth Explorer)
        # 2. Clip to Muranga County boundary
        # 3. Save as GeoTIFF

        logger.info(
            "Fetch elevation data placeholder - implement full download")
        logger.info(
            "For SRTM data, consider using elevation package or downloading directly from USGS")

        return None

    def fetch_poi_data(self, poi_type="all", force_refresh=False):
        """
        Fetch points of interest for Muranga County.

        Parameters:
        -----------
        poi_type : str
            Type of POIs to fetch. Options: "all", "education", "health", "commercial", etc.
        force_refresh : bool
            Whether to force refresh the data even if it exists
        """
        output_file = os.path.join(
            self.dirs["vector"], "poi", f"muranga_poi_{poi_type}.geojson")

        # Check if we already have the data and aren't forcing a refresh
        if os.path.exists(output_file) and not force_refresh:
            logger.info(f"Loading existing POI data from {output_file}")
            self.poi = gpd.read_file(output_file)
            return self.poi

        try:
            # Get the admin boundary to use as the query area
            if self.admin_boundaries is None:
                self.fetch_admin_boundaries()

            # Use the bounding box for now
            bbox = self.MURANGA_BBOX

            # Define tags to fetch based on poi_type
            tags = {}
            if poi_type == "education" or poi_type == "all":
                tags["amenity"] = ["school", "university",
                                   "college", "kindergarten"]
            if poi_type == "health" or poi_type == "all":
                tags["amenity"] = ["hospital", "clinic", "doctors", "pharmacy"]
            if poi_type == "commercial" or poi_type == "all":
                tags["shop"] = True

            # Fetch POIs from OSM
            logger.info(
                f"Fetching {poi_type} POIs for Muranga County from OpenStreetMap...")

            # Get POIs using OSMnx
            if tags:
                gdf = ox.geometries_from_bbox(
                    bbox[3], bbox[1], bbox[2], bbox[0],
                    tags
                )

                # Save to GeoJSON if we have data
                if not gdf.empty:
                    gdf.to_file(output_file, driver="GeoJSON")
                    logger.info(f"Saved POI data to {output_file}")

                    self.poi = gdf
                    return gdf
                else:
                    logger.warning(f"No POI data found for type: {poi_type}")
                    return None
            else:
                logger.warning(f"No tags defined for POI type: {poi_type}")
                return None

        except Exception as e:
            logger.error(f"Error fetching POI data: {str(e)}")
            return None

    def create_basic_map(self, output_file=None):
        """Create a basic map of Muranga County with key features."""
        # Ensure we have the necessary data
        if self.admin_boundaries is None:
            self.fetch_admin_boundaries()
        if self.roads is None:
            self.fetch_transport_network(network_type="roads")

        # Create a Folium map centered on Muranga County
        # Get the center of the county
        if self.admin_boundaries is not None:
            center_point = self.admin_boundaries.unary_union.centroid
            center = [center_point.y, center_point.x]
        else:
            # Use a default center based on the bounding box
            center = [
                (self.MURANGA_BBOX[1] + self.MURANGA_BBOX[3]) / 2,
                (self.MURANGA_BBOX[0] + self.MURANGA_BBOX[2]) / 2
            ]

        # Create the base map
        m = folium.Map(location=center, zoom_start=10, control_scale=True)

        # Add the admin boundary
        if self.admin_boundaries is not None:
            folium.GeoJson(
                self.admin_boundaries,
                name="Muranga County",
                style_function=lambda x: {
                    'fillColor': '#3186cc',
                    'color': '#000000',
                    'fillOpacity': 0.1,
                    'weight': 2
                }
            ).add_to(m)

        # Add the road network
        if self.roads is not None:
            folium.GeoJson(
                self.roads,
                name="Road Network",
                style_function=lambda x: {
                    'color': '#FF0000',
                    'weight': 1.5
                }
            ).add_to(m)

        # Add layer control
        folium.LayerControl().add_to(m)

        # Add a title
        title_html = '''
             <h3 align="center" style="font-size:16px"><b>Muranga County Geographic Features</b></h3>
             '''
        m.get_root().html.add_child(folium.Element(title_html))

        # Save the map if output file is specified
        if output_file:
            output_path = os.path.join(self.dirs["output"], output_file)
            m.save(output_path)
            logger.info(f"Saved basic map to {output_path}")

        return m

    def create_sector_suitability_map(self, sector="agriculture", output_file=None):
        """
        Create a suitability map for a specific economic sector in Muranga County.

        Parameters:
        -----------
        sector : str
            Economic sector to analyze. Options: "agriculture", "manufacturing", "tourism"
        output_file : str
            Name of output file to save the map
        """
        # This is a placeholder implementation - a real implementation would:
        # 1. Load multiple data layers (elevation, slope, land cover, etc.)
        # 2. Apply sector-specific suitability criteria
        # 3. Generate a combined suitability index
        # 4. Visualize the results

        logger.info(
            f"Creating {sector} suitability map (placeholder implementation)")

        # Create a simple map for now
        m = self.create_basic_map()

        # Add a title specific to the sector
        title_html = f'''
             <h3 align="center" style="font-size:16px"><b>Muranga County {sector.capitalize()} Suitability</b></h3>
             '''
        m.get_root().html.add_child(folium.Element(title_html))

        # Save the map if output file is specified
        if output_file:
            output_path = os.path.join(self.dirs["output"], output_file)
            m.save(output_path)
            logger.info(f"Saved {sector} suitability map to {output_path}")

        return m

    def create_infrastructure_gap_map(self, infrastructure_type="all", output_file=None):
        """
        Create a map showing infrastructure gaps in Muranga County.

        Parameters:
        -----------
        infrastructure_type : str
            Type of infrastructure to analyze. Options: "all", "transport", "energy", "water"
        output_file : str
            Name of output file to save the map
        """
        # This is a placeholder implementation - a real implementation would:
        # 1. Load infrastructure data
        # 2. Analyze coverage and identify gaps
        # 3. Visualize the results

        logger.info(
            f"Creating {infrastructure_type} infrastructure gap map (placeholder implementation)")

        # Create a simple map for now
        m = self.create_basic_map()

        # Add a title specific to the infrastructure type
        title_html = f'''
             <h3 align="center" style="font-size:16px"><b>Muranga County {infrastructure_type.capitalize()} Infrastructure Gaps</b></h3>
             '''
        m.get_root().html.add_child(folium.Element(title_html))

        # Save the map if output file is specified
        if output_file:
            output_path = os.path.join(self.dirs["output"], output_file)
            m.save(output_path)
            logger.info(
                f"Saved {infrastructure_type} infrastructure gap map to {output_path}")

        return m

    def create_market_access_map(self, output_file=None):
        """Create a map showing market access in Muranga County."""
        # This is a placeholder implementation - a real implementation would:
        # 1. Load road network data
        # 2. Calculate travel times to major markets
        # 3. Generate isochrones
        # 4. Visualize the results

        logger.info("Creating market access map (placeholder implementation)")

        # Create a simple map for now
        m = self.create_basic_map()

        # Add a title
        title_html = '''
             <h3 align="center" style="font-size:16px"><b>Muranga County Market Access</b></h3>
             '''
        m.get_root().html.add_child(folium.Element(title_html))

        # Save the map if output file is specified
        if output_file:
            output_path = os.path.join(self.dirs["output"], output_file)
            m.save(output_path)
            logger.info(f"Saved market access map to {output_path}")

        return m

    def create_3d_terrain_visualization(self, output_file=None):
        """Create a 3D terrain visualization of Muranga County."""
        # This is a placeholder implementation - a real implementation would:
        # 1. Load elevation data
        # 2. Create a 3D visualization
        # 3. Add additional layers (e.g., land cover, roads)

        logger.info(
            "Creating 3D terrain visualization (placeholder implementation)")
        logger.info(
            "For actual implementation, consider using libraries like pyvista or plotly")

        # Return None for now
        return None


def main():
    """Main function to demonstrate the use of the MurangaGISRepo class."""
    # Create a new GIS repository
    repo = MurangaGISRepo()

    # Fetch administrative boundaries
    repo.fetch_admin_boundaries()

    # Fetch road network
    repo.fetch_transport_network(network_type="roads")

    # Create a basic map
    repo.create_basic_map(output_file="muranga_basic_map.html")

    # Create sector suitability maps
    repo.create_sector_suitability_map(
        sector="agriculture", output_file="muranga_agriculture_suitability.html")
    repo.create_sector_suitability_map(
        sector="manufacturing", output_file="muranga_manufacturing_suitability.html")

    # Create infrastructure gap map
    repo.create_infrastructure_gap_map(
        infrastructure_type="transport", output_file="muranga_transport_gaps.html")

    # Create market access map
    repo.create_market_access_map(output_file="muranga_market_access.html")

    logger.info("All maps created successfully!")
    logger.info(f"Output directory: {os.path.abspath(repo.dirs['output'])}")


if __name__ == "__main__":
    main()
