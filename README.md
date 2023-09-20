# django-celery-start
  a demo or sample of django + celery for beginner。一个简单使用django+celery的入门例子。
  - 本示例使用的是消息队列用的redis ，数据库用的mysql。
  - 要正常启动需要安装redis 和 mysql数据
### 如何添加任务
  - 添加周期任务
  ![](https://github.com/brucelkx/django-celery-start/blob/main/start/screenshot/01.png)
  ![](https://github.com/brucelkx/django-celery-start/blob/main/start/screenshot/02.png)
  ![](https://github.com/brucelkx/django-celery-start/blob/main/start/screenshot/03.png)

### Linux下测试，启动Celery
 - Celery -A demo.demo_task worker -l INFO
### Windows下测试，启动Celery
 - Celery -A demo.demo_task worker -l INFO -P eventlet

### 启动flower 监控celery broker
- celery --broker=redis://127.0.0.1:6379/0 flower
- 访问：http://127.0.0.1:5555/
#启动 beat Scheduler
- celery -A demo.demo_job beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

### 环境部署 linux centos 安装必要的依赖包：
- 安装supervisor
- 安装依赖包：
  - pip install -r requirements.txt 
- 注意：
  - uwsgi 通过pip 去安装
### RUN SYSTEM  
#### 用supervisor 来管理所有服务器的启动和关闭
- 本系统运行相关的服务：
  - nginx：接收处理http请求
  - uwsgi：运行管理django服务，对应的配置文件 uwsgi.ini
  - celery:定时任务服务，会启动worker 和 beat两个进程
  - supervisor：用于管理nginx、uwsgi、celery服务的开启和停止
- 配置文件：
  - 各种配置文件查看当前项目deploy目录 
  
  - 重点提示：
    - nginx 和 uwsgi 通过 socket 文件进行通讯的，所以要保证cms-master.pid 和 uwsgi.sock 读写权限；建议两个文件的目录给所有权限 
    - 如果出现cms-master.pid 和 uwsgi.sock 不会自动生成的情况，可以手动提前创建
    - 防止配置文件被更改，实际配置文件不会在git上进行维护，需要在生产环境上进行实际配置
- 注意：
  - supervisord 设置开机启动 
  - deploy目录提供测试环境运行的配置，需要根据实际情况调整
  - supervisor配置变动需要重新 sudo supervisorctl reload 或 update
- 运行命令：
  - 启动supervisord后台进程： sudo supervisord -c /etc/supervisord.conf
  - 关闭nginx、uwsgi、celery服务： sudo supervisorctl stop all
  - 启动nginx、uwsgi、celery服务：sudo supervisorctl start all 
 



