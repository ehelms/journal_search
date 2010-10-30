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
