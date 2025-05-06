#!/usr/bin/python3
"""
Module for parsing log lines from stdin and computing metrics
"""
import sys
import re


def print_stats(total_size, status_counts):
    """
    Prints the total file size and status code counts in ascending order.

    Args:
        total_size (int): Total sum of file sizes.
        status_counts (dict): Dictionary mapping status codes to their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """
    Reads stdin line by line, computes metrics, and prints stats every 10 lines
    or on keyboard interrupt.
    """
    # Regex to match the log format
    log_pattern = re.compile(
        r'^([\d.]+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    )
    
    # Initialize metrics
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            line_count += 1
            
            # Parse line
            match = log_pattern.match(line)
            if not match:
                # Print stats every 10 lines, even if invalid
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)
                continue
            
            # Extract and validate status code and file size
            try:
                status_code = int(match.group(3))
                file_size = int(match.group(4))
            except ValueError:
                # Skip lines with non-integer status code or file size
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)
                continue
            
            # Validate status code
            if status_code not in status_counts:
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)
                continue
                
            # Update metrics
            total_size += file_size
            status_counts[status_code] += 1
            
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
                
    except KeyboardInterrupt:
        # Print stats on Ctrl+C
        print_stats(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
