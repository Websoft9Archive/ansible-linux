import os
import sys
import functions as ft

application = "redis"
url = "https://github.com/Websoft9/ansible-redis.git"

if os.getuid() != 0:
    print ("This program must be run as root. Aborting.")
    sys.exit(1)

a = input("Are you sure install ansible?[y/n] ")

if a.lower() == ('y' or 'yes'):
    os.system("yum install epel-release.noarch git ansible -y")
elif a.lower() == ('n' or 'no'):
    sys.exit()
else:
    print("Only input yes or no!")

# 下载ansible仓库
ft.download(url)

directory = "/tmp/ansible"
os.chdir(directory)  #切换到/tmp/ansible目录
# 创建hosts文件
hosts = '/tmp/ansible/hosts'

b = input("Do you want install this application on local server or remote server?[local/remote]")
if b == "local":
    ft.wirte_file_local(hosts)
    os.system('ansible-playbook -i hosts ' + application + '.yml -c local')
elif b == "remote":
    ip = input("Please input your server's public IP: ")
    username = input("Please input your server's username: ")
    password = input("Please input your srever's password: ")
    ft.write_file_remote(hosts, ip , username, password)
    os.system('ansible-playbook -i hosts ' + application + '.yml ')
else:
    print('Input error, please input "local" or "remote".')

