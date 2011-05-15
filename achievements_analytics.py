#!/usr/bin/python

"""
achievements_analytics.py

Created by Mahdi Yusuf on 2011-03-06.

"""

from github2.client import Github
import sys, re
from django.utils import simplejson
from achievements.models import Achievement, ProloggerUser
from datetime import datetime

#Helper functions
def string_found(string1, string2):
    if re.search(r"\b" + re.escape(string1) + r"\b", string2):
        return True
    return False
def uniqify(seq):  
    # order preserving 
    checked = [] 
    for e in seq: 
        if e not in checked: 
            checked.append(e) 
    return checked

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

    def languages(self):
        languages = []
        repos = self.client.repos.list(self.username)
        for repo in repos:
            print repo.language
            languages.append(str(repo.language))
        print uniqify(languages)
        if "Python" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Snakes!?, Why Did It Have To Be Snakes!')
        if "C" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('C')
        if "CoffeeScript" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Coffee Time')
        if "C++" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('C++')
        if "Haskell" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Haskell')
        if "Ruby" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Ruby')
        if "VimL" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Vimproved')
        if "Java" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Bean Beans the Magical Fruit')
        if "Shell" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Koopa')
        if "PHP" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('PH Level Is Rising!')
        if "Perl" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Camel Toe')
        if "JavaScript" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('JavaScript')
        if "ActionScript" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('LIGHTS, CAMERA, ACTION!')
        if "Ada" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Ada')
        if "ASP" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('ASP')
        if "Assembly" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Assembly')
        if "Boo" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Boo')
        if "C#" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('C#')
        if "Clojure" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Clojure')
        if "ColdFusion" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('ColdFusion')
        if "ooc" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('ooc')
        if "Common Lisp" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Common Lisp')
        if "D" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('D')
        if "Dylan" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Dylan')
        if "Eiffel" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Eiffel')
        if "Erlang" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Erlang')
        if "F#" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('F#')
        if "Go" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Go')
        if "Groovy" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Groovy')
        if "Io" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Io')
        if "Mirah" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Mirah')
        if "HaXe" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('HaXe')
        if "OCaml" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('OCaml')
        if "Nu" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Nu')
        if "Pure Data" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Pure Data')
        if "SuperCollider" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('SuperCollider')
        if "Tcl" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Tcl Me Elmo')
        if "Visual Basic" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Short Bus')
        if "Factor" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Factor')
        if "VHDL" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('VHDL')
        if "Racket" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Racket')
        if "Vala" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Vala')
        if "Lua" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Lua')
        if "sclang" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('sclang')
        if "Racket" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Racket')
        if "Self" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Self')
        if "Smalltalk" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('Smalltalk')
        if "R" in languages:
            prolog = self.prologger_user
            prolog.add_achievement('R')
            
    def repoman(self):
        repo = self.client.repos.list(self.username)
        repoman1 = {'repoman': False}
        if len(repo) >= 10:
            repoman1 = {'repoman': True}
            prolog = self.prologger_user
            prolog.add_achievement('Repoman')
        self.achievements.update(repoman1)

    def party_of_five(self):
        user = self.client.users.show(self.username)
        if user.followers_count >= 5:
            partyoffive = {'partyoffive': True}
            prolog = self.prologger_user
            prolog.add_achievement('Party Of Five')
        else:
            partyoffive = {'partyoffive': False}
        self.achievements.update(partyoffive)

    def lemming(self):
        user = self.client.users.show(self.username)
        if user.following_count >= 100:
            lemming = {'lemming': True}
            prolog = self.prologger_user
            prolog.add_achievement('Lemming')
        else:
            lemming = {'lemming': False}
        self.achievements.update(lemming)

    def forker(self):
        repos = self.client.repos.list(self.username)
        forker = {'forker': False}
        for repo in repos:
            if repo.fork:
                forker = {'forker': True}
                prolog = self.prologger_user
                prolog.add_achievement('You Forker')
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
                prolog = self.prologger_user
                prolog.add_achievement('99 Problems')
                break
            else:
                continue
        self.achievements.update(problems)

    def likeaboss(self):
        user = self.client.users.show(self.username)
        public_repos = user.owned_private_repo_count
        if public_repos > 0:
            likeaboss = {'likeaboss': True}
            prolog = self.prologger_user
            prolog.add_achievement('Like A Boss')
        else:
            likeaboss = {'likeaboss': False}
        self.achievements.update(likeaboss)

    def wiki(self):
        repos = self.client.repos.list(self.username)
        wiki = {'wiki': False}
        for repo in repos:
            if repo.has_wiki:
                wiki = {'wiki': True}
                prolog = self.prologger_user
                prolog.add_achievement('WIKI WIKI YEAH')
                break
            else:
                continue
        self.achievements.update(wiki)

    def microsoft(self):
        user = self.client.users.show(self.username)
        private_repos = user.total_private_repo_count
        if private_repos > 0:
            microsoft = {'microsoft': True}
            prolog = self.prologger_user
            prolog.add_achievement('Microsoft')
        else:
            microsoft = {'microsoft': False}
        self.achievements.update(microsoft)

    def linus(self):
        user = self.client.users.show(self.username)
        public_repos = user.public_repo_count
        if public_repos > 0:
            linus = {'linus': True}
            prolog = self.prologger_user
            prolog.add_achievement('Linus')
        else:
            linus = {'linus': False}
        self.achievements.update(linus)

    def pushable(self):
        pushable = self.client.repos.pushable()
        if len(pushable) > 0:
            pushable = {'pushable': True}
            prolog = self.prologger_user
            prolog.add_achievement('Get That Pandemic')
        else:
            pushable = {'pushable': False}

    def kickingit(self):
        pass

    def wearefamily(self):
        user = self.client.users.show(self.username)
        collabs = user.collaborators
        if collabs > 0:
            wearefamily = {'wearefamily': True}
            prolog = self.prologger_user
            prolog.add_achievement('We Are Family')
        else:
            wearefamily = {'wearefamily': False}
        self.achievements.update(wearefamily)

    def megarepo(self):
        megarepo = {'megarepo': False}
        user = self.client.users.show(self.username)
        if user.disk_usage > 1048576:
            megarepo = {'megarepo': True}
            prolog = self.prologger_user
            prolog.add_achievement('Mega Repository')
        self.achievements.update(megarepo)
    
    def priv_gist(self):
        private_gist  = {'public_gist': False}
        user = self.client.users.show(self.username)
        gist = user.private_gist_count
        if (gist>0):
            private_gist = {'private_gist': True}
            prolog = self.prologger_user
            prolog.add_achievement('Love Letter')
        self.achievements.update(private_gist)

    def pub_gist(self):
        public_gist  = {'public_gist': False}
        user = self.client.users.show(self.username)
        gist = user.public_gist_count
        if (gist>0):
            prolog = self.prologger_user
            prolog.add_achievement('Task List')
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
            if project == 'kennethreitz/osxpython.org' or project == 'kennethreitz/readthedocs.org' or project == 'kennethreitz/vapor.js' :
                continue
            commits += github.commits.list(project)
            for commit in commits:
                for word in words:
                    if string_found(word, commit.message) and commit.author['login'] == self.username:
                        pottymouth = {'pottymouth': True}
                        prolog = self.prologger_user
                        prolog.add_achievement('Pardon My French')
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
                prolog = self.prologger_user
                prolog.add_achievement('Google Me, Bitch.')
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
                prolog = self.prologger_user
                prolog.add_achievement('Google Me, Bitch.')
                break
            else:
                continue
        self.achievements.update(download)

    def get_achievements(self):
        print "Getting Achievements..\n"
        checks = ['pottymouth','repoman', 'likeaboss', 'microsoft', 'linus', 'wiki', 'wearefamily', 'megarepo',
                  'pushable', 'problems', 'forker', 'lemming', 'party_of_five', 'homepage_homie', 'just_download','necromancer', 'priv_gist', 'pub_gist', 'megarepo', 'languages']
        for check in checks:
            getattr(self, check)()
        return self.achievements


if __name__ == '__main__':
    exit(main())

        
    



        
    
    
    

    
    

