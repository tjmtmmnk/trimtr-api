import os


class Util:
    @classmethod
    def get_abbrev_types(cls) -> set:
        abbrev_types = set()

        directory = os.path.dirname(os.path.abspath(__file__)) + "/"
        with open(directory + 'abbrev_types.txt', 'r') as f:
            abbrev_list = f.readlines()
            for abbrev in abbrev_list:
                if abbrev != "":
                    abbrev = abbrev.replace("\n", "")
                    abbrev_types.add(abbrev)

        return abbrev_types
