import urllib

import gdata.spreadsheet.service

from journal_search import settings


class GoogleSpreadsheet():
    def __init__(self):
        self.client = gdata.spreadsheet.service.SpreadsheetsService()
        self.client.email = settings.USER_EMAIL
        self.client.password = settings.USER_PASSWORD
        self.client.ProgrammaticLogin()

    
    def insert_data(self, column, data, worksheet_id=1):
        row_counter = 2
        for item in data:
            self.insert_cell(row_counter, column, item, worksheet_id)
            row_counter = row_counter + 1
    

    def insert_cell(self, row, column, data, worksheet_id=1):
        entry = self.client.UpdateCell(row, column, data,
                                       settings.SPREADSHEET_KEY,
                                       worksheet_id)


    def insert_row(self, data):
        entry = self.client.InsertRow(data, settings.SPREADSHEET_KEY,
                                      settings.WORKSHEET_ID)
        if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
            return True
        else:
            print False
