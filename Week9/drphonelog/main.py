#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
import cgi
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from google.appengine.ext import db
import datetime

class Post(db.Model):
	ninja = db.UserProperty()
	duration = db.TimeProperty()
	date = db.DateTimeProperty(auto_now_add=True)
	comment = db.StringProperty(multiline=False)
	appName = db.StringProperty()

class PostHandler(webapp.RequestHandler):
	def post(self):
		durationsomething = datetime.time(hour = 0, minute = int(self.request.get('duration')), second = 0, microsecond = 0)
		post = Post()
		if users.get_current_user():
			post.ninja = users.get_current_user()
		self.response.out.write("Thanks!")
		# post.duration = datetime.time((0, int(self.request.get('duration')), 0, 0))
		post.duration = durationsomething
		post.appName = self.request.get('appName')
		post.comment = self.request.get('comment')
		post.date = datetime.datetime.now()
		post.put()
		self.redirect('/') #This will take us back to the Index
		

class ChartHandler(webapp.RequestHandler):
	def get(self):
		postStuff = db.GqlQuery("SELECT * from Post order by date")	
		postCount = postStuff.count() #counts the number of returned items
		self.response.out.write('<html><head><script type="text/javascript" src="http://www.google.com/jsapi"></script><link rel="stylesheet" type="text/css" href="/stylesheets/style.css" /></head>')
		# for call in postStuff:
		# 	pass
		def putUsersinDic(postStuff):
			userDic = dict()
			for call in postStuff:
				userDic[call.ninja] = userDic.get(call.ninja, 0) + 1
			return userDic
		q = 0
		userDictionary = putUsersinDic(postStuff)
		print userDictionary
		for item in userDictionary:
			q += 1

		self.response.out.write(("""
			<script type="text/javascript">google.load("visualization", "1", {packages:["piechart"]});\
				google.setOnLoadCallback(drawChart);
					function drawChart() {
						var data = new google.visualization.DataTable();
						data.addColumn('string', 'App');
						data.addColumn('number', '# of Calls');
						data.addRows(%d);""") % (q))
		i = 0
		for ninja in userDictionary:
			self.response.out.write(('data.setValue(%d, 0, \'%s\');') % (i, ninja))
			self.response.out.write('\r\n')
			self.response.out.write(('data.setValue(%d, 1, %d);') % (i, userDictionary[ninja]))
			self.response.out.write('\r\n')
			i += 1
		self.response.out.write("""
var chart2 = new google.visualization.PieChart(document.getElementById('chart_div2'));
chart2.draw(data, {width: 600, height: 480, is3D: true, legend: 'label', title: 'Per Ninja'});
}
</script>""")
		self.response.out.write('<body><h1>Charts! (hopefully)</h1> <br /><div id="chart_div2"></div>')
		self.response.out.write("</body></html>")
		

class Last5Handler(webapp.RequestHandler):
	def get(self):
		self.response.out.write('<html><head><link rel="stylesheet" type="text/css" href="/stylesheets/style.css" /></head>')
		self.response.out.write("<body><h1>Last Five Calls</h1>")
		self.response.out.write('<p>We\'re going in!</p>')
		self.response.out.write('<table width="500px"><th width="20%">User:</th><th width="33%">App</th><th width="47%">Notes</th>')
		lastfive = db.GqlQuery("SELECT * from Post order by date desc limit 5")
		for call in lastfive:
			self.response.out.write(('<tr><td>%s</td><td>%s</td><td>%s</td></tr><tr><td></td><td></td><td><span style="font-size:12px;">%s</span></td></tr>') % (call.ninja, call.appName, call.comment, call.date))
		self.response.out.write("</body></html>")

class MainHandler(webapp.RequestHandler):
    def get(self):
		self.response.out.write('<html><head><link rel="stylesheet" type="text/css" href="/stylesheets/style.css" /></head>')
		user = users.get_current_user()
		if user:
			# self.response.headers['Content-Type'] = 'text/plain'
			self.response.out.write(('<p>Hello, %s | <a href="%s">Sign Out</a></p>') % (user.nickname(), users.create_logout_url("/")))
		else:
			self.redirect(users.create_login_url(self.request.uri))
		self.response.out.write("<body><h1>Phone Log v2.0</h1><br />")
		self.response.out.write("<p>Update your stuff here</p>")
		self.response.out.write('<form action="/post" method="post">')
		self.response.out.write('Duration: <select name="duration" style="font-size:30px;">')
		for number in xrange(2,62,2):
				self.response.out.write(('<option value="%d">%d:00 minutes</option>') % (number, number))
		self.response.out.write("</select>")
		self.response.out.write("<br />")
		self.response.out.write("<br />")
		#Could simplify this even further by storing App names and values in a text file.
		self.response.out.write('App: <select name="appName" style="font-size:30px;"><option value="OmniFocus">OmniFocus</option>\
																				<option value="OmniFocus iPhone">OmniFocus/iPhone</option>\
																				<option value="OmniFocus iPad">OmniFocus/iPad</option>\
																				<option value="OmniPlan">OmniPlan</option>\
																				<option value="OmniGraffle">OmniGraffle</option>\
																				<option value="OmniGraffle iPad">OmniGraffle/iPad</option>\
																				<option value="OmniOutliner">OmniOutliner</option>\
																				<option value="OmniOutliner iPad">OmniOutliner/iPad</option>\
																				<option value="OmniDiskSweeper">OmniDiskSweeper</option>\
																				<option value="OmniDazzle">OmniDazzle</option>\
																				<option value="OmniGraphSketcher">OmniGraphSketcher</option>\
																				<option value="OmniGraphSketcher iPad">OmniGraphSketcher/iPad</option>\
																				<option value="Sales">Sales-related</option>\
																				<option value="OmniWeb">OmniWeb</option>\
																				</select>')
		self.response.out.write("<br />")
		self.response.out.write("<br />")
		
		self.response.out.write('<input name="comment" type="text" value="" />')
		self.response.out.write("<br />")
		
		self.response.out.write('<br /><input type="submit" style="font-size:30px; width:100px; height:50px;" value="Fin" /></form>')
		self.response.out.write('<div id="footer"><a href="/charts">Charts</a> | <a href="last5">Last 5</a></div>')
		self.response.out.write("</body></html>")


def main():
    application = webapp.WSGIApplication([('/', MainHandler), ('/charts', ChartHandler), ('/last5', Last5Handler), ('/post', PostHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
