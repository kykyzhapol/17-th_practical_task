"""Module for processing a shape-color dictionary file and finding shape names."""

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
    Create a mapping from colors to shapes from file content.

    First line of file should contain the number of entries.
    Subsequent lines contain a shape name followed by one or more colors.
    Each color is mapped to its corresponding shape.

    Args:
        file_content (list): List of strings from the dictionary file.

    Returns:
        dict: Dictionary with colors as keys and shapes as values.
    """
    dict_shape = {}
    # First line contains count, process only up to that many entries
    for word in file_content[1:int(file_content[0]) + 1]:
        split_line = word.split()
        if len(split_line) >= 2:
            # Map each color to the shape name
            for color in split_line[1:]:
                dict_shape[color] = split_line[0]
    return dict_shape


def main() -> None:
    """
    Main program execution.

    Reads shape-color dictionary file, creates a mapping from colors to shapes,
    and looks up the last word (color) to find its corresponding shape.
    """
    # Read file content
    file_list = dictionary()
    if not file_list:
        sys.exit(1)

    # Create color-to-shape mapping
    dict_shape = filtration(file_list)

    # Get the last word (color) to look up
    last_word = file_list[-1].strip()

    # Look up the shape for the given color
    if last_word in dict_shape:
        print(dict_shape[last_word])
    else:
        print('Shape is absent')


if __name__ == '__main__':
    main()
