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

Linux_Release=`cat /etc/*-release | awk -F' ' 'NR==1{print $1}'`

if [ "${Linux_version}"=="CentOS" ]; then
  yum install epel-release git python3 ansible -y 1>/dev/null 2>&1
fi

if [ "${Linux_version}"=="DISTRIB_ID=Ubuntu" ]; then
  apt-get update 2>/dev/null;
  apt-get install software-properties-common -y 1>/dev/null 2>&1;
  apt-add-repository --yes --update ppa:ansible/ansible 1>/dev/null 2>&1;
  apt-get install git python3-pip ansible -y 1>/dev/null 2>&1
fi

wget -P /opt https://raw.githubusercontent.com/Websoft9/linux/master/ansible_script/install.py


