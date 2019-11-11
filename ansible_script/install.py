#!/usr/bin/python env
#coding: utf-8
import os
import sys
import platform
import functions as ft

application = "redis"
url = "https://github.com/Websoft9/ansible-redis.git"

if os.getuid() != 0:
    print ("This program must be run as root. Aborting.")
    sys.exit(1)

a = input("Are you sure install ansible?[y/n] ")
distrubition = platform.dist()[0] # 判断系统发行版本

# 下载ansible仓库
ft.download(url)

directory = "/tmp/ansible"
os.chdir(directory)  #切换到/tmp/ansible目录
# 创建hosts文件
hosts_file = '/tmp/ansible/hosts'

b = input("Do you want install this application on local server or remote server?[local/remote]")
while True:
    if b == "local":
        ft.wirte_file_local(hosts_file)
        os.system('ansible-playbook -i hosts ' + application + '.yml -c local')
    elif b == "remote":
        ip = input("Please input your remote server's public IP: ")
        username = input("Please input your remote server's username: ")
        password = input("Please input your remote srever's password: ")
        ft.write_file_remote(hosts_file, ip , username, password)
        os.system('ansible-playbook -i hosts ' + application + '.yml ')
    else:
        print('Input error, please input "local" or "remote".')

