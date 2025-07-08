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
    if not nums or x < 1:
        return None

    # Find maximum n for sieve
    max_n = max(nums)
    if max_n < 1:
        return None

    # Sieve of Eratosthenes
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    # Count wins
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if n < 1:
            continue
        # Count primes from 2 to n
        prime_count = sum(1 for i in range(2, n + 1) if sieve[i])
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
