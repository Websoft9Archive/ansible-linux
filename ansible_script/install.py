#!/usr/bin/python env
#coding: utf-8

import os, sys, platform, shutil
#from distutils.spawn import find_executable

# 安装ansible
def install_ansible(a, distribution):
    if a in ('yes', 'y') and distribution == 'centos':
        os.popen("yum install epel-release.noarch git ansible -y 2>/dev/null")
    elif a in ('yes', 'y') and distribution == 'Ubuntu':
        os.popen('apt-get update 2>/dev/null; apt-get install software-properties-common -y 2>/dev/null; \
        apt-add-repository --yes --update ppa:ansible/ansible 2>/dev/null;\
        apt-get install git ansible -y 2>/dev/null')
    elif a in ('no', 'n'):
        sys.exit()
    else:
        print("Only input Y/N !")

# 克隆ansible仓库
def download(url, directory):
    if not os.path.exists(directory):
        os.system("git clone " + url + " /tmp/ansible")
    elif os.path.exists(directory):
        shutil.rmtree(directory)
        os.system("git clone " + url + " /tmp/ansible")

# 写入hosts文件
def wirte_file_local(hosts):
    with open(hosts, 'w') as hosts:
        hosts.write("[local] \n")
        hosts.write("localhost")

def write_file_remote(hosts, ip, username, password):
    os.system("sed -i 's/#host_key_checking = False/host_key_checking = False/g'  /etc/ansible/ansible.cfg")
    with open(hosts, 'w') as hosts:
        hosts.write("[remote] \n")
        hosts.write(ip + "\t ansible_ssh_user=" + username + "\t ansible_ssh_pass=" + password + "\t ansible_sudo_pass=" + password)

###############################################

try:
    input = raw_input
except NameError:
    pass

print(sys.argv)

application = sys.argv[1]
url = sys.argv[2]

if os.getuid() != 0:
    print ("This program must be run as root. Aborting.")
    sys.exit(1)

# 确认是否安装ansible
a = input("Are you sure install ansible?[yes/no] ").lower()
while a not in ('yes', 'no'):
    print('Input error, please input "Y/N"')
    a = input("Are you sure  install ansible?[Y/N] ").lower()
# 确认在本地还是远端安装
b = input("Do you want install this application on local server or remote server?[local/remote]")
while b not in ('local', 'remote'):
    print('Input error, please input "local" or "remote".')
    b = input("Do you want install this application on local server or remote server?[local/remote]")

print("Please Wait...")

# 判断系统发行版本,支持CentOS和Ubuntu
distribution = platform.dist()[0]
# 安装ansible
install_ansible(a, distribution)

# 脚本存放路径
directory = "/tmp/ansible"
# 下载ansible仓库
download(url, directory)

#切换到/tmp/ansible目录
os.chdir(directory)
# 创建hosts文件
hosts_file = '/tmp/ansible/hosts'

if b == "local":
    wirte_file_local(hosts_file)
    os.system('ansible-playbook -i hosts ' + application + '.yml -c local')
elif b == "remote":
    ip = input("Please input your remote server's public IP: ")
    username = input("Please input your remote server's username: ")
    password = input("Please input your remote srever's password: ")
    write_file_remote(hosts_file, ip , username, password)
    os.system('ansible-playbook -i hosts ' + application + '.yml ')

