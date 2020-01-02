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
    --playbook,          Select a playbook
    --init,              default: 0
    --install-ansible,   Choose whether to install ansible[y/n]
    "
}
ARG_NUM=$#      #传入参数的个数
TEMP=`getopt -o hvV --long help,version,playbook,init,install-ansible -- "$@" 2>/dev/null`
eval set -- "${TEMP}"
while :; do
  [-z "$1"] && break;
  case "$1" in 
    -h|--help)
      Show_Help; exit 0
      ;;
    -v|-V|--version)
      version; exit 0
      ;;
    --playbook)
      playb=$1;
      [[ -z ${playb} ]] && { echo "${CWARNING}Project_url input error! Please input a github repostory url;" exit 1; }
  esac
done

Linux_Release=`cat /etc/*-release | awk -F' ' 'NR==1{print $1}'`

if [ "${Linux_version}" == 'CentOS' ]; then
    yum install epel-release python3 ansible -y 2>/dev/null
fi

playb=`read -e -p "which application do you want to install? Please input it's github url: " `






