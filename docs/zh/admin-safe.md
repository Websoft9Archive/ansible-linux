# 网络与安全

## 防火墙

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