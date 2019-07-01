from bs4 import BeautifulSoup
import urllib2

resp = urllib2.urlopen("https://apod.nasa.gov/apod/ap170430.html")
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))

for link in soup.find_all('a', href=True):
    print link['href']
