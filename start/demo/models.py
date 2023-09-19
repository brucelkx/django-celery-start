import datetime

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.forms.models import model_to_dict


# Create your models here.

# 省市信息
class GitHubUser(models.Model):
    login = models.CharField(max_length=100, verbose_name="用户名")
    avatar_url = models.CharField(max_length=100, verbose_name="头像")

    class Meta:
        verbose_name = "GitHub用户信息"
        verbose_name_plural = 'GitHub用户信息'


class Repos(models.Model):
    user = models.ForeignKey(GitHubUser, related_name="repos", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="仓库名称")

    class Meta:
        verbose_name = "用户Repos"
        verbose_name_plural = '用户Repos'