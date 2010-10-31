import httplib
import urllib
import urllib2
import cookielib
import re

from BeautifulSoup import BeautifulSoup


class IEEEXploreSearch:
    def __init__(self):
        self.SEARCH_BASE_URL = "http://ieeexplore.ieee.org/search/searchresult.jsp"

    def search(self, terms, count):
        resp = self._get_response(terms, count + 1)
        titles = self._scrape(resp)
        return titles


    def _get_response(self, terms, page_number=1):
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


    def _scrape(self, response):
        titles = []
        try:
            html = response.read()
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
    
        return titles
