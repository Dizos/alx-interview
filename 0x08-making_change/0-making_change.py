#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations (positive integers).
        total (int): Target amount to make.

    Returns:
        int: Fewest number of coins needed to make total.
             Returns 0 if total is 0 or negative.
             Returns -1 if total cannot be made with given coins.
    """
    if total <= 0:
        return 0

    # Initialize dp array with total + 1 (unreachable value)
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # Fill dp array
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return -1 if total cannot be made, otherwise return dp[total]
    return dp[total] if dp[total] <= total else -1
