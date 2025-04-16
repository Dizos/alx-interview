#!/usr/bin/python3
"""
Pascal's Triangle Module
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    
    Args:
        n (int): Number of rows to generate
        
    Returns:
        list: Empty list if n <= 0, otherwise list of lists representing Pascal's triangle
    """
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize with the first row
    
    for i in range(1, n):
        # Previous row
        prev_row = triangle[-1]
        
        # Start new row with 1
        current_row = [1]
        
        # Calculate middle elements
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            current_row.append(prev_row[j-1] + prev_row[j])
        
        # End row with 1
        current_row.append(1)
        
        # Add the current row to the triangle
        triangle.append(current_row)
    
    return triangle
