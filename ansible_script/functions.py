import os
import sys
import platform

# 安装ansible
def install_ansible(a):
    if a.lower() == ('y' or 'yes'):
        os.system("yum install epel-release.noarch git ansible -y")
    elif a.lower() == ('n' or 'no'):
        sys.exit()
    else:
        print("Only input yes or no!")

# 克隆ansible仓库
def download(url):
    os.system("git clone " + url + " /tmp/ansible")

def wirte_file_local(hosts):
    with open(hosts, 'w') as hosts:
        hosts.write("[local] \n")
        hosts.write("localhost")

def write_file_remote(hosts, ip, username, password):
    os.system("sed -i 's/#host_key_checking = False/host_key_checking = False/g'  /etc/ansible/ansible.cfg")
    with open(hosts, 'w') as hosts:
        hosts.write("[remote] \n")
        hosts.write(ip + "\t ansible_ssh_user=" + username + "\t ansible_ssh_pass=" + password + "\t ansible_sudo_pass=" + password)

