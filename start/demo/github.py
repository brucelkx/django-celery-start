import copy
import datetime
import logging
import time
import requests
from dateutil.parser import parse
from django.core.cache import cache
from django.db import transaction
import json
from .models import GitHubUser, Repos


class GitHub():
    def __init__(self):
        self.http_user_url = "https://api.github.com/users"
        self.http_user_repos_url = "https://api.github.com/users/{login}/repos"

    def get_user_list(self):

        res = requests.get(self.http_user_url)
        if res.status_code == 200:
            user_list = res.json()
            for user in user_list:
                GitHubUser.objects.update_or_create(defaults={"avatar_url": user["avatar_url"]}, login=user["login"])

    def get_user_repo_list(self):
        users = GitHubUser.objects.all()
        for user in users:
            res = requests.get(self.http_user_repos_url.format(login=user.login))
            if res.status_code == 200:
                repo_list = res.json()
                for repo in repo_list:
                    Repos.objects.update_or_create(defaults={"name": repo["name"]}, user=user)
