"""Module for counting and displaying word frequencies in a user-input string."""

import sys
from collections import OrderedDict


def input_str() -> list:
    """
    Read and process user input string.

    Prompts the user to enter a string, converts it to lowercase,
    and splits it into words using space as delimiter.

    Returns:
        list: List of lowercase words from user input.

    Raises:
        SystemExit: If input reading fails with ValueError.
    """
    try:
        user_input = input('Enter string using space as separator: ').lower().split()
        return user_input
    except ValueError as e:
        print(f'Error - {e}')
        sys.exit(1)


def main() -> None:
    """
    Main program execution.

    Reads input string, counts frequency of each unique word,
    sorts them alphabetically, and displays the results.
    """
    # Get list of words from user
    words_list = input_str()

    # Count frequency of each unique word
    frequency_dict = {}
    for unique_word in set(words_list):
        frequency_dict[unique_word] = words_list.count(unique_word)

    # Sort dictionary by keys (words) alphabetically
    sorted_dict = OrderedDict(
        sorted(frequency_dict.items(), key=lambda item: item[0])
    )

    # Display each unique word
    for word in sorted_dict.keys():
        print(word)


if __name__ == '__main__':
    main()
