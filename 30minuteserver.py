import os, socket, sys, datetime, subprocess, pprint

defaults = ['127.0.0.1', '8080']
mime_types = {'.jpg' : 'image/jpg',
			 '.gif' : 'image/gif',
			 '.png' : 'image/png',
			 '.html' : 'text/html',
			 '.pdf' : 'application/pdf',
			 '.py' : 'text/html'}
response = {}

response[200] =\
"""HTTP/1.0 200 Okay
Server: ws30
Content-type: %s

%s
"""

response[301] =\
"""HTTP/1.0 301 Moved
Server: ws30
Content-type: text/plain
Location: %s

moved
"""

response[404] =\
"""HTTP/1.0 404 Not Found
Server: ws30
Content-type: text/plain

%s not found
"""

DIRECTORY_LISTING =\
"""<html>
<head><title>%s</title></head>
<body>
<a href="%s..">..</a><br>
%s
</body>
</html>
"""

EXECUTE_PYTHON =\
"""<html>
<head><title>%s</title></head>
<body>
<p>%s ran successfully.</p>
<p>The results:</p>
<blockquote>%s</blockquote>
</body>
</html>
"""

DIRECTORY_LINE = '<a href="%s">%s</a><br>'

def server_socket(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(1)
	return s

def listen(s):
	connection, client = s.accept()
	return connection.makefile('r+')

def get_request(stream):
	method = None
	while True:
		line = stream.readline()
		print line
		if not line.strip():
			break
		elif not method:
			method, uri, protocol = line.split()
	return uri

def list_directory(uri):
	entries = os.listdir('.' + uri)
	entries.sort()
	return DIRECTORY_LISTING % (uri, uri, '\n'.join(
		[DIRECTORY_LINE % (e, e) for e in entries]))

def send_time(uri):
	return datetime.datetime.now()

def get_file(path, uri):
	if path.endswith('.py'):
		return execute_python_script(path, uri)
	elif path.endswith('/time'):
	    return send_time(uri)
	else:
		f = open(path)
		try:
			return f.read()
		finally:
			f.close()
		
def execute_python_script(path, uri):
    # os.system('python %s' % path)
    # Need to switch to the subprocess module
    process = subprocess.Popen(['python', path], stdout=subprocess.PIPE)
    process.wait()
    return EXECUTE_PYTHON % (path, uri, process.stdout.read())

def get_content(uri):
	print 'fetching:', uri
	try:
		path = '.' + uri
		if os.path.isfile(path):
			return (200, get_mime(uri), get_file(path, uri))
		if os.path.isdir(path):
			if(uri.endswith('/')):
				return (200, 'text/html', list_directory(uri))
            # elif(uri.endswith('time')):
            #   return (200, 'text/html', send_time(uri))
            # elif(uri.endswith('.py')):
            #   return (200, 'text/html', execute_python_script(uri))
			else:
				return (301, uri + '/')
		else: return (404, uri)
	except IOError, e:
		return (404, e)

def get_mime(uri):
	return mime_types.get(os.path.splitext(uri)[1], 'text/plain')

def send_response(stream, content):
	stream.write(response[content[0]] % content[1:])

if __name__ == '__main__':
	args, nargs = sys.argv[1:], len(sys.argv) - 1
	host, port = (args + defaults[-2 + nargs:])[0:2]
	server = server_socket(host, int(port))
	print 'starting %s on %s...' % (host, port)
	try:
		while True:
			stream = listen (server)
			send_response(stream, get_content(get_request(stream)))
			stream.close()
	except KeyboardInterrupt:
		print 'shutting down...'
	server.close()