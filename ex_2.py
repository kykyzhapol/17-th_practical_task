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
    dict_ruen = {}
    for word in file[1:int(file[0])+1]:
        help_l = word.split()
        if len(help_l) >= 2:
            dict_ruen[help_l[0]] = help_l[1]
    return dict_ruen

def main() -> None:
    f_list = dictionary()
    if not f_list:
        sys.exit(1)
    dict_ru = filtration(f_list)
    exit_list = []
    for let in f_list[-1].split():
        if let in dict_ru:
            exit_list.append(dict_ru[let])
        else:
            exit_list.append(let)

    print(' '.join(exit_list))


if __name__ == '__main__':
    main()