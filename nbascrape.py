import urllib.request
from stools import *
from bs4 import BeautifulSoup
from Team import *

data = Data()
base_url = "http://www.basketball-reference.com/leagues/NBA_{0}.html"

y, num = 2016, 1
for year in range (y, y + num):
    link = base_url.format(year)
    source_code = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(source_code, "html.parser")
    data[year] = year_results(soup)