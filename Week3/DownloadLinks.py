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

def downloadPDFs():
	soup = BeautifulSoup(website)

	print soup.html.head.title.string # Should use this, somehow, to print out the HREF name (Between the <a></a> tags)

	print "There are " + str(len(soup('a'))) + " <a> tags"#So this tells us that we have 87 a tags

	researchstring = "^*.pdf"

	aTags = soup.findAll('a', href=re.compile("[^*].pdf"))

	s = []

	for item in aTags:
		# print item.string #Goal is to print out just the stuff, now.
		# print item
		something = str(item.attrs[0])
		something = something[12:-2]
		pdfDocument = "http://briandorsey.info/uwpython/" + something # OK, so I've stripped out the needless stuff
		pdfDocumentFile = urllib2.urlopen(pdfDocument)
		print "Downloading " + something
		if something.find("/") > 1:
			something = something.replace("/", "_")
			local_file = open("/tmp/pythonclass/" + something, "w")
			local_file.write(pdfDocumentFile.read())
			local_file.close()
	
		# s[item] = item.attrs[0]
		# print dir(item)

	# So, I've successfully scraped for all PDFs. Now I just need to follow all Documentation links that either in in "/" or ".html" and I'm good! I think.
	
downloadPDFs()