# 要点

Linux系统博大精深，学习Linux的资料浩瀚如大海。本文档不打算再做重复造轮子的事情，我们尽量根据实践中很常见的**技术要点**进行讲解，同时列出一些操作范例：

## 发行版

Linux 内核最初只是由芬兰人林纳斯·托瓦兹（Linus Torvalds）在赫尔辛基大学上学时出于个人爱好而编写的。后面Linux发展成为一个强大的生态体系，慢慢的就有一些专业公司基于内核再组合了一些应用软件，形成了多种分支，也就是发行版。

目前市面上较知名的发行版有：Ubuntu、RedHat、CentOS、Debian、Fedora、SuSE、OpenSUSE、Arch Linux、SolusOS 等。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-distro-websoft9.png)

这些版本并非完全独立，它们之前有着共同的家族关系：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-family-websoft9.jpg)

虽然版本繁多，实际上最流行的是：CentOS和Ubuntu这个两个发行版。

## 安装

如果你没有使用云服务器或虚拟机，就需要安装Linux。下面只大体介绍Linux系统的安装流程：

* 下载Linux系统（一般是ISO文件）
* 制作启动盘
* 开机进入图形化的交互式安装界面
* 安装完成

## 启动

Linux系统的启动过程分为如下几个阶段：

1. 开机自检：打开电源，BIOS进行硬件自检
2. 引导加载：自检通过后，进入MBR引导加载程序（MBR是硬盘中第一个扇区的前512个字节, 称为 main boot record）
3. 内核初始化：加载内核（Kernel）代码，即读入 /boot 目录下的内核文件，监测设备并加载设备驱动程序
4. Systemd初始化（替代init），获取系统控制权

   * 执行Systemd程序，Systemd是一个管理进程的进程程序，也是操作系统的第一个进程，其PID=1
   * 读取 /etc/systemd 下的配置文件
   * 读取 /etc/systemd/system/default.target 下的运行级别文件
   * 执行 */etc/rc.d/rc.local* 文件中的程序

2-4 是由GRUB（Grand Unified Bootloader）负责的。其中GRUB boot loader 代码的一小部分（子集）被写入MBR，其余部分存储在/boot分区中

5. Systemd 执行系统初始化
  
   * 设置主机名
   * 初始化网络
   * 基于配置初始化 SElinux
   * 显示欢迎标语
   * 基于内核参数初始化硬件
   * 加载文件系统
   * 清除 /var 中的目录
   * 启动交换分区

6. 建立终端：系统打开6个终端，以便用户登录系统。

7. 用户登录系统：用户登录使用Linux

## 目录结构

通过下面的一张图（右键在新窗口中打开，图片效果更好），我们了解Linux系统的目录结构

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-folders-websoft9.jpg)

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

## 进程

进程是操作系统的资源管理和调度单元。

* 当一个用户通过登录Linux系统，他就启动了一个shell进程
* 当一个进程创建另一个进程，就产生父进程和子进程的关系
* 当子进程运行时，父进程处于等待服务的状态，子进程完成它的工作后就会报告给父进程，再由父进程终止子进程

运行 `ps -ef` 列出所有进程:

```
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 Apr26 ?        00:00:02 /usr/lib/systemd/systemd --switched-root --system --deserialize 22
root         2     0  0 Apr26 ?        00:00:00 [kthreadd]
root         4     2  0 Apr26 ?        00:00:00 [kworker/0:0H]
root         6     2  0 Apr26 ?        00:00:00 [ksoftirqd/0]
root         7     2  0 Apr26 ?        00:00:00 [migration/0]
root         8     2  0 Apr26 ?        00:00:00 [rcu_bh]
root         9     2  0 Apr26 ?        00:00:00 [rcu_sched]
root        10     2  0 Apr26 ?        00:00:00 [lru-add-drain]
root        11     2  0 Apr26 ?        00:00:00 [watchdog/0]
root        12     2  0 Apr26 ?        00:00:00 [watchdog/1]
```

如果仅ps命令不带参数，其仅列出所在Shell所调度运行的进程（不会列出如何系统的守护进程）  

运行 `ps tree` 命令，列出进程树  
```
systemd─┬─NetworkManager─┬─dhclient
        │                └─2*[{NetworkManager}]
        ├─2*[abrt-watch-log]
        ├─abrtd
        ├─accounts-daemon───2*[{accounts-daemon}]
        ├─at-spi-bus-laun─┬─dbus-daemon
        │                 └─3*[{at-spi-bus-laun}]
        ├─at-spi2-registr───2*[{at-spi2-registr}]
        ├─atd
        ├─auditd─┬─audispd─┬─sedispatch
        │        │         └─{audispd}
        │        └─{auditd}
        ├─boltd───2*[{boltd}]
        ├─chronyd
        ├─colord───2*[{colord}]
        ├─crond
        ├─cupsd
        ├─2*[dbus-daemon]
        ├─dbus-launch
        ├─gdm─┬─X───3*[{X}]
        │     ├─gdm-session-wor─┬─gnome-session-b─┬─gnome-shell─┬─ibus-daemon─┬─ibus-dconf───3*[{ibus-dconf}]
        │     │                 │                 │             │             ├─ibus-engine-sim───2*[{ibus-engine-sim}]
        │     │                 │                 │             │             └─2*[{ibus-daemon}]
        │     │                 │                 │             └─14*[{gnome-shell}]
        │     │                 │                 ├─gsd-a11y-settin───3*[{gsd-a11y-settin}]
        │     │                 │                 ├─gsd-clipboard───2*[{gsd-clipboard}]
        │     │                 │                 ├─gsd-color───3*[{gsd-color}]
        │     │                 │                 ├─gsd-datetime───2*[{gsd-datetime}]
        │     │                 │                 ├─gsd-housekeepin───2*[{gsd-housekeepin}]
        │     │                 │                 ├─gsd-keyboard───3*[{gsd-keyboard}]
        │     │                 │                 ├─gsd-media-keys───3*[{gsd-media-keys}]
        │     │                 │                 ├─gsd-mouse───2*[{gsd-mouse}]
        │     │                 │                 ├─gsd-power───3*[{gsd-power}]
        │     │                 │                 ├─gsd-print-notif───2*[{gsd-print-notif}]
        │     │                 │                 ├─gsd-rfkill───2*[{gsd-rfkill}]
        │     │                 │                 ├─gsd-screensaver───2*[{gsd-screensaver}]
        │     │                 │                 ├─gsd-sharing───3*[{gsd-sharing}]
        │     │                 │                 ├─gsd-smartcard───4*[{gsd-smartcard}]
        │     │                 │                 ├─gsd-sound───3*[{gsd-sound}]
        │     │                 │                 ├─gsd-wacom───2*[{gsd-wacom}]
        │     │                 │                 ├─gsd-xsettings───3*[{gsd-xsettings}]
        │     │                 │                 └─3*[{gnome-session-b}]
        │     │                 └─2*[{gdm-session-wor}]
        │     └─3*[{gdm}]
        ├─ibus-portal───2*[{ibus-portal}]
        ├─ibus-x11───2*[{ibus-x11}]
        ├─irqbalance
        ├─lvmetad
        ├─polkitd───6*[{polkitd}]
        ├─pulseaudio───{pulseaudio}
        ├─python
        ├─rsyslogd───2*[{rsyslogd}]
        ├─rtkit-daemon───2*[{rtkit-daemon}]
        ├─sshd─┬─4*[sshd───bash]
        │      ├─3*[sshd───sftp-server]
        │      └─sshd───bash───pstree
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-udevd
        ├─tuned───4*[{tuned}]
        ├─udisksd───4*[{udisksd}]
        ├─upowerd───2*[{upowerd}]
        ├─wpa_supplicant
        ├─wrapper─┬─java───14*[{java}]
        │         └─{wrapper}
        └─xdg-permission-───2*[{xdg-permission-}]
```

还有更多与进程有关的命令是需要我们掌握的，包括：

* kill  终止进程，以PID作为标识
* pkill 终止进程，以名称作为标识
* pgrep 查询PID

### 守护进程

什么是守护进程？就是在后台运行的一个程序，主要提供一些系统服务。例如：httpd,nginx 等

守护进程是怎么工作的？它时刻等待事件的发生，当它收到一个请求事件之后，就会为需要处理这个事件创建一个子进程，然后它继续等待后续事件

根据事件的处理方式来看，守护进程分为：

* 独立守护进程
* 临时守护进程

临时守护进程无法直接面对请求事件，只能被 **xinetd** 这个超级守护进程分配任务。

## Systemd

[Systemd](https://www.freedesktop.org/software/systemd/man/systemd.unit.html) 是 Linux 系统中最新的初始化系统（init），它主要的设计目标是克服 sysvinit 固有的缺点，提高系统的启动速度。  

> 学习Systemd，参考阮一峰提供的通俗易懂的教程：[《Systemd 入门教程：实战篇》](http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-part-two.html)

根据 Linux 惯例，字母d是守护进程（daemon）的缩写。 Systemd 这个名字的含义，就是它要守护整个系统。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/systemd-components-websoft9.png)

Systemd 把每一项处理的任务以**单元**形式组织起来，所支持的各种类型的单元包括：  

* Service unit：系统服务
* Target unit：多个 Unit 构成的一个组
* Device Unit：硬件设备
* Mount Unit：文件系统的挂载点
* Automount Unit：自动挂载点
* Path Unit：文件或路径
* Scope Unit：不是由 Systemd 启动的外部进程
* Slice Unit：进程组
* Snapshot Unit：Systemd 快照，可以切回某个快照
* Socket Unit：进程间通信的 socket
* Swap Unit：swap 文件
* Timer Unit：定时器

Target 与 传统 RunLevel 的对应关系如下  

```
Traditional runlevel      New target name     Symbolically linked to...
Runlevel 0           |    runlevel0.target -> poweroff.target
Runlevel 1           |    runlevel1.target -> rescue.target
Runlevel 2           |    runlevel2.target -> multi-user.target
Runlevel 3           |    runlevel3.target -> multi-user.target
Runlevel 4           |    runlevel4.target -> multi-user.target
Runlevel 5           |    runlevel5.target -> graphical.target
Runlevel 6           |    runlevel6.target -> reboot.target
```

有三个目录可以存放目标单元：  

* /etc/systemd/system：系统管理员创建的单元，开机默认启动
* /usr/lib/systemd/system：应用程序安装包所创建的单元，开机不启动
* /run/systemd/system：运行期间创建的单元

下面举例解释 /etc/systemd/system 与 /usr/lib/systemd/system 的区别：

比如：Apache 安装的时候，会自动在/usr/lib/systemd/system 目录添加一个配置文件 httpd.service，如果你希望开机启动httpd，就需要运行如下的命令：

```
sudo systemctl enable httpd

systemctl enable docker
Created symlink from /etc/systemd/system/multi-user.target.wants/docker.service to /usr/lib/systemd/system/docker.service.

```

执行命令后，/etc/systemd/system 就多了一个指向  /usr/lib/systemd/system/httpd.service 的软连接。

当然，直接把 httpd.service 文件拷贝到 /etc/systemd/system 也能起到同样的效果。


### 维护命令

监控和控制 Systemd 主要使用的指令是`systemctl`。主要是从来看系统状态、服务状态，以及管理系统和服务。

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

### 配置文件

一个服务怎么启动，完全由它的配置文件决定。下面就来看，配置文件有些什么内容。

systemctl cat命令可以用来查看配置文件，下面以sshd.service文件为例，它的作用是启动一个 SSH 服务器，供其他用户以 SSH 方式登录。
```
$ systemctl cat sshd.service

[Unit]
Description=OpenSSH server daemon
Documentation=man:sshd(8) man:sshd_config(5)
After=network.target sshd-keygen.service
Wants=sshd-keygen.service

[Service]
EnvironmentFile=/etc/sysconfig/sshd
ExecStart=/usr/sbin/sshd -D $OPTIONS
ExecReload=/bin/kill -HUP $MAINPID
Type=simple
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target
```
#### [Unit]区域
#### [Service]区域

Service区块定义如何启动当前服务。

**Type** 字段定义启动类型。它可以设置的值如下。

```
simple（默认值）：ExecStart字段启动的进程为主进程
forking：ExecStart字段将以fork()方式启动，此时父进程将会退出，子进程将成为主进程
oneshot：类似于simple，但只执行一次，Systemd 会等它执行完，才启动其他服务
dbus：类似于simple，但会等待 D-Bus 信号后启动
notify：类似于simple，启动结束后会发出通知信号，然后 Systemd 再启动其他服务
idle：类似于simple，但是要等到其他任务都执行完，才会启动该服务。一种使用场合是为让该服务的输出，不与其他服务的输出相混合
```
**启动命令**字段  

```
ExecStart字段：定义启动进程时执行的命令。
ExecReload字段：重启服务时执行的命令
ExecStop字段：停止服务时执行的命令
ExecStartPre字段：启动服务之前执行的命令
ExecStartPost字段：启动服务之后执行的命令
ExecStopPost字段：停止服务之后执行的命令
```

#### [Install]区域

Install区块，定义如何安装这个配置文件，即怎样做到开机启动。

### 日志

Systemd 统一管理所有 Unit 的启动日志。带来的好处就是，可以只用journalctl一个命令，查看所有日志（内核日志和应用日志）。日志的配置文件是/etc/systemd/journald.conf。

journalctl功能强大，用法非常多。

```
# 查看所有日志（默认情况下 ，只保存本次启动的日志）
$ sudo journalctl

# 查看内核日志（不显示应用日志）
$ sudo journalctl -k

# 查看系统本次启动的日志
$ sudo journalctl -b
$ sudo journalctl -b -0

# 查看上一次启动的日志（需更改设置）
$ sudo journalctl -b -1

# 查看指定时间的日志
$ sudo journalctl --since="2012-10-30 18:17:16"
$ sudo journalctl --since "20 min ago"
$ sudo journalctl --since yesterday
$ sudo journalctl --since "2015-01-10" --until "2015-01-11 03:00"
$ sudo journalctl --since 09:00 --until "1 hour ago"

# 显示尾部的最新10行日志
$ sudo journalctl -n

# 显示尾部指定行数的日志
$ sudo journalctl -n 20

# 实时滚动显示最新日志
$ sudo journalctl -f

# 查看指定服务的日志
$ sudo journalctl /usr/lib/systemd/systemd

# 查看指定进程的日志
$ sudo journalctl _PID=1

# 查看某个路径的脚本的日志
$ sudo journalctl /usr/bin/bash

# 查看指定用户的日志
$ sudo journalctl _UID=33 --since today

# 查看某个 Unit 的日志
$ sudo journalctl -u nginx.service
$ sudo journalctl -u nginx.service --since today

# 实时滚动显示某个 Unit 的最新日志
$ sudo journalctl -u nginx.service -f

# 合并显示多个 Unit 的日志
$ journalctl -u nginx.service -u php-fpm.service --since today

# 查看指定优先级（及其以上级别）的日志，共有8级
# 0: emerg
# 1: alert
# 2: crit
# 3: err
# 4: warning
# 5: notice
# 6: info
# 7: debug
$ sudo journalctl -p err -b

# 日志默认分页输出，--no-pager 改为正常的标准输出
$ sudo journalctl --no-pager

# 以 JSON 格式（单行）输出
$ sudo journalctl -b -u nginx.service -o json

# 以 JSON 格式（多行）输出，可读性更好
$ sudo journalctl -b -u nginx.serviceqq
 -o json-pretty

# 显示日志占据的硬盘空间
$ sudo journalctl --disk-usage

# 指定日志文件占据的最大空间
$ sudo journalctl --vacuum-size=1G

# 指定日志文件保存多久
$ sudo journalctl --vacuum-time=1years
```

### 常见问题

#### 服务文件名中@代表什么意思，例如：name@.service?

“@”提示符是Systemd的一个高级功能，@可以被实际的参数替换。举一个例子可以更好的说明其作用：

通过 Docker 部署了MySQL和Nginx，假如我们需要为这两个应用增加service文件，正常的处理方式是写两个服务单元，但如果我们学会使用@的话，一个单元就可以搞定

```
#/etc/systemd/system/containers@.service

[Unit]
Description=Service %I in container
After=docker.service
Requires=docker.service

[Service]
Restart=always
ExecStart=/usr/bin/docker start -a %i
ExecStop=/usr/bin/docker stop %i
TimeoutStopSec=1m

[Install]
WantedBy=default.target
```

相比其他的.service文件，这个文件赫然有很多“%i” 参数。

下面两条命令就是使用此服务单元以及设置开机启动：

```
systemctl start container@mysql.service
systemctl enable contaner@mysql.service
```

可以，其类似于程序设计里面的类与对象的关系



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

## 认证

Linux认证指获得专业Linux培训后通过考试得到的资格。国际上广泛承认的Linux认证有LinuxProfessionalInstitute（简称为LPI）、SairLinux和GNU、Linux+和RedHatCertifiedEngineer。

以RedHat为例，主要的认证等级包括：

| 认证考试 | 认证培训课程编号               | 认证培训课程名称   |
| -------- | ------------------------------ | ------------------ |
| RHCSA    | RH124,RH135                    | 红帽认证系统管理员 |
| RHCE     | RH254                          | 红帽认证工程师     |
| RHCA     | RH401,RH436,RH423,RH442,RHS333 | 红帽认证架构师     |