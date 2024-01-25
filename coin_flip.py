import random

flip_results = ['heads', 'tails']
flip_count = 20
counts = {'heads': 0, 'tails': 0}

def flip_coin(flip_count: int) -> None:
    """
    Simulates flipping a coin for a given number of times and prints the results.

    Parameters:
    flip_count (int): The number of times to flip the coin.

    Returns:
    None
    """
    print("Options:", flip_results)

    for i in range(1, flip_count + 1):
        print(f"Flip {i}...")
        result = random.choice(flip_results)
        print("The result is:", result, "\n")
        counts[result] += 1

    print("After", flip_count, "flips, the results are:")
    print(60 * "-")
    print(f"Heads: {counts['heads']} - {(counts['heads'] / flip_count) * 100:.2f}%")
    print(f"Tails: {counts['tails']} - {(counts['tails'] / flip_count) * 100:.2f}%")
    print(60 * "-", "\n")

    print("That's all folks!")

flip_coin(flip_count)
