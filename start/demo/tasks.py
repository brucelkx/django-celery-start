from celery import Celery, shared_task, Task, chain
from .envsetup import demo_task
from .github import GitHub
from .models import GitHubUser

# # 设置环境变量
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms.settings')
# django.setup()
# # 实例化
# cms_task = Celery('cms_task')
#
# # namespace='CELERY'作用是允许你在Django配置文件中对Celery进行配置
# # 但所有Celery配置项必须以CELERY开头，防止冲突
# cms_task.config_from_object('django.conf:settings', namespace='CELERY')
#
# # 自动从Django的已注册app中发现任务
# cms_task.autodiscover_tasks()

retry_policy = {
    'max_retries': 3,
    'interval_start': 0,
    'interval_step': 0.2,
    'interval_max': 0.2,
    'retry_errors': None,
}

MAX_TRY_TIME = 1


@demo_task.task(bind=True, max_retrie=MAX_TRY_TIME)
def hello(self):
    print(f'hellohellohellohello!!!!!')


@demo_task.task(bind=True, max_retrie=MAX_TRY_TIME)
def fetch_github_user_list(self):
    u = GitHub()
    u.get_user_list()


@demo_task.task(bind=True, max_retrie=MAX_TRY_TIME)
def fetch_github_user_repos(self):
    u = GitHub()
    u.get_user_repo_list()


@demo_task.task(bind=True, max_retrie=MAX_TRY_TIME)
def chain_fetch_github_user_info(self):
    chain(fetch_github_user_list.s(), fetch_github_user_repos.s()).get()
