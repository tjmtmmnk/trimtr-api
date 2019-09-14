import unittest
from trimtr.util import Util


class TestUtil(unittest.TestCase):
    def test_get_abbrev_types(self):
        util = Util()
        abbrev_types = util.get_abbrev_types()
        self.assertGreater(len(abbrev_types), 0)


if __name__ == "__main__":
    unittest.main()
