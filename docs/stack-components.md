# Parameters

## Components and directory

The AWX deployment package includes not only AWX itself, but also a series of other software (herein referred to as components) required to support AWX operation. The important information such as the main component name, installation path, and configuration file address are listed below:

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

### PostgreSQL

PostgreSQL Management URL: http://Internet IP:9090

### Redis
Redis configuration file: /etc/redis.conf  
Redis data directory: /var/lib/redis

## Ports

The following is the port number you need to use during the process of using this image. Please set it through the cloud console security group.

| Name | Port | Use |  Necessity |
| --- | --- | --- | --- |
| MySQL | 3306 | Remote connect MySQL | Optional |
| HTTP | 80 | Use HTTP to visit AWX | Must |
| HTTPS | 443 | Use HTTPS to visit AWX | Optional |
| phpPgAdmin on Docker | 9090 | Web-GUI for Postgresql | Optional |

## Version

The basic version number corresponding to the component can be viewed through the product page on Cloud platform, but after deployment to your server, the version will be upgraded. Therefore, the more accurate version can be viewed by running the command on the server:

```shell
# Nginx version

# MySQL version

# Python version
```