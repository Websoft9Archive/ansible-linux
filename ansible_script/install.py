#!/usr/bin/python env
#coding: utf-8

import os, sys, platform, shutil
#from distutils.spawn import find_executable

def root_judge():
    if os.getuid() != 0:
        print("This program must be run as root. Aborting.")
        sys.exit(1)

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

# 选择在本地还是远端安装(此函数暂时不用)
def install_where():
    b = input("\nWhere do you want to install it? [1/2]: \n\t 1. local server \n\t 2. remote server\nPlease input a number: ")
    while b not in ('1', '2'):
      print('\nInput error, please input "1" or "2".')
      b = input("\nWhere do you want to install it? [1/2]: \n\t 1. local server \n\t 2. remote server\nPlease input a number: ")
    if b == "2":
      print('\nYou must input your remote server IP and account for installation\n')
      ip = input("\tPublic or Internet IP: ")
      username = input("\tUsername: ")
      password = input("\tPassword: ")
    #to do 验证输入的账号密码是否可以ssh登录，如果不可以询问用户：重新输入 or 退出？

# 写入hosts文件
def write_file_local(hosts):
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

#-----------------start 获取入口变量--------------#

#主playbook
application = sys.argv[1][6:]
#项目git地址或本地已上传
url = sys.argv[2][4:]
#安装完成后是否初始化操作系统
init_os= sys.argv[3][5:]
#是否需要安装ansible
exist_ansible=sys.argv[4][8:]

#-----------------end 获取入口变量--------------#

root_judge()

# 确认是否安装ansible
a = input("\nAre you sure to start installation?  [y/n]: ").lower()
while a not in ('y', 'n'):
    print('\nInput error, please input "y" or "n":  ')
    a = input("\nAre you sure to start installation?  [y/n]: ").lower()

if a in ('no', 'n'):
    sys.exit()

print("\nStarting pre-installation, waiting for 1-3 minutes...\n")

#默认安装到本地
b='1'

# 判断主控端操作系统发行版本,支持CentOS和Ubuntu
distribution = platform.dist()[0]

# 主控端安装ansible
if exist_ansible == "y":
   install_ansible(a, distribution)

# 脚本存放路径
directory = "/tmp/ansible"

# 克隆ansible仓库
if url != "local":
   download(url, directory)
   #切换到/tmp/ansible目录
   os.chdir(directory)
   # 创建hosts文件
   hosts_file = '/tmp/ansible/hosts'
else:
   hosts_file = 'hosts'

if b == "1":
    write_file_local(hosts_file)
    os.system('ansible-playbook -i hosts ' + application + '.yml -c local'+ ' -e init=' + init_os)
elif b == "2":
    write_file_remote(hosts_file, ip , username, password)
    os.system('ansible-playbook -i hosts ' + application + '.yml ' + ' -e init=' + init_os)