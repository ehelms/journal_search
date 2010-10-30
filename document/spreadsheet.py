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
        self.set_worksheet_size(len(data), worksheet_id)
        #batch_request = gdata.spreadsheet.SpreadsheetsCellsFeed()
        for item in data:
            #batch_request.AddUpdate(self.get_cell(row_counter, column, item))
            print "Inserting item " + str(row_counter)
            self.insert_cell(row_counter, column, item, worksheet_id)
            row_counter = row_counter + 1
            print "Inserted"
        #updated = self.client.ExecuteBatch(batch_request)
    

    def set_worksheet_size(self, num_rows, worksheet_id=1):
        worksheet = self.client.GetWorksheetsFeed(settings.SPREADSHEET_KEY,
                                                  wksht_id = worksheet_id)
        worksheet.row_count.text = str(num_rows + 1)
        entry = self.client.UpdateWorksheet(worksheet)
        
        if isinstance(entry, gdata.spreadsheet.SpreadsheetsWorksheet):
            return True
        else:
            return False


    def get_cell(self, row, column, data):
        cell = gdata.spreadsheet.Cell()
        cell.row = row
        cell.col = column
        cell.inputValue = data
        cell.batch_id = cell
        return cell


    def insert_cell(self, row, column, data, worksheet_id=1):
        entry = self.client.UpdateCell(row, column, data, settings.SPREADSHEET_KEY, wksht_id = worksheet_id)


    def insert_row(self, data):
        entry = self.client.InsertRow(data, settings.SPREADSHEET_KEY,
                                      settings.WORKSHEET_ID)
        if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
            return True
        else:
            print False


    def get_rows(self, worksht_id=1):
        row = self.client.GetListFeed(settings.SPREADSHEET_KEY,
                                        worksht_id)
        return row
    
    
    def get_cells(self):
        return self.client.GetCellsFeed(settings.SPREADSHEET_KEY, 1)
