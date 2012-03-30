from journal_search.search.engines.google_scholar import GoogleScholarSearch
from journal_search.search.engines.citeseerx import CiteSeerXSearch
from journal_search.search.engines.ieeexplore import IEEEXploreSearch
from journal_search.search.engines.acm_portal import ACMPortalSearch
from journal_search.document.spreadsheet import GoogleSpreadsheet
from journal_search import settings

from string import lower

def run(num_results=None):
    gs = GoogleSpreadsheet()
    
    for search_engine in settings.SEARCH_ENGINES:
        for criteria in settings.SEARCH_CRITERIA:
            engine = _get_search_engine(search_engine["engine"])
            print "Starting search on: " + search_engine["engine"]

            if num_results:
                print "Retrieving " + str(num_results) + " total results..."

            print "Search criteria is: " + str(criteria)
            data = search(engine, criteria, num_results)

            if data:
                print "Inserting " + str(len(data))  + " results into spreadsheet..."
                gs.insert_cell(1, settings.SEARCH_CRITERIA.index(criteria) + 1,
                               " ".join(criteria), search_engine["worksheet_id"])
                gs.insert_data(settings.SEARCH_CRITERIA.index(criteria) + 1,
                               data, search_engine["worksheet_id"])
            else:
                print "Empty pubs"


def _get_search_engine(query):
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


def search(engine, criteria, num_results):
    count = 0
    titles = []

    if num_results:
        while count < num_results:
            titles.extend(engine.search(criteria, count))
            count = count + 10
    else:
        titles.extend(engine.search(criteria, count))
        count = count + 10
        if len(titles) != 0:
            while not _stop_search(criteria, titles):
                titles.extend(engine.search(criteria, count))
                print count
                count = count + 10
    return titles
    
    
def _stop_search(terms, titles):
    for i in range(len(titles) - settings.STOPPING_THRESHOLD, len(titles)):
        if _has_criteria(terms, titles[i]):
            print "not stopping"
            return False

    return True


def _has_criteria(terms, entry):
    for term in terms:
        if lower(entry).find(lower(term)) == -1:
            return False

    return True
