from github2.client import Github
import sys, os

"""
Takes the usernamd and api_token from the command line,
and then asks the user if it wants to take _every_ repo,
or download on a True/False basis.
"""

if len(sys.argv) > 2:
	USER = sys.argv[1]
	APITOKEN = sys.argv[2]
else:
	print "\n************************"
	print """USAGE:\n checkoutNewMachine.py username api_token\n"""
	print "I'd like to add capabilities to go for EVERYTHING"
	print "Or to go case-by-case. It's not here yet."
	print "************************\n"
	sys.exit(1)


github = Github(username=USER, api_token=APITOKEN)

listOfRepos = github.repos.list(USER)

def caseByCase():
	for repo in listOfRepos:
		print "Clone %s?\n(True/False)" % repo.name
		b = input("\n>")
		if b:
			os.system("git clone %s.git" % repo.url)
			print "Finished with %s\n\n" % repo.name
		else:
			print "\n\n"


if __name__ == '__main__':
	caseByCase()