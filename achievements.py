from github2.client import Github

#achievement dictionary
achievements = {}

class Achievement(object, username, api_token):
	self.username = username
	self.api_token = api_token

def connect(self, username, api_token):
	return github = Github(username = username, api_token = api_token, requests_per_second=1)

def repoman(self, github):
	repo = github.repo.list()
	if len(repo) >= 10:
		repoman = {'repoman': true}
	else:
		repoman = {'repoman' : false}
	achievements.update(repoman)
def partyoffive(self,github):
	followers = github.users.followers(self.username)
	if len(followers) >= 5:
		partyoffive = {'partyoffive': true}
	else:
		partyoffive = {'partyoffive' : false}
	achievements.update(partyoffive)
def lemming(self, github):
	following = github.users.following(self.username)
	if len(following)>= 100:
		lemming = {'lemming': true}
	else:
		lemming = {'lemming' : false}
	achievements.update(lemmings)

	
	

