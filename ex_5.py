"""Module for counting descendants in a family tree from a file."""

import sys


def read_data() -> list:
    """
    Read and parse the family tree data file from user input.

    Prompts user for filename, reads the file content,
    and returns non-empty lines as a list without trailing newlines.

    Returns:
        list: List of strings, each representing a non-empty line from the file.

    Raises:
        SystemExit: If file cannot be found or opened.
    """
    filename = input('Enter file name -> ')
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Read all lines, filtering out empty ones
            file_content = [line.strip() for line in file if line.strip()]
    except (FileNotFoundError, FileExistsError) as e:
        print(f'Error - {e}')
        sys.exit(1)
    return file_content


def build_tree(data: list) -> dict:
    """
    Build a family tree structure from the input data.

    First line of file should contain the number of relationships.
    Subsequent lines contain parent-child pairs separated by space.
    Each parent is mapped to a list of their children.

    Args:
        data (list): List of strings from the file.

    Returns:
        dict: Dictionary with parents as keys and lists of children as values.
    """
    tree = {}
    number_of_relations = int(data[0])

    # Process only the relationship lines (indices 1 to number_of_relations)
    for relation in data[1:number_of_relations + 1]:
        parts = relation.split()
        if len(parts) >= 2:  # Ensure we have both parent and child
            parent, child = parts[0], parts[1]
            tree.setdefault(parent, []).append(child)
        # Invalid lines are ignored (could add warning here)

    return tree


def count_descendants(tree: dict, person: str) -> int:
    """
    Recursively count all descendants of a given person in the family tree.

    Args:
        tree (dict): Family tree structure with parent-child relationships.
        person (str): Name of the person to count descendants for.

    Returns:
        int: Total number of descendants (children, grandchildren, etc.).
    """
    if person not in tree:
        return 0

    total_descendants = 0
    for child in tree[person]:
        # Count the child itself plus all of their descendants
        total_descendants += 1 + count_descendants(tree, child)

    return total_descendants


def main() -> None:
    """
    Main program execution.

    Reads family tree data from file, builds a tree structure,
    and counts descendants for the person specified in the last line.
    """
    # Read file content
    file_data = read_data()
    if not file_data or len(file_data) < 2:
        print('File is empty or has incorrect format')
        sys.exit(1)

    # Build family tree from relationships
    family_tree = build_tree(file_data)

    # Last line contains the person to search for
    target_person = file_data[-1]

    # Count descendants and display result
    descendant_count = count_descendants(family_tree, target_person)
    print(descendant_count)


if __name__ == '__main__':
    main()
