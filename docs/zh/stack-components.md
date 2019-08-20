# 参数

## 组件及路径

AWX部署包中不仅仅只有AWX本身，还包含一序列支持AWX运行所需的其他软件（这里称之为组件），下面列出主要组件名称、安装路径、配置文件地址等重要的信息：

### AWX

AWX: /var/lib/awx  
AWX Python package directory: /opt/awx  
AWX configuration file: /etc/awx/settings.py  
Ansible: /opt/awx/embedded/lib/python2.7/site-packages/ansible  

```python
TATIC_ROOT = '/opt/awx/static'
PROJECTS_ROOT = '/var/lib/awx/projects'
JOBOUTPUT_ROOT = '/var/lib/awx/job_status'
```

### Python
PHP Configuration File: _/etc/php.ini_  
PHP Modules Configuration Directory: _/etc/php.d_

### RabbitMQ

Installation directory: /var/lib/rabbitmq

### Apache


### PostgreSQL

MySQL Management URL: http://Internet IP:9090

### Redis
Redis configuration file: /etc/redis.conf  
Redis data directory: /var/lib/redis

## 端口号

下面是您在使用本镜像过程中，需要用到的端口号，请通过云控制台安全组进行设置

| 名称 | 端口号 | 用途 |  必要性 |
| --- | --- | --- | --- |
| MySQL | 3306 | 远程连接MySQL | 可选 |
| HTTP | 80 | 通过http访问Metabase | 必须 |
| HTTPS | 443 | 通过https访问Metabase | 可选 |
| phpMyAdmin on Docker | 9090 | 可视化管理MySQL | 可选 |

## 版本号

组件对应的基本版本号可以通过云市场商品页面查看，但部署到您的服务器之后，版本会有一定的升级，故更为精准的版本请通过在服务器上运行命令查看：

```shell
# Nginx version

# MySQL version

# Python version
```