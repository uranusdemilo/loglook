import urllib
from HTMLParser import HTMLParser

class Mstripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
def strip_tags(html):
    s = Mstripper()
    s.feed(html)
    return s.get_data()
        
baseurl = 'http://www.abuseipdb.com/check/'
ipaddr = '148.251.143.82'
pageurl = baseurl + ipaddr
#print pageurl
#ippage = urllib.urlopen(pageurl)
#ip_line = 'preload'
siteSource = open('siteoutput.htm', 'r')
ipLine = 'preload'
while ipLine:
   ipLine = siteSource.readline()
#	ipLine = ippage.readline()
   if "ISP:" in ipLine:
      ipLine = siteSource.readline()
      taggedISP = strip_tags(ipLine.strip())
   elif "Host Name:" in ipLine:
      ipLine = siteSource.readline()
      taggedHostName = strip_tags(ipLine.strip())
   elif "Organization:" in ipLine:
      ipLine = siteSource.readline()
      taggedOrganization = strip_tags(ipLine.strip())
   elif "Country:" in ipLine:
      ipLine = siteSource.readline()
      taggedCountry = strip_tags(ipLine.strip())
   elif "City:" in ipLine:
      ipLine = siteSource.readline()
      taggedCity = strip_tags(ipLine.strip())
   else:
      continue

print taggedISP + '-'
print taggedHostName + '-'
print taggedOrganization + '-'
print taggedCountry + '-'
print taggedCity
