import os


def get_abs_path() -> str:
    return os.path.dirname(os.path.abspath(__file__)) + "/"


def get_abbrev_types_from_file() -> set:
    abbrev_types = set()

    with open(get_abs_path() + 'abbrev_types.txt', 'r') as f:
        abbrev_list = f.readlines()
        for abbrev in abbrev_list:
            if abbrev != "":
                abbrev = abbrev.replace("\n", "")
                abbrev_types.add(abbrev)

    return abbrev_types
