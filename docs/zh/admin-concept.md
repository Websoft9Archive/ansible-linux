# 要点

Linux系统博大精深，学习Linux的资料浩瀚如大海。本文档不打算再做重复造轮子的事情，我们尽量根据实践中很常见的**技术要点**进行讲解，同时列出一些操作范例：

## 安装

如果你没有使用云服务器或虚拟机，就需要安装Linux。下面只大体介绍Linux系统的安装流程：

* 下载Linux系统（一般是ISO文件）
* 制作启动盘
* 开机进入图形化的交互式安装界面
* 安装完成


## 启动

### 开机启动

Linux系统的启动过程分为5个阶段：

* 内核的引导：读入 /boot 目录下的内核文件
* 运行 init：init是一个管理进程的进程，init进程的一大任务，就是去运行开机启动的程序
* 系统初始化：这个阶段主要完成激活交换分区，检查磁盘，加载硬件模块等任务。
* 建立终端：系统打开6个终端，以便用户登录系统。在inittab中的以下6行就是定义了6个终端
* 用户登录系统：用户登录使用Linux

### 启动脚本

上面介绍了Linux系统开机的启动的宏观过程。下面再针对于Linux内核加载后，系统脚本的启动情况。


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

## 编码与字体

一个字符（不管是中文还是英文，或是其它文字）在计算机里都是以0101这样数字存放的，编码就是某个字符是以一个什么数字存放在计算机里的。  

字符编码有名为字符集。其原理一句话解释：不同语言对应的机器编码。目前最常用的是**UTF-8**编码方式，下面就是通一个字符在不同字符编码下的机器代码：

| 语言 | 示例               | UTF-8编码  |
| -------- | ------------------------------ | ------------------ |
| 中文    | 你好                    | \xE4\xBD\xA0\xE5\xA5\xBD |
| 英文    | Hello                    | \x68\x65\x6C\x6C\x6F |

编码决定字符的存放，字体决定字符的显示。

字体决定一个字符在界面上显示出来的形状，比如同样是'A'用不同的字体显示出来的形状是不一样的。

同样的文件内容，在屏幕上的输出同时取决于用什么编码和字体。


### 查看编码

我们在Linux中输入 `locale` 命令，会得到如下的结果：

```
[root@test ~]# locale
LANG=en_US.UTF-8
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=
```

en_US.UTF-8 是 UTF-8 的子集，也就是说en_US.UTF-8也是支持中文字符的。区别在于zh_US.UTF-8能够支持更多的汉语特殊字符。

### 修改编码

如果想切换操作系统的默认显示的语言，就必须修改默认的编码。

### 字体

我们在实际操作中发现即使当前是en_US.UTF-8编码，如果安装下面的命令后，操作系统便可以正常显示中文。
```
yum groupinstall "fonts"
```
这是为什么呢？ 这个要从计算图形学的角度去分析。编码解决了字符是否可以被计算的问题，而字体解决的是字符渲染成图像，被人识别的问题。

即，如果你希望可以显示中文，你的服务器就必须有中文字体。

> 最后我们来总结：字符编码就是把二进制字节码文件转成计算机能够懂的文字；字体就是把计算机中的文字转换成人能够看懂的图像

## Linux与云计算

在当前的云计算领域，毫无疑问Linux系统是最重要的基石。  

掌握了Linux就等于拿到了云计算领域的入场券。

## Linux命令

Linux命令是对Linux系统进行管理的命令。对于Linux系统来说，无论是CPU、内存、磁盘驱动器、键盘、鼠标，还是用户等都是文件，Linux系统管理的命令是它正常运行的核心，与之前的DOS命令类似。

更多命令参考：[《Linux命令大全》](https://man.linuxde.net/)

## 软（硬）连接

Linux中的软连接和硬连接很常用，下面分别介绍。

### 软连接

软连接是指向另外一个文件的文件，类似Windows中的快捷方式文件。  

如何才能知道哪些文件是软连接文件呢？

#### 查询软连接

我们先进入etc目录，然后列出文件（以re关键词作为结果筛选）

```
root@test:/etc# ls -l | grep re
-rw-r--r-- 1 root root     367 Jan 27  2016 bindresvport.blacklist
drwxr-xr-x 2 root root    4096 Apr  9 06:04 firefox
lrwxrwxrwx 1 root root      33 Dec 25 16:13 localtime -> /usr/share/zoneinfo/Asia/Shanghai
-rw-r--r-- 1 root root     105 Jan 30 20:28 lsb-release
lrwxrwxrwx 1 root root      21 Jan 30 20:28 os-release -> ../usr/lib/os-release
drwxr-xr-x 4 root root    4096 Dec 25 16:13 resolvconf
lrwxrwxrwx 1 root root      29 Dec 25 16:13 resolv.conf -> ../run/resolvconf/resolv.conf
-rw-r--r-- 1 root root    3663 Jun  9  2015 screenrc
-rw-r--r-- 1 root root    4141 Jan 25  2018 securetty
-rw-r--r-- 1 root root    1656 Jul 25  2019 tmpreaper.conf

root@test:/etc# ls -l | grep ^l
lrwxrwxrwx 1 root root      33 Dec 25 16:13 localtime -> /usr/share/zoneinfo/Asia/Shanghai
lrwxrwxrwx 1 root root      19 Dec 26 00:11 mtab -> ../proc/self/mounts
lrwxrwxrwx 1 root root      21 Jan 30 20:28 os-release -> ../usr/lib/os-release
lrwxrwxrwx 1 root root      29 Dec 25 16:13 resolv.conf -> ../run/resolvconf/resolv.conf
lrwxrwxrwx 1 root root      23 Dec 25 16:08 vtrgb -> /etc/alternatives/vtrgb

```

上面的例子中，我们运行了 `ls -l` 命令，显示了几种不同类型的文件：

* lrwxrwxrwx: 这种以l开头的就是软连接文件
* drwxr-xr-x：这种以d开头的就是目录
* -rw-r--r--：这种以-开头的就是文件

了解了什么是软连接之后，我们就可以自己动手进行软连接的相关操作：

#### 创建软连接

```
cd /root
ln -s /usr/share/zoneinfo/Asia/Shanghai2 mysoftlink
file mysoftlink
```

#### 删除软连接

```
rm -rf mysoftlink
```

注意事项：  

1. 被连接的文件名（路径）建议采用绝对路径
2. 错误的软连接（又名断开）使用 `ls -l` 的时候显示的是红色
3. 软连接是一个文件，其在硬盘中是存在数据块的
4. 软连接文件的数据库中存储的是路径信息，而非真正的数据
5. 软连接可能是多级嵌套的，例如：B连接A，C连接B，D连接C

### 硬连接

硬连接相对于软连接来说，理解会困难一点点。硬连接是把不同的文件名对应到同一个存储块节点上。  

例如：在服务器硬盘中有一个数据块存在的是一段小视频，这个小视频的文件名称为：/data/mymedia.mp4。  

创建一个硬连接，只需使用`ln`命令即可

```
cd /data
ln /data/mymedia.mp4  mymedia2.mp4
```

注意事项：  

1. 被连接的文件名（路径）建议采用绝对路径
2. 如果一个文件增加了对应的硬连接，那么删除文件的时候不会删除数据
3. 硬连接文件存储的是真实数据块位置
4. 只能对文件建立硬连接，而不能对一个目录建立硬连接


> 硬链接与域名管理中的同一个网站，用A记录配置上两个域名是同类原理。  
软连接与域名管理中的cname解析是同类原理。

## 环境变量

环境变量即操作系统的变量。环境变量非常灵活，在实际使用过程中需要深刻理解几个关键要点：环境变量作用域、环境变量存放处以及存储环境变量的文件的开机启动顺序。

```
# 列出所有变量
set

# 列出所有环境变量
env

# 列出和设置环境变量
export 
export varname

# 列出所有别名
alias
```

## Systemd

Systemd 是 Linux 系统中最新的初始化系统（init），它主要的设计目标是克服 sysvinit 固有的缺点，提高系统的启动速度。  

监控和控制 Systemd 主要使用的指令是`systemctl`。主要是从来看系统状态、服务状态，以及管理系统和服务。

所有可用的单元都在 /etc/systemd/system/(优先度高) 和 /usr/lib/systemd/system/(优先度低)。

### 维护命令

```
# 通过ssh连接远程控制其他主机
systemctl -H <username>@<URL>

# 显示系统状态
ystemctl status

# 输出激活的单元列表
systemctl 或 systemctl list-units

# 输出运行失败的单元
systemctl —failed

# 查看所有已安装的服务 
systemctl list-unit-files
```

### 配置单元

一个单元配置文件可以描述如下内容之一：系统服务（.service）、挂载点（.mount）、sockets（.sockets） 、系统设备（.device）、交换分区（.swap）、文件路径（.path）、启动目标（.target）、由 systemd 管理的计时器（.timer）。

我们通常在用systemctl调用单元的时候一般要单元文件的全名。也就是带上述后缀的那些。
如果不带扩展名的话systemctl会默认成是.service文件，所以为了不发生意外一般还是推荐把名字打全了。
挂载点和设备会自动转化为对应的后缀单元，比如/home就等价于home.mount, /dev/sda等价于dev-sda.device。

systemctl在enable、disable、mask子命令里面增加了--now选项，可以激活同时启动服务，激活同时停止服务等。
```
立刻激活单元：$ systemctl start <unit>
立刻停止单元：$ systemctl stop <unit>
重启单元：$ systemctl restart <unit>
重新加载配置：$ systemctl reload <unit>
输出单元运行的状态：$ systemctl status <unit>
检测单元是否为自动启动：$ systemctl is-enabled <unit>
设置为开机自动激活单元：$ systemctl enable <unit>
设置为开机自动激活单元并现在立刻启动：$ systemctl enable --now <unit>
取消开机自动激活单元：$ systemctl disable <unit>
禁用一个单元：$ systemctl mask <unit>
取消禁用一个单元：$ systemctl unmask <unit>
显示单元的手册页（前提是由unit提供）：$ systemctl help <unit>
重新载入整个systemd的系统配置并扫描unit文件的变动：$ systemctl daemon-reload
```

上述内容来源于：https://www.jianshu.com/p/c498327f39d4


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