import urllib2
# import sys

# briandorsey = urllib2.urlopen("http://briandorsey.info")

theTextFile = open('/tmp/DownloadTHESE.txt', 'r')
listofsites = theTextFile.readlines()
i = 0

for line in listofsites:
	print line
	a = open(('/tmp/%s.txt' % (i)), 'w')
	something = urllib2.urlopen(line)
	contents = something.read()
	a.write(contents)
	a.close()
	i += 1

print "All done"