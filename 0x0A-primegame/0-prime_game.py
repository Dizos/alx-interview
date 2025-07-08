#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game for multiple rounds.
    
    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing n for each round.
    
    Returns:
        str or None: Name of the player who wins the most rounds ("Maria" or "Ben"),
                     or None if equal or no valid games.
    """
    # Handle edge cases: empty nums or invalid number of rounds
    if not nums or x < 1 or len(nums) < x:
        return None

    # If all values are less than 1, no valid games possible
    max_n = max(nums)
    if max_n < 1:
        return None

    # Sieve of Eratosthenes to identify primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Precompute prefix sum of primes for O(1) lookup
    prefix = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prefix[i] = prefix[i - 1] + (1 if sieve[i] else 0)

    # Count wins for each player
    maria_wins = 0
    ben_wins = 0
    for i in range(x):  # Only process x rounds
        n = nums[i]
        if n < 1:
            continue  # Skip invalid rounds, though problem assumes n >= 1
        prime_count = prefix[n]  # Number of primes up to n
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage and testing
if __name__ == "__main__":
    # Test case from typical problem example
    print(isWinner(3, [4, 5, 1]))  # Should determine winner based on rounds
    print(isWinner(5, [2, 5, 1, 4, 3]))  # Should output "Ben"
