import httplib
import urllib
import urllib2
import cookielib
import re

from BeautifulSoup import BeautifulSoup


class IEEEXploreSearch:
    def __init__(self):
        self.SEARCH_BASE_URL = "http://ieeexplore.ieee.org/search/searchresult.jsp"

    def search(self, terms, num_results=10):
        titles = []
        count = 1
        
        while (count * 10) <= num_results:
            resp = self.get_response(terms, count)
            try:
                html = resp.read()
                html = html.decode('ascii', 'ignore')
                soup = BeautifulSoup(html)

                attrs = soup.findAll("div", { 'class' : 'detail' })
                titles = []
                for attr in attrs:
                    titles.append("".join(attr.a.findAll(text=True)))
                
            except urllib2.HTTPError:
                print "ERROR: ",
                print resp.status, resp.reason
                return []
            count = count + 1
        
        return titles
    
    def get_response(self, terms, page_number=1):
        params = urllib.urlencode({'queryText': " ".join(terms), 'pageNumber' :
                                   page_number,
                                   'rowsPerPage' : '10',
                                   'newsearch' : 'true'})
        url = self.SEARCH_BASE_URL + "?" + params
        headers = [( 'User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12' )]
        
        cj = cookielib.CookieJar()
        cj.clear()
        cj.clear_session_cookies()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = headers
        resp = opener.open(url)
        
        return resp

