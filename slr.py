from journal_search.search.engines.google_scholar import GoogleScholarSearch
from journal_search.search.engines.citeseerx import CiteSeerXSearch
from journal_search.search.engines.ieeexplore import IEEEXploreSearch
from journal_search.search.engines.acm_portal import ACMPortalSearch
from journal_search.search.combiner import eliminate_duplicates
from journal_search.document.spreadsheet import GoogleSpreadsheet
from journal_search import settings


def run_search(num_results):
    gs = GoogleSpreadsheet()
    
    for search_engine in settings.SEARCH_ENGINES:
        engine = get_search_engine(search_engine["engine"])
        print "Starting search on: " + search_engine["engine"]
        print "Retrieving " + str(num_results) + " total results..."
        for criteria in settings.SEARCH_CRITERIA:
            print "Search criteria is: " + str(criteria)
            data = engine.search(criteria, num_results)
            if data:
                print "Inserting " + str(len(data))  + " results into spreadsheet..."
                gs.insert_cell(1, settings.SEARCH_CRITERIA.index(criteria) + 1,
                               " ".join(criteria), search_engine["worksheet_id"])
                gs.insert_data(settings.SEARCH_CRITERIA.index(criteria) + 1,
                               data, search_engine["worksheet_id"])
            else:
                print "Empty pubs"


def run_combine():
    gs = GoogleSpreadsheet()
    print "Eliminating duplicates..."
    titles = eliminate_duplicates(gs)
    print "Inserting titles set....."
    gs.insert_data(len(settings.SEARCH_CRITERIA) + 1, titles, 1)
    print "Done."


def get_search_engine(query):
    if "google_scholar" == query:
        google_scholar = GoogleScholarSearch()
        return google_scholar
    if "citeseerx" == query:
        citeseerx = CiteSeerXSearch()
        return citeseerx
    if "acmportal" == query:
        acmportal = ACMPortalSearch()
        return acmportal
    if "ieeexplore" == query:
        ieeexplore = IEEEXploreSearch()
        return ieeexplore
    return None
