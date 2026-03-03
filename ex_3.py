"""Module for processing an antonyms dictionary file and performing word transformations."""

import sys


def dictionary_antonyms() -> list:
    """
    Read and parse the antonyms dictionary file from user input.

    Prompts user for filename, reads the file content,
    and returns each line as a list element without trailing newlines.

    Returns:
        list: List of strings, each representing a line from the file.

    Raises:
        SystemExit: If file cannot be found or opened.
    """
    filename = input('Enter file name -> ')
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file_content = []
            for line in file:
                file_content.append(line.strip())
    except (FileNotFoundError, FileExistsError) as e:
        print(f'Error - {e}')
        sys.exit(1)
    return file_content


def filtration(file_content: list) -> dict:
    """
    Extract antonym word pairs from file content.

    First line of file should contain the number of word pairs.
    Subsequent lines contain antonym pairs separated by space.
    Only lines with at least two parts are included.

    Args:
        file_content (list): List of strings from the antonyms dictionary file.

    Returns:
        dict: Dictionary with words as keys and their antonyms as values.
    """
    dict_ant = {}
    # First line contains count, process only up to that many entries
    for word in file_content[1:int(file_content[0]) + 1]:
        split_line = word.split()
        if len(split_line) >= 2:
            dict_ant[split_line[0]] = split_line[1]
    return dict_ant


def get_keys_by_value(dictionary_obj: dict, target_value: str) -> list:
    """
    Find all keys in a dictionary that correspond to a given value.

    Args:
        dictionary_obj (dict): Dictionary to search through.
        target_value (str): Value to search for.

    Returns:
        list: List of keys that have the target value.
    """
    return [key for key, val in dictionary_obj.items() if val == target_value]


def main() -> None:
    """
    Main program execution.

    Reads antonyms dictionary file, extracts antonym pairs,
    and transforms each word in the last line:
    - If word is a key, replace with its antonym (value)
    - If word is a value, replace with its first corresponding key
    - Otherwise, keep the word unchanged
    """
    # Read file content
    file_list = dictionary_antonyms()
    if not file_list:
        sys.exit(1)

    # Create antonyms dictionary
    dict_ant = filtration(file_list)

    # Process last line words
    transformed_words = []
    for word in file_list[-1].split():
        if word in dict_ant:
            # Word found as key - replace with its antonym
            transformed_words.append(dict_ant[word])
        else:
            # Check if word exists as a value (antonym of some key)
            keys = get_keys_by_value(dict_ant, word)
            if keys:
                # Word found as value - replace with first corresponding key
                transformed_words.append(keys[0])
            else:
                # Word not found in dictionary - keep unchanged
                transformed_words.append(word)

    # Display transformed text
    print(' '.join(transformed_words))


if __name__ == '__main__':
    main()
