#!/bin/bash
echo '
# 0x03-log_parsing

This directory contains scripts for parsing and analyzing log data.

## Files
- `0-generator.py`: Generates random log lines for testing.
- `0-stats.py`: Reads log lines from stdin, computes metrics (total file size and status code counts), and prints stats every 10 lines or on keyboard interrupt.

## Requirements
- Ubuntu 20.04 LTS
- Python 3.4.3
- PEP 8 (version 1.7.x)
- All files must be executable
- All files must end with a newline

## Usage
- Generate logs and parse stats:
  ```bash
  ./0-generator.py | ./0-stats.py
'
