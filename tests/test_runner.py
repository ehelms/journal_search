import unittest

from journal_search.tests.search import TestJournalSearch
from journal_search.tests.engine_tests import TestIEEEXplore
from journal_search.tests.spreadsheet_tests import TestSpreadsheet


def run():
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestIEEEXplore)
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestJournalSearch))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSpreadsheet))
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSpreadsheet)
    unittest.TextTestRunner(verbosity=2).run(suite)
