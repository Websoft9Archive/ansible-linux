#!/usr/bin/python env
#coding: utf-8
import os, sys, platform
import functions as ft

application = "redis"
url = "https://github.com/Websoft9/ansible-redis.git"

if os.getuid() != 0:
    print ("This program must be run as root. Aborting.")
    sys.exit(1)

# 确认是否安装ansible
a = input("Are you sure install ansible?[yes/no] ")
while a != ('y' or 'yes' or 'n' or 'no'):
    print('Input error, please input "y"/"yes" or "n"/"no"')
    a = input("Are you sure install ansible?[yes/no] ")
# 确认在本地还是远端安装
b = input("Do you want install this application on local server or remote server?[local/remote]")
while b != ('local' or 'remote'):
    print('Input error, please input "local" or "remote".')
    b = input("Do you want install this application on local server or remote server?[local/remote]")

# 判断系统发行版本,支持CentOS和Ubuntu
distribution = platform.dist()[0]
# 安装ansible
ft.install_ansible(a, distribution)
# 脚本存放路径
directory = "/tmp/ansible"
# 下载ansible仓库
ft.download(url, directory)

#切换到/tmp/ansible目录
os.chdir(directory)
# 创建hosts文件
hosts_file = '/tmp/ansible/hosts'

if b == "local":
    ft.wirte_file_local(hosts_file)
    os.system('ansible-playbook -i hosts ' + application + '.yml -c local')
elif b == "remote":
    ip = input("Please input your remote server's public IP: ")
    username = input("Please input your remote server's username: ")
    password = input("Please input your remote srever's password: ")
    ft.write_file_remote(hosts_file, ip , username, password)
    os.system('ansible-playbook -i hosts ' + application + '.yml ')

