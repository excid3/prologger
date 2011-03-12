#!/usr/bin/python

"""

@author Mahdi Yusuf
@website www.mahdiyusuf.com

"""

from github2.client import Github
import sys, re
from django.utils import simplejson



def string_found(string1, string2):
	   if re.search(r"\b" + re.escape(string1) + r"\b", string2):
		  return True
	   return False

#cmdline testing 
def main():
	username = sys.argv[1]
	api_token = sys.argv[2]
	ach	= Achievements1(username, api_token)
	points = ach.get_achievements()
	print "You have unlocked the following achievements! Congratulations!!"
	print simplejson.dumps(points)

class Achievements1(object):

	#achievement dictionary
	achievements = {}

	# initializing the the achievements class
	def __init__(self, username, api_token):
		self.username = username
		self.api_token = api_token
		self.client = Github(self.username, self.api_token, requests_per_second=1)
		self.achievements = {}

	def repoman(self):
		repo = self.client.repos.list()
		if len(repo) >= 10:
			repoman = {'repoman': True}
		else:
			repoman = {'repoman' : False}
		self.achievements.update(repoman)
	
	def party_of_five(self):
		user = self.client.users.show(self.username)
		if user.followers_count >= 5:
			partyoffive = {'partyoffive': True}
		else:
			partyoffive = {'partyoffive' : False}
		self.achievements.update(partyoffive)
	
	def lemming(self):
		user = self.client.users.show(self.username)
		if user.following_count >= 100:
			lemming = {'lemming': True}
		else:
			lemming = {'lemming' : False}
		self.achievements.update(lemming)
	
	def forker(self):
		repos = self.client.repos.list()
		forker = {'forker': False}
		for repo in repos:
			if repo.fork:
				forker = {'forker': True}
				break
			else:
				continue
		self.achievements.update(forker)
	
	def problems(self):
		repos = self.client.repos.list()
		problems = {'problems': False}
		for repo in repos:
			if repo.open_issues > 0:
				problems = {'problems': True}
				break
			else:
				continue
		self.achievements.update(problems)
	
	def likeaboss(self):
		user = self.client.users.show(self.username)
		public_repos = user.owned_private_repo_count
		if public_repos > 0 :	
			likeaboss = {'likeaboss': True}
		else:
			likeaboss = {'likeaboss': False}
		self.achievements.update(likeaboss)

	def wiki(self):
		repos = self.client.repos.list()
		wiki = {'wiki': False}
		for repo in repos:
			if repo.has_wiki:
				wiki = {'wiki': True}
				break
			else:
				continue
		self.achievements.update(wiki)
	
	def microsoft(self):
		user = self.client.users.show(self.username)
		private_repos = user.total_private_repo_count
		if private_repos > 0 :	
			microsoft = {'microsoft': True}
		else:
			microsoft = {'microsoft': False}
		self.achievements.update(microsoft)

	def linus(self):
		user = self.client.users.show(self.username)
		public_repos = user.public_repo_count
		if public_repos > 0 :	
			linus = {'linus': True}
		else:
			linus = {'linus': False}
		self.achievements.update(linus)
	
	def pushable(self):
		pushable = self.client.repos.pushable()
		if len(pushable)>0:
			pushable ={'pushable' : True}
		else:
			pushable ={'pushable' : False}
		
	def kickingit(self):
		pass
	
	def wearefamily(self):
		user = self.client.users.show(self.username)
		collabs = user.collaborators
		if collabs > 0:
			wearefamily = {'wearefamily': True}
		else:
			wearefamily = {'wearefamily': False}
		self.achievements.update(wearefamily)
		
	
	def megarepo(self):
		megarepo = {'megarepo': False}
		user = self.client.users.show(self.username)
		if user.disk_usage > 1048576:
			megarepo = {'megarepo': True}
		self.achievements.update(megarepo)
	
	def pottymouth(self):
		pottymouth = {'pottymouth': False}
		repos = self.client.repos.list()
		commits = []
		words = ['fuck', 'shit', 'piss', 'cunt', 'tits', 'motherfucker', 'cocksucker']
		for repo in repos:
			commits += self.client.commits.list(str(repo.project))
			for commit in commits:
				for word in words:
					if (string_found(word, str(commit.message)) and str(commit.author['login']) == self.username):
						pottymouth = {'pottymouth': True}
						break
					else:
						continue
		self.achievements.update(pottymouth)

	def get_achievements(self):
		print "Getting Achievements..\n"
		self.pottymouth()
		self.repoman()
		self.likeaboss()
		self.microsoft()
		self.linus()
		self.wiki()
		self.wearefamily()
		self.megarepo()
		self.pushable()
		self.problems()
		self.forker()
		self.lemming()
		self.party_of_five()
		return self.achievements
	
	
if __name__ == '__main__':
	exit(main())


		
	



		
	
	
	

	
	

