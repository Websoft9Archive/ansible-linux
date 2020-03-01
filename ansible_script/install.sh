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
ARG_NUM=$#      #传入参数的个数
while :; do
  [ -z "$1" ] && break;
  case "$1" in 
    -h|--help)
      Show_Help; exit 0
      ;;
    -v|-V|--version)
      version; exit 0
      ;;
  esac
done

if command -v yum > /dev/null; then
  yum install libselinux-python epel-release git python python-pip python3 python3-pip -y 1>/dev/null 2>&1
  pip3 install ansible 1>/dev/null 2>&1
fi

if command -v apt > /dev/null; then
  apt update 1>/dev/null 2>&1
  apt-get install git python python-pip python3 python3-pip -y 1>/dev/null 2>&1
  pip3 install ansible 1>/dev/null 2>&1
fi

python -m pip install -U --force-reinstall pip
wget -P /opt https://raw.githubusercontent.com/Websoft9/linux/master/ansible_script/install.py 1>/dev/null 2>&1
echo "Install Complete"
