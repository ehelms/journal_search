from journal_search.document.spreadsheet import GoogleSpreadsheet
from journal_search import settings

def run():
    gs = GoogleSpreadsheet()

    for search_engine in settings.SEARCH_ENGINES:
        print "Eliminating duplicates..."
        data = eliminate_duplicates(gs, search_engine["worksheet_id"])
        print "Inserting titles set....."
        gs.insert_data(len(settings.SEARCH_CRITERIA) + 1, data,
                       search_engine["worksheet_id"])
        print "Done."


def eliminate_duplicates(google_spreadsheet, worksht_id=1):
    titles = get_titles(google_spreadsheet, worksht_id)
    return titles


def get_titles(google_spreadsheet, worksht_id):
    feed = google_spreadsheet.get_rows(worksht_id)
    titles = set()
    for entry in feed.entry:
        for item in iter(entry.custom):
            titles.add(entry.custom[item].text)
    return titles
