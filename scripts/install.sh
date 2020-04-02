#!/bin/bash
export PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin
clear

# Check if user is root
[ $(id -u) != "0" ] && { echo "Error: You must be root to run this script, please use 'sudo su -' command to change root"; exit 1; }

version(){
    echo "version: 0.1"
    echo "updated date: 2019-12-30"
}

Show_Help(){
    version
    echo "Usage: $0 command ...[parameters]...
    --help, -h           Show this help message
    --version, -v        Show version info
    "
}

while getopts ":r:" opt
do
    case $opt in
        r)
        repo_name=$OPTARG
        ;;
        ?)
        echo "参数无值"
        exit 1;;
    esac
done
echo $repo_name

echo "Pre-installation is starting, please wait for 1-3 minutes..."

# install pip for Oracle which yum have not pip
q_str=$(lsb_release -a);s_str="Oracle"; if [[ $q_str == *$s_str* ]];then curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py;sudo python get-pip.py;fi

if command -v yum > /dev/null; then
  yum install libselinux-python epel-release git python python-pip python3 python3-pip -y 1>/dev/null 2>&1
  pip3 install -U --force-reinstall requests docker 1>/dev/null 2>&1
fi

if command -v apt > /dev/null; then
  apt update 1>/dev/null 2>&1
  apt-get install git python python-pip python3 python3-pip -y 1>/dev/null 2>&1
  pip3 install -U --force-reinstall requests docker 1>/dev/null 2>&1
fi

python -m pip install -U --force-reinstall pip
echo "Pre-installation has beend completed"

if [[ $repo_name != "" ]]
then
pip3 install -U --force-reinstall ansible
rm -rf  /tmp/ansible-$repo_name
cd /tmp; git clone https://github.com/Websoft9/ansible-$repo_name.git;
echo "localhost" > /tmp/ansible-$repo_name/hosts
cd ansible-$repo_name;ansible-galaxy install -r requirements.yml -f
ansible-playbook -i hosts $repo_name.yml -c local -e init=0
fi
