import httplib
import urllib
import urllib2
import re

from BeautifulSoup import BeautifulSoup


class GoogleScholarSearch:
    def __init__(self):
        self.SEARCH_BASE_URL = "http://scholar.google.com/scholar"

    def search(self, terms, num_results=10):
        titles = []
        count = 0
        
        if num_results:
            while count < num_results:
                resp = self._get_response(terms, count)
                titles.extend(self._scrape(resp))
                count = count + 10
        else:
            resp = self._get_response(terms, count)
            titles.extend(self._scrape(resp))
            count = count + 10
            while not self._stop_search(terms, titles):
                resp = self._get_response(terms, count)
                titles.extend(self._scrape(resp))
                count = count + 10
                print count

        return titles
    
    
    def _stop_search(self, terms, titles):
        for i in range(len(titles) - 10, len(titles)):
            if self._has_criteria(terms, titles[i]):
                return False

        return True


    def _has_criteria(self, terms, entry):
        for term in terms:
            if entry.find(term) == -1:
                return False

        return True
    
    
    def _get_response(self, terms, start):
        params = urllib.urlencode({'q': "+".join(terms), 'start': start, 
                                    'hl' : 'en',
                                    'btnG' : 'Search', 'as_sdt' : '40000000000',
                                    'as_vis' : '1' })
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
            
            attrs = soup.findAll("div", { "class" : "gs_rt"})
            for attr in attrs:
                temp = BeautifulSoup(str(attr))
                title = ""
                
                for item in temp.a.contents:
                    item = str(item).replace("<b>", "")
                    item = str(item).replace("</b>", "")
                    title = title + str(item)
                titles.append(title)

        except urllib2.HTTPError:
            print "ERROR: ",
            print resp.status, resp.reason
            return []
        
        return titles
