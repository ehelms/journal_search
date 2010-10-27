import unittest

from journal_search.tests.search import TestJournalSearch
from journal_search.tests.engine_tests import TestIEEEXplore


def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIEEEXplore)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestJournalSearch))
    unittest.TextTestRunner(verbosity=2).run(suite)
