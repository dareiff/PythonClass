import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')

print s.echo('hello')
print s.echo('world')
print s.time()
print s.add("4+5")
print s.google_utc_time()