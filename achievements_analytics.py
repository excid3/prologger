#!/usr/bin/python

"""
achievements_analytics.py

Created by Mahdi Yusuf on 2011-03-06.

"""

from github2.client import Github
import sys, re
from django.utils import simplejson
from achievements.models import Achievements, ProloggerUser
from datetime import datetime


def string_found(string1, string2):
    if re.search(r"\b" + re.escape(string1) + r"\b", string2):
        return True
    return False

#cmdline testing 
def main():
    username = sys.argv[1]
    api_token = sys.argv[2]
    ach = AchievementsAnalytics(username, api_token)
    points = ach.get_achievements()
    print "You have unlocked the following achievements! Congratulations!!"
    print simplejson.dumps(points)

class AchievementsAnalytics(object):
    #achievement dictionary
    achievements = {}

    # initializing the the achievements class
    def __init__(self, oauthtoken, prologger_user=None):
        self.oauthtoken = oauthtoken
        self.prologger_user = prologger_user
        self.username = str(prologger_user.user)
        self.client = Github(access_token=str(oauthtoken))
        self.achievements = {}

    def repoman(self):
        repo = self.client.repos.list(self.username)
        repoman = {'repoman': False}
        if len(repo) >= 10:
            repoman = {'repoman': True}
            repoman = Achievements.objects.create(name = "Repoman", date = datetime.now(), description = "Have more than 10 repositories on Github")
            self.prologger_user.achievements.add(repoman)
            self.prologger_user.save()
        self.achievements.update(repoman)

    def party_of_five(self):
        user = self.client.users.show(self.username)
        if user.followers_count >= 5:
            partyoffive = {'partyoffive': True}
        else:
            partyoffive = {'partyoffive': False}
        self.achievements.update(partyoffive)

    def lemming(self):
        user = self.client.users.show(self.username)
        if user.following_count >= 100:
            lemming = {'lemming': True}
        else:
            lemming = {'lemming': False}
        self.achievements.update(lemming)

    def forker(self):
        repos = self.client.repos.list(self.username)
        forker = {'forker': False}
        for repo in repos:
            if repo.fork:
                forker = {'forker': True}
                break
            else:
                continue
        self.achievements.update(forker)

    def problems(self):
        repos = self.client.repos.list(self.username)
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
        if public_repos > 0:
            likeaboss = {'likeaboss': True}
        else:
            likeaboss = {'likeaboss': False}
        self.achievements.update(likeaboss)

    def wiki(self):
        repos = self.client.repos.list(self.username)
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
        if private_repos > 0:
            microsoft = {'microsoft': True}
        else:
            microsoft = {'microsoft': False}
        self.achievements.update(microsoft)

    def linus(self):
        user = self.client.users.show(self.username)
        public_repos = user.public_repo_count
        if public_repos > 0:
            linus = {'linus': True}
        else:
            linus = {'linus': False}
        self.achievements.update(linus)

    def pushable(self):
        pushable = self.client.repos.pushable()
        if len(pushable) > 0:
            pushable = {'pushable': True}
        else:
            pushable = {'pushable': False}

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
    
    def priv_gist(self):
        private_gist  = {'public_gist': False}
        user = self.client.users.show(self.username)
        gist = user.private_gist_count
        if (gist>0):
            private_gist = {'private_gist': True}
        self.achievements.update(private_gist)

    def pub_gist(self):
        public_gist  = {'public_gist': False}
        user = self.client.users.show(self.username)
        gist = user.public_gist_count
        if (gist>0):
            public_gist = {'public_gist': True}
        self.achievements.update(public_gist)

    def pottymouth(self):
        pottymouth = {'pottymouth': False}
        github = Github(self.oauthtoken)
        repos = github.repos.list(self.username)
        commits = []
        words = ['fuck', 'shit', 'piss', 'cunt', 'tits', 'motherfucker', 'cocksucker']
        for repo in repos:
            project = repo.project
            commits += github.commits.list(project)
            for commit in commits:
                for word in words:
                    if string_found(word, unicode(commit.message)) and unicode(commit.author['login']) == self.username:
                        pottymouth = {'pottymouth': True}
                        break
                    else:
                        continue
        self.achievements.update(pottymouth)
    def top_commiter(self):
        "achievement if your the top commiter to a repo repo achievement"
        top_commiter = {'top_commiter': False}
        repos = self.client.repos.list(self.username)
        for repo in repos:
            pass

    def necromancer(self):
        "achievement if last push to this repository was over a year old repo achievement"
        necromancer = {'necromancer': False}
        repos = self.client.repos.list(self.username)
        for repo in repos:
            pass
            
    def homepage_homie(self):
        "achievement is homepage is set for one project or more repo achievement"
        homepage = {'homepage': False}
        repos = self.client.repos.list(self.username)
        for repo in repos:
            homepage = repo.homepage
            if (str(homepage) != ''):
                homepage = {'homepage': True}
                break
            else:
                continue
        self.achievements.update(homepage)
    def just_download(self):
        download = {'download': False}
        repos = self.client.repos.list(self.username)
        for repo in repos:
            has_downloads = repo.has_downloads
            if(has_downloads):
                download = {'download': True}
                break
            else:
                continue
        self.achievements.update(download)
		
	
		


    def get_achievements(self):
        print "Getting Achievements..\n"
        checks = ['pottymouth','repoman', 'likeaboss', 'microsoft', 'linus', 'wiki', 'wearefamily', 'megarepo',
                  'pushable', 'problems', 'forker', 'lemming', 'party_of_five', 'homepage_homie', 'just_download','necromancer', 'priv_gist', 'pub_gist']
        for check in checks:
            getattr(self, check)()
        return self.achievements


if __name__ == '__main__':
    exit(main())

        
    



        
    
    
    

    
    

