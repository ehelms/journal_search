import unittest

from journal_search.search_engines.ieeexplore import IEEEXploreSearch

class TestIEEEXplore(unittest.TestCase):

    def setUp(self):
        self.ieeexplore = IEEEXploreSearch()
        self.search_terms = ["role", "based", "access"]

    def test_connectivity(self):
        resp = self.ieeexplore.get_response(self.search_terms)
        self.assertNotEqual(resp, None)

    def test_results(self):
        resp = self.ieeexplore.get_response(self.search_terms)
        self.assertNotEqual(len(resp.read().split("detail")), 9)
    
    def test_search(self):
        resp = self.ieeexplore.search(self.search_terms)
        self.assertEqual(len(resp), 25)
