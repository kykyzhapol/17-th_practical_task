import sys
from collections import OrderedDict


def input_str() -> list:
    try:
        lst = input('Enter string using space button like sep: ').lower().split()
        return lst
    except ValueError as e:
        print(f'Error - {e}')
        sys.exit(1)


def main() -> None:
    lst = input_str()
    frequency_dict = {}
    for unic in set(lst):
        frequency_dict[unic] = lst.count(unic)
    sorted_dict = OrderedDict(sorted(frequency_dict.items(), key=lambda item: item))
    for elem in sorted_dict.keys():
        print(elem)


if __name__ == '__main__':
    main()