# ACI Port Monitoring and Capacity Analysis Tools

A collection of Python scripts for monitoring, analyzing, and reporting on Cisco ACI fabric port states and capacity.

## Scripts

| File Name                   | Description                                                                                                                       |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `port_capacity_analyzer.py` | Main utility for analyzing port capacity across large ACI fabrics with multi-pod support. Generates detailed utilization reports. |
| `monitoring_port_states.py` | Basic utility for monitoring port states in real-time.                                                                            |
| `port_state_analyzer_v2.py` | Enhanced port state analysis tool (version 2).                                                                                    |
| `port_state_basic.py`       | Simplified version for basic port state retrieval.                                                                                |
| `retrieve_device_info.py`   | Utility for retrieving basic device information from ACI fabric.                                                                  |
| `session_based_client.py`   | Session-based ACI API client with connection management.                                                                          |

## Usage

To use the main port capacity analyzer:

```bash
python port_capacity_analyzer.py
```

## Default Credentials

The scripts use these default credentials for the Cisco ACI sandbox:

```
URL: https://sandboxapicdc.cisco.com
Username: admin
Password: !v3G@!4@Y

NOTE: The above credentials are for the Cisco ACI sandbox environment only.
For production deployments:
1. Create a .env file to manage credentials securely:

## Requirements

- Python 3.6+
- Required Python packages:
  - requests
  - pandas
  - openpyxl (for Excel output)
  - tqdm (for progress bars)
  - urllib3

## 📁 Output Directories

The tools generate various report directories with detailed analysis:

- **aci_capacity_report_TIMESTAMP**: Contains capacity analysis including CSV, Excel, and text reports
  - `port_capacity.csv` - Raw data export
  - `port_capacity.xlsx` - Multi-sheet workbook with pod-specific tabs
  - `capacity_summary.txt` - Text summary with key utilization metrics

- **aci_report_TIMESTAMP**: Contains interface state reports
  - `fabric_summary.txt` - Overview of fabric nodes
  - `node_interfaces.txt` - Detailed interface information by node
  - `all_interfaces.csv` - Complete interface data export

## ⚡ Performance Tuning 

For large deployments (200+ nodes), adjust these parameters in `port_capacity_analyzer.py`:

```python
# Performance optimization settings
MAX_WORKERS = 5      # Number of concurrent requests (increase for faster collection)
REQUEST_DELAY = 0.5  # Delay between requests in seconds (increase if hitting rate limits)
BATCH_SIZE = 50      # Nodes processed before pausing (decrease for slower APICs)
BATCH_PAUSE = 2      # Seconds to pause between batches (increase for slower APICs)
```

Recommended values:
- For small fabrics (<50 nodes): `MAX_WORKERS=10, REQUEST_DELAY=0.2`
- For medium fabrics (50-200 nodes): `MAX_WORKERS=5, REQUEST_DELAY=0.5`
- For large fabrics (>200 nodes): `MAX_WORKERS=3, REQUEST_DELAY=1.0, BATCH_SIZE=25`

## 🔧 Troubleshooting

### Common Issues

1. **Connection Errors**
   - Verify APIC URL is correct
   - Check network connectivity (including firewalls)
   - Confirm SSL certificate settings

2. **Authentication Failures**
   - Verify username and password
   - Check user account permissions (read access needed)
   - Ensure account is not locked

3. **Data Collection Errors**
   - "Node unavailable" - Node may be offline or unreachable
   - "Request timeout" - Increase request timeouts or reduce parallelism
   - "Too many requests" - Increase REQUEST_DELAY to avoid rate limiting

4. **Report Generation Issues**
   - Missing openpyxl package: `pip install openpyxl`
   - Directory permissions: Ensure write access to current directory
   - Large report failures: Reduce collection scope or filter by pod/node

## 🔄 Regular Monitoring

For ongoing capacity management, set up automated collection:

### Windows (PowerShell)

```powershell
# Daily capacity report at 2:00 AM
$action = New-ScheduledTaskAction -Execute 'python' -Argument 'C:\path\to\port_capacity_analyzer.py'
$trigger = New-ScheduledTaskTrigger -Daily -At 2am
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "ACI Capacity Report" -Description "Daily ACI port capacity analysis"
```

### Linux (Cron)

```bash
# Edit crontab
crontab -e

# Add daily capacity report at 2:00 AM
0 2 * * * cd /path/to/aci_tools && python port_capacity_analyzer.py
```

## 📝 Development History

### PEP 8 Compliance Refactoring

The codebase has been refactored to follow Python best practices according to [PEP 8](https://www.python.org/dev/peps/pep-0008/), particularly regarding file naming conventions:

#### Original Filenames (Non-Standard)
- `Monitoring Port States.PY`
- `RETRetrieve basic device informatioN.PY`
- `RETRIEAVE_PORT_STATE copy 2.PY`
- `RETRIEAVE_PORT_STATE copy.PY`
- `RETRIEAVE_PORT_STATE.py`
- `session-Based Device Interaction.PY`

#### Refactored Filenames (PEP 8 Compliant)
- `monitoring_port_states.py`
- `retrieve_device_info.py`
- `port_state_analyzer_v2.py`
- `port_state_basic.py`
- `port_capacity_analyzer.py`
- `session_based_client.py`

This refactoring follows Python naming conventions by:
- Using all lowercase letters for filenames
- Using underscores to separate words (snake_case)
- Eliminating spaces in filenames
- Using consistent lowercase `.py` extensions
- Using descriptive names that indicate the purpose of each file

The repository structure has been reorganized to improve maintainability and follow standard Python project layouts, making it easier for contributors to understand and extend the codebase.
