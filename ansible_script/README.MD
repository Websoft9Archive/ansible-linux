该脚本使用 Python2 运行，Python3支持还在开发中。

## 使用示例

CentOS/Redhat系统：
yum install python3 -y; wget 脚本链接; python3 应用名 git仓库地址 初始化参数

Ubuntu系统：
apt install python3 -y; wget 脚本链接; python3 应用名 git仓库地址 初始化参数

例如,在Ubuntu上安装zabbix：
~~~
wget https://raw.githubusercontent.com/Websoft9/linux/master/ansible_script/install.py ; python install.py zabbix https://github.com/Websoft9/ansible-zabbix.git init=0
~~~

## 变量

python install.py 命令之后，是可变变量：

```
#适用于制作镜像，init=1表示初始化操作系统
python install.py zabbix https://github.com/Websoft9/ansible-zabbix.git init=1

#适用于用户使用，init=0表示不初始化操作系统
python install.py zabbix https://github.com/Websoft9/ansible-zabbix.git init=0
```