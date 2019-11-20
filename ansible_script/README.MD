TODO：  
兼容Python2

使用方法：
CentOS/Redhat系统：
yum install python3 -y; wget 脚本链接; python3 应用名 git仓库地址

Ubuntu系统：
apt install python3 -y; wget 脚本链接; python3 应用名 git仓库地址

例如,在Ubuntu上安装zabbix：
~~~
apt install python3 -y; wget https://github.com/Websoft9/linux/blob/master/ansible_script/install.py ; python3 zabbix https://github.com/Websoft9/ansible-zabbix.git
~~~