#!/usr/bin/python3
"""
Module for parsing log lines from stdin and computing metrics
"""
import sys
import re


def print_stats(total_size, status_counts):
    """
    Prints total file size and status code counts in ascending order.

    Args:
        total_size (int): Sum of file sizes.
        status_counts (dict): Status codes to counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))
    sys.stdout.flush()


def main():
    """
    Reads stdin, computes metrics, prints stats every 10 lines or on interrupt.
    """
    # Regex for IPv4 and log format
    ip_part = r'(?:\d{1,3}\.){3}\d{1,3}'
    log_pattern = re.compile(
        r'^({}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{{3}})\s+(\d+)$'
        .format(ip_part)
    )
    
    # Initialize metrics
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                     405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            line_count += 1
            
            # Parse line
            match = log_pattern.match(line)
            if not match:
                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)
                continue
            
            # Extract and validate
            try:
                status_code = int(match.group(3))
                file_size = int(match.group(4))
            except ValueError:
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
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
