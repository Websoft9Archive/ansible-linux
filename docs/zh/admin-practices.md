# 最佳实践

## 如何连接Linux？

最常见的方式是使用SSH工具连接Linux，SSH工具包括：Putty,Xshell,WinSCP等  

如果使用云服务器，云厂商一般都会提供在线的SSH工具

## 如何安装FTP？

安装FTP是比较繁琐的工作，具体参考：[FTP相关章节](/zh/admin-file.md#ftp)

## 如何初始化数据磁盘？

初始化数据磁盘主要分为三个步骤：

* 磁盘分区
* 磁盘初始化
* 磁盘挂载

## 如何写一个系统服务？

服务(service) 本质就是进程，但是是运行在后台的，通常都会监听某个端口，等待其它程序的请求，比如(mysql , sshd 防火墙等)，因此我们又称为守护进程，是 Linux 中非常重要的知识点。

一般通过下面的格式来管理服务：
```
systemctl    服务名 [start | stop | restart | reload | status]
```

那服务是如何创建的呢？以Websoft9提供的Redmine自动化项目为例，下面描述完整的服务创建过程：

1. 编辑好[redmine.service](https://github.com/Websoft9/ansible-redmine/blob/master/roles/redmine/files/redmine.service)文件
   ```
   [Unit]
   Description=Redmine
   After=nginx.service
   [Service]
   Environment=RAILS_ENV=production
   Type=simple
   WorkingDirectory=/data/wwwroot/redmine
   ExecStart=/usr/local/bin/puma -b tcp://127.0.0.1:9292 -e production 
   User=redmine
   [Install]
   WantedBy=multi-user.target
   ```
2. 将服务文件放入路径：*/etc/systemd/system* 下
3. 启动并设置开机启动
4. 测试服务的可用性
   ···
   systemctl restart redmine
   systemctl stop redmine
   ···

## 如何设置计划任务？

Cron是一个Linux下的定时执行工具，可以在无需人工干预的情况下定时地运行任务task。

1. 安装Crontab
   ```
   yum install vixie-cron
   yum install crontabs
   ```
2. 编写计划任务脚本：我们推荐一个在线的[Crontab生成器](https://crontab-generator.org/)，帮助不熟悉语法的用户简化脚本的编写
   ```
   4 * * * * echo "hello" >/dev/null 2>&1
   ```
3. 将脚本插入Cron配置文件：*/etc/crontab*

## 如何安装图形化桌面

下面针对不同Linux家族，提供安装桌面的命令

### CentOS/Oracle
```
yum groupinstall -y "GNOME Desktop" 
systemctl set-default graphical.target
systemctl set-default graphical.target
```

### OracleLinux

1. 安装,使用root用户执行

   ```bash
   yum groupinstall -y 'Server with GUI'  # 如果这一步骤有错误,先执行 yum update 更新系统
   yum install -y tigervnc-server tigervnc-server-module
   ```

2. 配置桌面

   ```
   systemctl set-default graphical.target
   systemctl isolate graphical.target
   systemctl get-default
   ```

### Ubuntu
```
待完善
```

## 如何安装VNC Server

### Centos/Oracle Linux

1. 安装VNC

   ```bash
   yum install -y tigervnc-server tigervnc-server-module
   ```

2. 配置桌面

   ```
   # vnc 设置密码
   vncserver 
   
   # 配置文件
   cat > /etc/systemd/system/vncserver@:1.service << EOF
   [Unit]
   Description=Remote desktop service (VNC)
   After=syslog.target network.target
   
   [Service]
   Type=forking
   
   ExecStartPre=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'
   ExecStart=/usr/sbin/runuser -l root -c "/usr/bin/vncserver %i"
   PIDFile=/root/.vnc/%H%i.pid
   ExecStop=/bin/sh -c '/usr/bin/vncserver -kill %i > /dev/null 2>&1 || :'
   
   [Install]
   WantedBy=multi-user.target
   EOF
   
   # 启动VNC
   systemctl enable vncserver@:1.service
   systemctl start vncserver@:1.service
   ```

## 如何实现自动交互应答？

Linux 系统中，通过安装 expect 扩展，来实现自动交互应答
```
yum install expect -y
```

下面是一个 expect 使用范例：

```
#! /usr/bin/expect
set timeout 2  # 演示2秒
spawn /mnt/ask.sh  #开始 ask.sh 文件的交互式问答
expect "name?" #应对包含 name? 的问题
send "tom\r" #回答问题
expect "old?" #应对包含 old? 的问题
send "18\r"#回答问题
expect eof #结束
```

## 推荐可视化面板工具？


Linux命令行操作功能强大的同时，也让一些用户望而生畏。Linux面板工具可以通过Web页面，对服务器进行可视化操作，降低Linux使用门槛。

### Cockpit

Cockpit 是一个基于 Web 的服务器管理工具，可用于 CentOS 和 RHEL 系统。最近发布的 CentOS 8 和 RHEL 8，其中 cockpit 是默认的服务器管理工具。

![](https://libs.websoft9.com/Websoft9/DocsPicture/en/cockpit/cockpit-gui-websoft9.png)

### Webmin

Webmin是一款开源免费的Web面板，可以对Linux进行深度操作。


登录方式：*http://公网IP地址:10000* ，登录账号为服务器账号（root/服务器密码）

更多参考[详细文档](https://libs.websoft9.com/Websoft9/documents/zh/webmin/index.html)
