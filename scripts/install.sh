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

while getopts ":r:"":i:"  opt
do
    case $opt in
        r)
        repo_name=$OPTARG;;
        i)
        repo_init=$OPTARG
        ;;
        ?)
        echo "参数无值"
        exit 1;;
    esac
done
echo $repo_name
echo $repo_init

echo "Pre-installation is starting, please wait for 1-3 minutes..."

# install pip for Oracle which yum have not pip
# to do: this command can not run in Azure, lsb_release not found
# q_str=$(lsb_release -a);s_str="Oracle"; if [[ $q_str == *$s_str* ]];then curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py;sudo python get-pip.py;fi

if command -v yum > /dev/null; then
  sudo yum update -y 1>/dev/null 2>&1
  sudo yum install -y epel-release 1>/dev/null 2>&1
  sudo yum install yum-utils libselinux-python git python python2-pip python3 python3-pip -y 1>/dev/null 2>&1
  sudo pip3 install -U --force-reinstall requests docker 1>/dev/null 2>&1
fi

if command -v apt > /dev/null; then
  sudo apt update 1>/dev/null 2>&1
  sudo apt-get install git python python2-pip python3 python3-pip -y 1>/dev/null 2>&1
  sudo pip3 install -U --force-reinstall requests docker 1>/dev/null 2>&1
fi

sudo python -m pip install -U --force-reinstall pip
sudo echo "Pre-installation has beend completed"

if [[ $repo_name != "" ]]
then
sudo pip3 install -U --force-reinstall ansible
sudo rm -rf  /tmp/ansible-$repo_name
sudo cd /tmp; sudo git clone https://github.com/Websoft9/ansible-$repo_name.git;
sudo cd /tmp/ansible-$repo_name;sudo ansible-galaxy install -r requirements.yml -f
sudo touch  /tmp/ansible-$repo_name/hosts
sudo echo "localhost" > /tmp/ansible-$repo_name/hosts
sudo ansible-playbook -i hosts $repo_name.yml -c local -e init=$i
sudo shutdown -r -t 3 "System will restart in 3s, then installation completed"
fi
