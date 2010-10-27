import httplib
import urllib
import urllib2
import re

from BeautifulSoup import BeautifulSoup


class CiteSeerXSearch:
    def __init__(self):
        self.SEARCH_BASE_URL = "http://citeseerx.ist.psu.edu/search"

    def search(self, terms):
        params = urllib.urlencode({'q': "+".join(terms), 'submit' : 'Search',
                                    'sort' : 'rlv', })

        url = self.SEARCH_BASE_URL + "?" + params
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12' }
        request = urllib2.Request(url, None, headers)
        resp = urllib2.urlopen(request)
        
        titles = []

        try:
            html = resp.read()
            results = []
            html = html.decode('ascii', 'ignore')
                        
            # Screen-scrape the result to obtain the publication information
            BeautifulSoup.NESTABLE_TAGS['em'] = []
            soup = BeautifulSoup(html)
            
            attrs = soup.findAll("em", { "class" : 'title'})
            
            for attr in attrs:
                title = ''.join(attr.findAll(text=True))
                titles.append(title)

            return titles
        except urllib2.HTTPError:
            print "ERROR: ",
            print resp.status, resp.reason
            return []
