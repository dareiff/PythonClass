import bookdb, cherrypy, template, os

def test_list_books():
	books = bookdb.BookDB()
	titles = books.titles()
	assert len(titles) > 1
	# print titles
	returnString = ''
	for title in titles:
		returnString += "<p><a href=\"book/%s\">%s</a></p>" % (title['id'], title['title'])
		#Line above, we're building a string of HTML to return.
		#In each <p> tag, we're putting the dictionary value of 'title' in.
		assert 'title' in title
		assert 'id' in title
	return returnString

def test_get_book_info():
	books = bookdb.BookDB()
	titles = books.titles()
	id = titles[0]['id']
	print id
	info = books.title_info(id)
	print info
	assert 'title' in info
	assert info['title'] == titles[0]['title']
	assert 'publisher' in info
	assert 'isbn' in info
	assert 'author' in info

def get_book_info(id):
	books = bookdb.BookDB()
	title = books.title_info(id)
	assert len(title)
	returnString = template.template_detail()
	returnString += "<h3>" + title['title'] + "</h3>"
	returnString += "<div style=\"small\">by </div><h4>" + title['author'] + "</h4>"
	returnString += "<p>" + title['publisher'] + ", " + title['isbn'] + "</p>"
	returnString += template.template_detail_second()
	return returnString

class theIndex(object):
	def index(self):
		return test_list_books()
	index.exposed = True

	def book(self, id):
		# print "Only in the thing", self, id
		return get_book_info(id)
	book.exposed = True

	book = book
	
current_dir = os.path.dirname(os.path.abspath(__file__))
conf = {'/static': {'tools.staticdir.on': True,
                      'tools.staticdir.dir': os.path.join(current_dir, 'static'),
                      'tools.staticdir.content_types': {'rss': 'application/xml',
                                                        'atom': 'application/atom+xml'}}}

cherrypy.quickstart(theIndex(), '/', conf)