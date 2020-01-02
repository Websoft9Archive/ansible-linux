# 最佳实践

## 如何连接Linux？

## 如何安装FTP？

## 如何初始化数据磁盘？

## 如何自定义服务？

## 如何设置计划任务？

## 如何安装图形化桌面

### Centos/Oracle Linux
```
yum groupinstall -y "GNOME Desktop" 
systemctl set-default graphical.target
systemctl set-default graphical.target

```

## 如何安装VNC Server

### Centos/Oracle Linux

```
yum install tigervnc-server -y

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

### Webmin

Webmin是一款开源免费的Web面板，可以对Linux进行深度操作。


登录方式：*http://公网IP地址:10000* ，登录账号为服务器账号（root/服务器密码）

更多参考[详细文档](https://libs.websoft9.com/Websoft9/documents/zh/webmin/index.html)
