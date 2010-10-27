import httplib
import urllib
import urllib2
import cookielib
import re

from BeautifulSoup import BeautifulSoup


class IEEEXploreSearch:
    def __init__(self):
        self.SEARCH_BASE_URL = "http://ieeexplore.ieee.org/search/searchresult.jsp"

    def search(self, terms, limit=10):
        params = urllib.urlencode({'queryText': " ".join(terms), 'pageNumber' : '1',
                                   'newsearch' : 'true'})
        url = self.SEARCH_BASE_URL + "?" + params
        headers = [( 'User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12' )]
        
        cj = cookielib.CookieJar()
        cj.clear()
        cj.clear_session_cookies()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = headers
        resp = opener.open(url)
        
        titles = []

        try:
            html = resp.read()
            results = []
            html = html.decode('ascii', 'ignore')
            print html
            # Screen-scrape the result to obtain the publication information
            soup = BeautifulSoup(html)

            #attrs = soup.findAll("div", { "class" : "detail" })
            attrs = soup.findAll("div", { 'class' : 'detail' })
            for attr in attrs:
                print attr
                if str(attr).find("/search/") != -1:
                    print attr
            '''
            for attr in attrs:
                temp = BeautifulSoup(str(attr))
                title = ""
                
                for item in temp.a.contents:
                    item = str(item).replace("<b>", "")
                    item = str(item).replace("</b>", "")
                    title = title + str(item)
                titles.append(title)

            return titles
            '''
        except urllib2.HTTPError:
            print "ERROR: ",
            print resp.status, resp.reason
            return []
