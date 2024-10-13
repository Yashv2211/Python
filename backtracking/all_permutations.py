"""
In this problem, we want to determine all possible permutations
of the given sequence. We use backtracking to solve this problem.

Time complexity: O(n! * n),
where n denotes the length of the given sequence.
"""

from __future__ import annotations


def generate_all_permutations(sequence: list[int | str]) -> list[list[int | str]]:
    """
    Generate all permutations of the given sequence.
    
    :param sequence: List of integers or strings
    :return: A list of all permutations

    Example 1:
    >>> generate_all_permutations([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    Example 2:
    >>> generate_all_permutations(["A", "B", "C"])
    [['A', 'B', 'C'], ['A', 'C', 'B'], ['B', 'A', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B'], ['C', 'B', 'A']]

    Example 3:
    >>> generate_all_permutations([1])
    [[1]]
    """
    results = []
    create_state_space_tree(sequence, [], 0, [0 for _ in range(len(sequence))], results)
    return results


def create_state_space_tree(
    sequence: list[int | str],
    current_sequence: list[int | str],
    index: int,
    index_used: list[int],
    results: list[list[int | str]],
) -> None:
    """
    Creates a state space tree to iterate through each branch using DFS.
    We know that each state has exactly len(sequence) - index children.
    It terminates when it reaches the end of the given sequence.

    :param sequence: The input sequence for which permutations are generated.
    :param current_sequence: The current permutation being built.
    :param index: The current index in the sequence.
    :param index_used: list to track which elements are used in permutation.
    :param results: List to store all generated permutations.
    """

    if index == len(sequence):
        results.append(current_sequence[:])  # Append a copy of current sequence
        return

    for i in range(len(sequence)):
        if not index_used[i]:
            current_sequence.append(sequence[i])
            index_used[i] = True
            create_state_space_tree(sequence, current_sequence, index + 1, index_used, results)
            current_sequence.pop()
            index_used[i] = False


def get_permutations():
    """
    A function that allows user input to generate permutations.
    It handles both integer and string inputs.
    """
    input_type = input("Enter 'i' for integers or 's' for strings: ").strip().lower()

    if input_type == 'i':
        sequence = list(map(int, input("Enter the integer elements separated by spaces: ").split()))
    elif input_type == 's':
        sequence = input("Enter the string elements separated by spaces: ").split()
    else:
        print("Invalid input type. Please enter 'i' or 's'.")
        return

    permutations = generate_all_permutations(sequence)
    print("Permutations:")
    for p in permutations:
        print(p)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Uncomment the following line to allow user input for generating permutations
    # get_permutations()

    # Example usage:
    sequence: list[int | str] = [3, 1, 2, 4]
    print(generate_all_permutations(sequence))

    sequence_2: list[int | str] = ["A", "B", "C"]
    print(generate_all_permutations(sequence_2))
