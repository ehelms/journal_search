import unittest

from journal_search.tests.search import TestJournalSearch

def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJournalSearch)
    unittest.TextTestRunner(verbosity=2).run(suite)
