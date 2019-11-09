import os

# 克隆ansible仓库
def download(url):
    os.system("git clone " + url + " /tmp/ansible")

def wirte_file_local(hosts):
    with open(hosts, 'r') as hosts:
        hosts.write("[local] \n")
        hosts.write("localhost")

def write_file_remote(hosts, ip, username, password):
    with open(hosts, 'w') as hosts:
        hosts.write("[remote] \n")
        hosts.write(ip + "\t ansible_ssh_user=" + username + "\t ansible_ssh_pass=" + password + "\t ansible_sudo_pass=" + password)
