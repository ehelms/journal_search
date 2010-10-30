from journal_search.document.spreadsheet import GoogleSpreadsheet

def run():
    gs = GoogleSpreadsheet()

    for search_engine in settings.SEARCH_ENGINES:
        print "Eliminating duplicates..."
        data = eliminate_duplicates(gs)
        print "Inserting titles set....."
        gs.insert_data(len(settings.SEARCH_CRITERIA) + 1, data,
                       search_engine["worksheet_id"])
        print "Done."



def eliminate_duplicates(google_spreadsheet):
    titles = get_titles(google_spreadsheet)
    return titles


def get_titles(google_spreadsheet):
    feed = google_spreadsheet.get_rows(1)
    titles = set()
    for entry in feed.entry:
        for item in iter(entry.custom):
            titles.add(entry.custom[item].text)
    return titles
