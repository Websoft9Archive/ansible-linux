# 网络与安全

## 防火墙

与Linux防火墙有关的组件有三个，它们分别是：firewalld、iptables和nftables

```
#CentOS 安装 iptables
yum install iptables -y

#CentOS 安装 firewalld
yum install firewalld -y
```

据说，从CentOS7开始，建议使用firewalld作为主要的防火墙管理工具。firewalld功能更全面，甚至支持图形化设置，`firewall-config &`

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/firewalld-gui-websoft9.png)


> 如果使用云服务器，Linux系统的防火墙的端口管理被安全组替代，只要设置好合适的安全组规则，就能很好的控制端口的访问。

## 安全组件使用

### clamav 基本使用
1.更新病毒库 命令 : freshclam 2\. 扫描: 2.1 扫描所有用户的主目录就使用 clamscan -r /home 2.2 扫描您计算机上的所有文件并且显示所有的文件的扫描结果，就使用 clamscan -r / 2.3 扫描您计算机上的所有文件并且显示有问题的文件的扫描结果， 就使用 clamscan -r –bell -i /

### LMD 基本使用

扫描:maldet –scan-all /var #扫描 /var 目录

### rkhunter基本使用

更新:rkhunter –update

扫描恶意软件和检查系统基本安全:rkhunter –check

### Lynix 基本使用

检测: lynix audit system -Q #检测系统安全问题 并提出一定得建议