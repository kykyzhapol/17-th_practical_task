import sys


def dictionary() -> list:
    namefile = input('Enter file name ->')
    try:
        with open(namefile, 'r', encoding='utf-8') as f:
            file = []
            for line in f:
                file.append(line.strip())
    except (FileNotFoundError, FileExistsError) as e:
        print(f'Error - {e}')
        sys.exit(1)
    return file


def filtration(file: list) -> dict:
    dict_shape = {}
    for word in file[1:int(file[0]) + 1]:
        help_l = word.split()
        if len(help_l) >= 2:
            for item in help_l[1:]:
                dict_shape[item] = help_l[0]
    return dict_shape


def main() -> None:
    f_list = dictionary()
    if not f_list:
        sys.exit(1)

    dict_shape = filtration(f_list)
    last_word = f_list[-1].strip()

    if last_word in dict_shape:
        print(dict_shape[last_word])
    else:
        print('Shape is absent')


if __name__ == '__main__':
    main()
