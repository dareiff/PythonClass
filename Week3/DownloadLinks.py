#I'm not at all done yet. Was in San Fran for Macworld this past week and have been just racked with stuff to do.

from BeautifulSoup import BeautifulSoup
import urllib2
from pprint import pprint
import html2text
import re

website = urllib2.urlopen("http://briandorsey.info/uwpython/Internet_Programming_in_Python.html")

#What we need to do:
# - Download Files from the Topics column in table
# - Download HTML (& save) from the Readings column in table

soup = BeautifulSoup(website)

print soup.html.head.title.string # Should use this, somehow, to print out the HREF name (Between the <a></a> tags)

print "There are " + str(len(soup('a'))) + " <a> tags"#So this tells us that we have 87 a tags

researchstring = "^*.pdf"

aTags = soup.findAll('a', href=re.compile("[^*].pdf"))

print dir(aTags)

for item in aTags:
	print item.string #Goal is to print out just the stuff, now.

# So that works. Just need to put an http://briandorsey.info/uwpython/ at the beginning of each href

