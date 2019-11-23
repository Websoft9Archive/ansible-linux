import os, sys, platform, shutil

# 安装ansible
def install_ansible(a, distribution):
    if a in ('yes', 'y') and distribution == 'centos':
        os.system("yum install epel-release.noarch git ansible -y")
    elif a in ('yes', 'y') and distribution == 'Ubuntu':
        os.system('apt update; apt install software-properties-common; apt-add-repository --yes --update ppa:ansible/ansible;\
        apt install git ansible -y')
    elif a.lower() == ('n' or 'no'):
        sys.exit()
    else:
        print("Only input yes or no!")

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

def check_python_version():
    if sys.version_info.major < 3:
        try:
            input = raw_input
        except NameError:
            pass
    return

def ping_module(ip, username, password):
    os.system("ssh " + username + "@" + ip )



