import os
from celery import Celery

celery_settings = 'start.settings.dev'
START_ENV_TYPE = os.environ.get("START_ENV_TYPE")
if START_ENV_TYPE == "staging":
    celery_settings = 'start.settings.staging'
elif START_ENV_TYPE == "product":
    celery_settings = 'start.settings.product'
# 设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', celery_settings)

# 实例化
demo_task = Celery('demo_task')
# namespace=CELERY作用是允许你在Django配置文件中对Celery进行配置
# 但所有Celery配置项必须以CELERY开头，防止冲突
demo_task.config_from_object(celery_settings, namespace='CELERY')

# 自动从Django的已注册app中发现任务
demo_task.autodiscover_tasks()
demo_job = Celery('demo_job')
demo_job.config_from_object(celery_settings, namespace='CELERY')
