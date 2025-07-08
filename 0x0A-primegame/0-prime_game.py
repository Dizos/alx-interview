#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of the Prime Game across multiple rounds.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers, each representing the value of n for a round.

    Returns:
        str or None: The name of the player who wins the most rounds ("Maria" or "Ben"),
                     or None if they win an equal number of rounds or input is invalid.
    """
    # Handle invalid inputs
    if not nums or x < 1 or x > len(nums):
        return None

    # Find the maximum n to compute primes up to that value
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

    # Precompute the number of primes up to each n (prefix sum)
    prime_count = [0] * (max_n + 1)
    for i in range(2, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Count wins for each player
    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        n = nums[i]
        if n < 1:
            continue
        # Number of primes determines the winner (odd: Maria, even: Ben)
        if prime_count[n] % 2 == 1:
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
