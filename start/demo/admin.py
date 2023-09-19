import json
import time

from django.contrib import admin
from .models import GitHubUser, Repos


# admin.site.disable_action('delete_selected')

# Register your models here.

# @admin.action(permissions=['change'])

def fetch_user_avatar(ModelAdmin, request, queryset):
    # queryset
    authentication_info = []
    for user in queryset.all():
        pass


# 手动获取城市信息
fetch_user_avatar.short_description = "手动获取头像"


class GitHubUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'login', 'avatar_url']
    search_fields = ('login',)
    # actions = []


class ReposAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name']
    search_fields = ('name',)
    # actions = []


admin.site.register(GitHubUser, GitHubUserAdmin)
admin.site.register(Repos, ReposAdmin)
