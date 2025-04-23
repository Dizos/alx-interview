#!/usr/bin/python3
"""
This module contains a method to determine if all locked boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened starting from box 0.

    Args:
        boxes (List[List[int]]): A list of lists where each inner list contains
                                keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # Box 0 is unlocked
    queue = [0]  # Start with box 0

    while queue:
        current_box = queue.pop(0)  # Get the next box to process
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            # Check if the key is valid and the box hasn't been visited
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)  # Add the newly unlocked box to the queue

    # Return True if all boxes are visited, False otherwise
    return all(visited)
