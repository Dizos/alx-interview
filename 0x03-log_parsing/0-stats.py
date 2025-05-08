#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Print accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read input line by line
for line in sys.stdin:
    # Increment line count
    line_count += 1
    
    # Split and validate line format
    try:
        parts = line.strip().split()
        if len(parts) < 9:
            continue
            
        # Check if the line matches expected format
        if (parts[1] != '-' or 
            not parts[2].startswith('[') or 
            parts[4] != '"GET' or 
            parts[5] != '/projects/260' or 
            parts[6] != 'HTTP/1.1"'):
            continue
            
        # Extract status code and file size
        status_code = int(parts[7])
        file_size = int(parts[8])
        
        # Validate status code
        if status_code not in status_counts:
            continue
            
        # Update metrics
        total_size += file_size
        status_counts[status_code] += 1
        
    except (ValueError, IndexError):
        # Skip lines with invalid format or non-integer values
        continue
    
    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final stats if any lines were processed
if line_count > 0:
    print_stats()
