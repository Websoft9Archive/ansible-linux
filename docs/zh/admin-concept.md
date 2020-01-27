# 概念

## 安装

如果你没有使用云服务器或虚拟机，就需要安装Linux。下面只大体介绍Linux系统的安装流程：

* 下载Linux系统（一般是ISO文件）
* 制作启动盘
* 开机进入图形化的交互式安装界面
* 安装完成


## 启动

Linux系统的启动过程分为5个阶段：

* 内核的引导：读入 /boot 目录下的内核文件
* 运行 init：init是一个管理进程的进程，init进程的一大任务，就是去运行开机启动的程序
* 系统初始化：这个阶段主要完成激活交换分区，检查磁盘，加载硬件模块等任务。
* 建立终端：系统打开6个终端，以便用户登录系统。在inittab中的以下6行就是定义了6个终端
* 用户登录系统：用户登录使用Linux

## 目录结构

通过下面的一张图（右键在新窗口中打开，图片效果更好），我们了解Linux系统的目录结构

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-folders-websoft9.jpg)


## 发行版

Linux 内核最初只是由芬兰人林纳斯·托瓦兹（Linus Torvalds）在赫尔辛基大学上学时出于个人爱好而编写的。后面Linux发展成为一个强大的生态体系，慢慢的就有一些专业公司基于内核再组合了一些应用软件，形成了多种分支，也就是发行版。

目前市面上较知名的发行版有：Ubuntu、RedHat、CentOS、Debian、Fedora、SuSE、OpenSUSE、Arch Linux、SolusOS 等。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-distro-websoft9.png)

这些版本并非完全独立，它们之前有着共同的家族关系：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-family-websoft9.jpg)

虽然版本繁多，实际上最流行的是：CentOS和Ubuntu这个两个发行版。


## 认证

Linux认证指获得专业Linux培训后通过考试得到的资格。国际上广泛承认的Linux认证有LinuxProfessionalInstitute（简称为LPI）、SairLinux和GNU、Linux+和RedHatCertifiedEngineer。

以RedHat为例，主要的认证等级包括：

| 认证考试 | 认证培训课程编号               | 认证培训课程名称   |
| -------- | ------------------------------ | ------------------ |
| RHCSA    | RH124,RH135                    | 红帽认证系统管理员 |
| RHCE     | RH254                          | 红帽认证工程师     |
| RHCA     | RH401,RH436,RH423,RH442,RHS333 | 红帽认证架构师     |

## Linux与云计算

在当前的云计算领域，毫无疑问Linux系统是最重要的基石。  

掌握了Linux就等于拿到了云计算领域的入场券。

## Linux命令

Linux命令是对Linux系统进行管理的命令。对于Linux系统来说，无论是CPU、内存、磁盘驱动器、键盘、鼠标，还是用户等都是文件，Linux系统管理的命令是它正常运行的核心，与之前的DOS命令类似。

更多命令参考：[《Linux命令大全》](https://man.linuxde.net/)

## Shell编程

Shell 是一个用 C 语言编写的程序，它是用户使用 Linux 的桥梁。Shell 既是一种命令语言，又是一种程序设计语言。

通俗的说：用户向Linux发送Shell命令（或多个命令组成的程序体）来控制Linux，故 Shell 也是一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务。

### 解释器

Shell 编程跟 JavaScript、php 编程一样，只要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器就可以了。

Linux 的 Shell 种类众多，常见的有：

* Bourne Shell（/usr/bin/sh或/bin/sh）
* Bourne Again Shell（/bin/bash）
* Debian Almquist Shell(dash)
* C Shell（/usr/bin/csh）
* K Shell（/usr/bin/ksh）
* Shell for Root（/sbin/sh）

其中，bash和dash是目前广泛使用的解释器。

### 语法

Shell有着面向过程的程序设计常见的语法体系，包括：

* 变量
* 函数
* 流程控制
* 输入输出
* 数组
* 运算符

Shell语法并不复杂，边学边用就能掌握。

### 运行脚本

Shell脚本可以保存为 .sh 文件后运行，也可以直接在Linux交互式命令中运行

加入我们编写了一段Shell程序，内容如下
```
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi
```
将上面的代码保存为 test.sh，并 cd 到相应目录，然后选择如下的一种执行命令的方式：

```
#方式一：./ 执行脚本
chmod +x ./test.sh  #使脚本具有执行权限
./test.sh  #执行脚本

#方式二：直接用解释器执行脚本
/bin/sh test.sh

#方式三：直接用解释器执行脚本
bash test.sh

#方式四：直接在交互式命令上中运行一段Shell程序
if [ $(ps -ef | grep -c "ssh") -gt 1 ]; then echo "true"; fi

```