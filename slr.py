from journal_search.search.engines.google_scholar import GoogleScholarSearch
from journal_search.search.engines.citeseerx import CiteSeerXSearch
from journal_search.search.engines.ieeexplore import IEEEXploreSearch
from journal_search.search.engines.acm_portal import ACMPortalSearch
from journal_search.search.combiner import eliminate_duplicates
from journal_search.document.spreadsheet import GoogleSpreadsheet
from journal_search import settings


def run_search(num_results):
    gs = GoogleSpreadsheet()
    search_engines = get_search_engines()
    
    for engine in search_engines:
        print "Starting search on: " + str(settings.SEARCH_ENGINES[search_engines.index(engine)])
        print "Retrieving " + str(num_results) + " total results..."
        for criteria in settings.SEARCH_CRITERIA:
            print "Search criteria is: " + str(criteria)
            data = engine.search(criteria, num_results)
            if data:
                print "Inserting " + str(len(data))  + " results into spreadsheet..."
                gs.insert_cell(1, settings.SEARCH_CRITERIA.index(criteria) + 1, " ".join(criteria), search_engines.index(engine) + 1)
                gs.insert_data(settings.SEARCH_CRITERIA.index(criteria) + 1, data, search_engines.index(engine) + 1)
            else:
                print "Empty pubs"


def run_combine():
    gs = GoogleSpreadsheet()
    print "Eliminating duplicates..."
    titles = eliminate_duplicates(gs)
    print "Inserting titles set....."
    gs.insert_data(4, titles, 1)
    print "Done."


def get_search_engines():
    engines = []
    if "google_scholar" in settings.SEARCH_ENGINES:
        google_scholar = GoogleScholarSearch()
        engines.append(google_scholar)
    if "citeseerx" in settings.SEARCH_ENGINES:
        citeseerx = CiteSeerXSearch()
        engines.append(citeseerx)
    if "acmportal" in settings.SEARCH_ENGINES:
        acmportal = ACMPortalSearch()
        engines.append(acmportal)
    if "ieeexplore" in settings.SEARCH_ENGINES:
        ieeexplore = IEEEXploreSearch()
        engines.append(ieeexplore)
    return engines
