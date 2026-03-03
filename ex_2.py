"""Module for processing a dictionary file and translating words."""

import sys


def dictionary() -> list:
    """
    Read and parse the dictionary file from user input.

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
    Extract Russian-English word pairs from file content.

    First line of file should contain the number of word pairs.
    Subsequent lines contain word pairs separated by space.
    Only lines with at least two parts are included.

    Args:
        file_content (list): List of strings from the dictionary file.

    Returns:
        dict: Dictionary with Russian words as keys and English words as values.
    """
    dict_ru_en = {}
    # First line contains count, process only up to that many entries
    for word in file_content[1:int(file_content[0]) + 1]:
        split_line = word.split()
        if len(split_line) >= 2:
            dict_ru_en[split_line[0]] = split_line[1]
    return dict_ru_en


def main() -> None:
    """
    Main program execution.

    Reads dictionary file, extracts word pairs,
    and translates the last line's words using the dictionary.
    """
    # Read file content
    file_list = dictionary()
    if not file_list:
        sys.exit(1)

    # Create translation dictionary
    dict_ru = filtration(file_list)

    # Translate last line
    translated_words = []
    for word in file_list[-1].split():
        if word in dict_ru:
            translated_words.append(dict_ru[word])
        else:
            translated_words.append(word)

    # Display translated text
    print(' '.join(translated_words))


if __name__ == '__main__':
    main()
