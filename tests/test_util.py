import unittest
from trimtr.util import get_abbrev_types_from_file


class TestUtil(unittest.TestCase):
    def test_get_abbrev_types(self):
        abbrev_types = get_abbrev_types_from_file()
        self.assertGreater(len(abbrev_types), 0)


if __name__ == "__main__":
    unittest.main()
