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

        while count < num_results:
            params = urllib.urlencode({'q': "+".join(terms), 'start': count, 
                                        'hl' : 'en',
                                        'btnG' : 'Search', 'as_sdt' : '40000000000',
                                        'as_vis' : '1' })
            url = self.SEARCH_BASE_URL + "?" + params
            headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12' }
            request = urllib2.Request(url, None, headers)
            resp = urllib2.urlopen(request)
            

            try:
                html = resp.read()
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
            count = count + 10

        return titles
