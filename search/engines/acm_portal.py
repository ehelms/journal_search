import httplib
import urllib
import urllib2
import re

from BeautifulSoup import BeautifulSoup


class ACMPortalSearch:
    def __init__(self):
        self.SEARCH_BASE_URL = "http://portal.acm.org/results.cfm"

    def search(self, terms, count):
        if count < 10:
            resp = self._get_response(terms, count)
        else: 
            resp = self._get_response(terms, count + 10)
        titles = self._scrape(resp)
        return titles


    def _get_response(self, terms, start):
        params = urllib.urlencode({'query': "+".join(terms), 'start' : start + 1 })
        url = self.SEARCH_BASE_URL + "?" + params
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12' }
        request = urllib2.Request(url, None, headers)
        resp = urllib2.urlopen(request)
        return resp


    def _scrape(self, response):
        titles = []
        try:
            html = response.read()
            results = []
            html = html.decode('ascii', 'ignore')
                        
            # Screen-scrape the result to obtain the publication information
            soup = BeautifulSoup(html)
            
            attrs = soup.findAll("a", { "class" : "medium-text"})
            for attr in attrs:
                title = attr.contents[0]
                titles.append(title)
        except urllib2.HTTPError:
            print "ERROR: ",
            print resp.status, resp.reason
            return []

        return titles
