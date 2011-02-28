import sys
import urllib2
import re
from BeautifulSoup import BeautifulSoup


url = 'http://briandorsey.info/uwpython/Internet_Programming_in_Python.html'

# so we can pretend to be IE 6
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)'}

req = urllib2.Request(url)
response = urllib2.urlopen(req)
html = response.read()     #So far so good. Just spoofing as IE 6, downloading the page, and reading the response

#print html
soup = BeautifulSoup(html)


#Now we want to do something like read in the table, and look in the table header for "date"

firstRow = soup.table.tr.td
letsTrySecond = firstRow.child

print firstRow.text
print letsTrySecond

for incident in soup('td'):
    while(incident):
        print incident.nextSibling
        break





# def spelling_text(text):
#     text = text.lower()
#     if ('did you mean' in text or
#             'showing results for' in text):
#         return True
# 
# did_you_mean = soup.find(text=spelling_text)
# if did_you_mean:
#     div = did_you_mean.parent.parent
#     #print div
#     print div.i.text
# else:
#     print 'not found'
# 
