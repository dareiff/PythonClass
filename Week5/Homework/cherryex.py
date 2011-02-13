import cherrypy

class SomethingOrOther:
	def index(self):
		return "Other page"
	index.exposed = True

class HelloWorld:
	something = SomethingOrOther()
	def index(self):
		return """<html><head><title>Hello, World!</title></head><body><h1>Hello, World!</h1></body></html>"""
	index.exposed = True


cherrypy.quickstart(HelloWorld())
