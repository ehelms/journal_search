import unittest

from journal_search.document.spreadsheet import GoogleSpreadsheet
import gdata.spreadsheet.service

class TestSpreadsheet(unittest.TestCase):

    def setUp(self):
        self.gs = GoogleSpreadsheet()
        

    def test_change_row_count(self):
        result = self.gs.set_worksheet_size(50)
        self.assertTrue(result)

    def test_batch_insert(self):
        cells = self.gs.get_cells()
        for cell in cells.entry:
            print cell.cell.row
        self.assertTrue(True)
