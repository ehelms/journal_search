from journal_search.search_engines.google_scholar import GoogleScholarSearch
from journal_search.search_engines.citeseerx import CiteSeerXSearch
from journal_search.search_engines.ieeexplore import IEEEXploreSearch
from journal_search.search_engines.acm_portal import ACMPortalSearch
from journal_search.document.spreadsheet import GoogleSpreadsheet
from journal_search import settings


def run_search():
    gs = GoogleSpreadsheet()
    search_engines = get_search_engines()
    
    for engine in search_engines:
        for criteria in settings.SEARCH_CRITERIA:
            data = engine.search(criteria)
            if data:
                gs.insert_cell(1, settings.SEARCH_CRITERIA.index(criteria) + 1, " ".join(criteria), search_engines.index(engine) + 1)
                gs.insert_data(settings.SEARCH_CRITERIA.index(criteria) + 1, data, search_engines.index(engine) + 1)
            else:
                print "Empty pubs"


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
