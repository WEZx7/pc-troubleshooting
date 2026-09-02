# PC Troubleshooting Tool

An interactive Python command-line tool for diagnosing and troubleshooting common PC hardware and software issues.

## Features

### PC Won't Power On
Helps identify possible power-related issues such as:
- Power cable problems
- PSU issues
- Front panel connector problems
- Missing motherboard power connections

### PC Powers On But No Display
Checks common display and POST-related problems:
- RAM seating
- GPU power
- Display cables
- Motherboard video output
- Debug LEDs

### Random Shutdowns / Restarts
Helps diagnose:
- Overheating
- PSU instability
- RAM issues
- Driver crashes
- Motherboard problems

### Overheating
Checks for:
- Dust buildup
- Poor airflow
- Fan problems
- Old thermal paste
- High CPU or GPU load

### Slow Performance
Helps identify:
- Too many startup applications
- High CPU or memory usage
- Low storage space
- Malware
- Slow storage drives
- Thermal throttling

### Boot / Windows Startup Problems
Troubleshoots:
- Boot drive detection
- BIOS boot order
- Corrupted bootloader
- Windows startup errors
- Failed updates
- Driver conflicts

### BSOD / Blue Screen
Helps diagnose:
- Faulty drivers
- RAM instability
- Overheating
- Storage errors
- PSU instability
- Corrupted system files

### Storage Drive Problems
Checks:
- Missing drives
- SATA and power connections
- Drive health
- SMART warnings
- Slow or failing storage
- File system errors

### Network Problems
Helps diagnose:
- Wi-Fi or Ethernet issues
- Router problems
- DNS or IP configuration
- Weak Wi-Fi signal
- Network congestion
- ISP problems

### Troubleshooting Report Generator
Creates a text report containing:
- Diagnosed problem
- Possible cause
- Recommended action
- Date and time

The report is saved as:

```text
troubleshooting_report.txt
How to Run

Make sure Python 3 is installed.

Clone the repository:

git clone https://github.com/WEZx7/pc-troubleshooting.git

Navigate to the project directory:

cd pc-troubleshooting

Run the tool:

python main.py
Example Menu
================================
       PC TROUBLESHOOTING
================================
1. PC Won't Power On
2. PC Powers On But No Display
3. Random Shutdowns / Restarts
4. Overheating
5. Slow Performance
6. Boot / Windows Startup Problems
7. BSOD / Blue Screen
8. Storage Drive Problems
9. Network Problems
10. Generate Troubleshooting Report
11. Exit
## Project Purpose

This project was created to practice Python programming while building a practical troubleshooting assistant for common IT support scenarios.

It demonstrates:
- Troubleshooting logic
- User input handling
- Decision-based workflows
- Basic error handling
- Report generation
- Hardware and software troubleshooting concepts

## Future Improvements

Planned improvements include:
- More detailed diagnostic decision trees
- Automatic system information detection
- Automatic network testing
- Better Windows-specific diagnostics
- GUI version
- Exporting reports in multiple formats

## Technologies Used

- Python 3
- datetime
- Command-line interface

## Author

Feras M. Jubran
