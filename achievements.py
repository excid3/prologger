from github2.client import Github



class Achievements(object):

	#achievement dictionary
	_achievements = {}

# initializing the the achievements class
def __init__(self, username, api_token):
	self.username = username
	self.api_token = api_token
	self.client = Github(self.username, self.api_token, requests_per_second=1)
	
def repoman(self):
	repo = self.client.repo.list()
	if len(repo) >= 10:
		repoman = {'repoman': True}
	else:
		repoman = {'repoman' : False}
	achievements.update(repoman)
	
def party_of_five(self):
	followers = self.client.users.followers(self.username)
	if len(followers) >= 5:
		partyoffive = {'partyoffive': True}
	else:
		partyoffive = {'partyoffive' : False}
	achievements.update(partyoffive)
	
def lemming(self):
	following = self.client.users.following(self.username)
	if len(following)>= 100:
		lemming = {'lemming': True}
	else:
		lemming = {'lemming' : False}
	achievements.update(lemmings)
	
def forker(self):
	repos = self.client.repo.list()
	forker = {'forker': False}
	for repo in repos:
		if repo.fork:
			forker = {'forker': True}
			break
		else:
			continue
	achievements.update(forker)
def problems(self):
	repos = self.client.repo.list()
	problems = {'problems': False}
	for repo in repos:
		if repo.open_issue > 0:
			problems = {'problems': True}
			break
		else:
			continue
	achievements.update(problems)
def likeaboss(self):
	repos = self.client.repo.list()
	likeaboss = {'likeaboss': False}
	for repo in repos:
		if repo.owner == self.username:
			likeaboss = {'likeaboss': True}
			break
		else:
		continue
	achievements.update(likeaboss)
def wiki(self):
	repos = self.client.repo.list()
	wiki = {'wiki': False}
	for repo in repos:
		if repo.has_wiki:
			wiki = {'wiki': True}
			break
		else:
		continue
	achievements.update(wiki)
def microsoft(self):
	repos = self.client.repo.list()
	microsoft = {'microsoft': False}
	for repo in repos:
		if repo.private:
			microsoft = {'microsoft': True}
			break
		else:
		continue
	achievements.update(microsoft)
def linus(self):
	repos = self.client.repo.list()
	linus = {'linus': False}
	for repo in repos:
		if not repo.private:
			linus = {'linus': True}
			break
		else:
		continue
	achievements.update(linus)
	
def pushable(self):
	pushable = self.client.repos.pushable()
	if len(pushable)>0:
		pushable ={'pushable' : True}
	else:
		pushable ={'pushable' : False}
def kickingit(self):
	pass
def wearefamily(self):
	collabs = self.client.repos.list_collaborators()
	

		
	



		
	
	
	

	
	

