该脚本使用 Python2 运行，Python3支持还在开发中。

## 使用示例

CentOS/Redhat系统：
yum install python3 -y; wget 脚本链接; python3 应用名 git仓库地址 初始化参数

Ubuntu系统：
apt install python3 -y; wget 脚本链接; python3 应用名 git仓库地址 初始化参数

例如,在Ubuntu上安装zabbix：
~~~
wget -N https://raw.githubusercontent.com/Websoft9/linux/master/ansible_script/install.py ; python install.py playb=zabbix url=https://github.com/Websoft9/ansible-zabbix.git init=0 ansible=y
~~~

## 变量

python install.py 命令之后，是可变变量：

* playb main playbook，
* url  local | https://https://github.com/Websoft9/ansible-×××.git，local 表示已经上传了ansible-xxx项目到服务器，且install.py同时存在项目的根目录
* init  0 | 1，  1表示初始化操作系统
* ansible y | n，y表示需要安装ansible，n表示ansible已经存在无需安装

```
#适用于用户使用，init=0,ansible=y
python install.py playb=zabbix url=https://github.com/Websoft9/ansible-zabbix.git init=0 ansible=y


#适用于制作镜像，init=1,ansible=y
python install.py playb=zabbix url=https://github.com/Websoft9/ansible-zabbix.git init=1 ansible=y


#适用于测试使用，init=0,ansible=n.提前将ansible项目上传到服务器，同时将install.py文件上传到项目的根目录
python install.py playb=zabbix url=local init=0 ansible=n
```