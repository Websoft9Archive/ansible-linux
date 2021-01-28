---
sidebarDepth: 3
---

# 包和仓库

Linux生态中的软件包资源非常丰富，从某种程度上看，用户是否熟练的下载安装以及更新这些包，决定了能够为所在的企业创作的价值的大小。

除了传统的下载源码在编译的软件包安装方案之外，Linux 操作系统都提供了一个集中的软件包管理机制，即搜索、安装和管理软件包。 Linux 软件包的基本组成部分通常有：共享库、应用程序（二进制）、服务和文档。从另外一个角度看，包文件通常包含编译好的二进制文件和其它资源组成的：软件、安装脚本、元数据及其所需的依赖列表。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-rpms-websoft9.png)

包管理通常不仅限于软件的一次性安装，还包括了对已安装软件包进行升级的工具。

* 包：被安装到本地服务器的软件安装包，例如Apache安装包
* 包缓存：安装软件时在本地保存的临时文件，通常存储在 */var/cache/yum* 目录下
* 仓库：存放多个软件包的一个远端服务器
* 仓库地址：用于访问仓库的网址
* 本地安装包缓存：本地已经下载的软件缓存，通常存储在 */var/lib/rpm* 目录下，可以通过 `rpm -`
* 本地存储的软件清单：从仓库下载所有的软件清单并存在在本地，可以通过`yum list`检索

本章主要讨论和研究Linux系统的包管理机制、实践方案。

## 仓库

多个软件包存储在一个集中位置，就称之为仓库「repository」，这种以仓库方式集中存放，有利于软件开发者或包维护者进行管理。

仓库的网址，称之为仓库地址，专业术语叫”源”。

互联网上有大量的源，比如 Redhat 官方的源，也有云厂家提供的源。在配置 Linux 服务器或开发环境时，通常都不仅限于使用官方源。相较于现如今软件版本快速更新迭代而言，系统管理员和开发人员掌握常见 Linux 包管理基本操作还是一项必备的常用技能。

每个操作系统发行版厂家从商业战略的角度，会直接维护或间接维护多个仓库，以实现其分级服务和规避责任的目的。

例如：CentOS 可用的几个仓库有：

* 官方仓库
* SCL仓库
* IUS仓库

官方仓库中的软件包理论上最稳定可靠，其他仓库作为辅助。  

与此同时，官方为了吸引用户贡献包，也会提供最简单的工具（[copr 项目](https://copr.fedorainfracloud.org/)），让用户专注于包配置（sepc文件）方面的工作，而构建编译和托管由平台负责，就可以充分利用社区力量，让仓库的软件变得异常丰富。

仓库越来越多，自然就诞生了跨仓库的搜索引擎，类似 [pkgs](https://pkgs.org/) 便可以检索主流的仓库的包，节省了用户寻找的时间。

### 仓库源

下面我们列出全球比较流行的仓库：

|  名称  | 地址 |             概要              |
| :----: | :--: | :---------------------------: |
| RPM Fusion | https://rpmfusion.org/ | RPM Fusion provides software that the Fedora Project or Red Hat doesn't want to ship. That software is provided as precompiled RPMs for all current Fedora versions and current Red Hat Enterprise Linux or clones versions;  |
| EPEL | https://fedoraproject.org/wiki/EPEL | EPEL (Extra Packages for Enterprise Linux), 是由 Fedora Special Interest Group 维护的 Enterprise Linux（RHEL、CentOS）中经常用到的包。 |
| RepoForge | http://repoforge.org/ |Repoforge 是 RHEL 系统下的软件仓库，拥有 10000 多个软件包，被认为是最安全、最稳定的一个软件仓库。|
| Remi | https://www.remi.com |Remi repository 是包含最新版本 PHP 和 MySQL 包的 Linux 源，由 Remi 提供维护。|
| PackMan | http://packman.links2linux.org/ | Packman 是 OpenSUSE 最大的第三方软件源，主要为 OpenSUSE 提供额外的软件包，包括音视频解码器、多媒体应用、游戏等。 |
| Dotdeb | http://www.debian.org/ | Dotdeb is an extra repository providing up-to-date packages for your Debian 8 “Jessie” servers .|
| Gentoo portage | https://www.gentoo.org | Gentoo Portage 软件源 |
| Fedora altarch | https://archives.fedoraproject.org/pub/ | Fedora altarch 是 Fedora Linux 额外平台的安装镜像和官方软件包仓库。 |
| Ubuntu Ports | http://ports.ubuntu.com | Ubuntu Ports 是 Arm64，Armhf 等平台的 Ubuntu 软件仓库 |
| Centos altarch | http://mirror.centos.org/altarch/ | CentOS 额外平台的安装镜像和官方软件包仓库 |
| IUS | https://ius.io/ | IUS（Inline with Upstream Stable）是一个社区项目，它旨在为 Linux 企业发行版提供可选软件的最新版 RPM 软件包。 |

以上是"大卖场"式的仓库源，实际上很多知名的开源软件，例如：MySQL,Apache等还提供自建的仓库，供用户使用。

* [MySQL repo](https://dev.mysql.com/downloads/repo/yum/)
* [Nginx repo](http://nginx.org/en/linux_packages.html#RHEL-CentOS)

下图是MySQL官方的仓库文件下载页面，*mysql80-community-release-el8-1.noarch.rpm*这种文件就是用户安装仓库地址的rpm包。

![repo mysql](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/repo-mysql-websoft9.png)

### 安装仓库

安装仓库通俗的讲，就是将仓库的网址（地址）信息写入到服务器的指定文件夹（文件）中。类似我们为了方便自己购物，将不同的购物网站的网站收藏到浏览器是一个道理。

* CentOS仓库网址存放地：/etc/yum.repos.d
* Ubuntu仓库网址存放地：/etc/apt/sources.list

以CentOS仓库为例，查看 */etc/yum.repos.d* 目录，我们会发现下面有几个以 repo 结尾的文件

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/repo-list-websoft9.png)

打开每个.repo文件，你会看到其中的主要信息就是网址

那这些.repo文件是如何被安装的呢？主要有如下几种方式：

```
#1 yum 安装
yum install epel-release

#2 下载 RPM包安装

wget -O /etc/yum.repos.d/epel.repo https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -i epel-release-latest-7.noarch.rpm

#3 直接在 /etc/yum.repos.d 新增一个.repo文件，内容如下

[rpmfusion-free]
name=RPM Fusion for Fedora $releasever - Free
baseurl=https://mirrors.tuna.tsinghua.edu.cn/rpmfusion/free/fedora/releases/$releasever/Everything/$basearch/os/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-$releasever&arch=$basearch
enabled=1
metadata_expire=7d
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever-$basearch

[rpmfusion-free-debuginfo]
name=RPM Fusion for Fedora $releasever - Free - Debug
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-debug-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever-$basearch

[rpmfusion-free-source]
name=RPM Fusion for Fedora $releasever - Free - Source
baseurl=https://mirrors.tuna.tsinghua.edu.cn/rpmfusion/free/fedora/releases/$releasever/Everything/source/SRPMS/
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-fedora-source-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever-$basearch
```

我们知道仓库网址上有一个特殊的**数据库**文件（软件列表），这个文件记录这个网址所提供的所有安装包，有的仓库只有少数几个安装包，有的仓库提供成千上万个安装包。

同时本地也有一个**数据库**文件（RPM 数据库 ），它记录本地已经安装的软件包名称、版本、来源等信息。当用户使用yum安装软件的时候，本地就会到仓库中下载软件列表，通过与本地的RPM数据库做对比，然后决定是否安装或提示已经存在无需安装。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/installwithyum-websoft9.jpg)


### 自建仓库

在安装MySQL的时候，我们就发现，MySQL官方提供了自己的仓库以供用户使用。也就意味着，仓库是可以自行建设的。

参考：[《配置本地Yum仓库》](https://www.runoob.com/linux/linux-yum.html)


## 管理包

虽然大多数流行的 Linux 发行版在包管理工具、方式和形式都大同小异，但却还是有平台差异：

|  系统  | 格式 |             工具              |
| :----: | :--: | :---------------------------: |
| Debian | .deb | apt, apt-cache、apt-get、dpkg |
| Ubuntu | .deb | apt、apt-cache、apt-get、dpkg |
| CentOS | .rpm |              yum              |
| Fedora | .rpm |              dnf              |

下图是典型的deb包组成部分：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/DEB-Package-Format.png)

Debian 及其衍生产品如：Ubuntu、Linux Mint 和 Raspbian 的包格式为.deb文件，apt 是最常见包操作命令，可：搜索库、安装包及其依赖和管理升级。而要直接安装现成.deb包时需要使用dpkg命令。

CentOS、Fedora 及 Red Hat 系列 Linux 使用RPM包文件，并使用yum命令管理包文件及与软件库交互。

在最新的 Fedora 版本中，yum命令已被dnf取代进行包管理。


### 更新本地数据库

大多数 Linux 都使用本地数据库来存储远程可用的包仓库列表，所以在安装或升级包之前最好更新（同步）一下这个数据库。

|      系统       |        命令         |
| :-------------: | :-----------------: |
| Debian / Ubuntu | sudo apt-get update |
|     CentOS      |  yum check-update   |
|     Fedora      |  dnf check-update   |

### 升级已安装的包

在没有包管理方式时，要升级并保持 Linux 已装软件处在最新版本上是一个巨大的工程，管理员和用户不得不手动跟踪上游软件版本变化及安全警告。在有了包管理系统之后，只需几条命令便可保持软件最新。

|      系统       |           命令            |                 备注                 |
| :-------------: | :-----------------------: | :----------------------------------: |
| Debian / Ubuntu |   sudo apt-get upgrade    |         仅升级已安装的软件包         |
|                 | sudo apt-get dist-upgrade | 可添加或删除程序包，以满足新的依赖。 |
|     CentOS      |      sudo yum update      |                                      |
|     Fedora      |     sudo dnf upgrade      |                                      |

### 查找/搜索软件包

大多数 Linux 桌面版本都提供用户可搜索和安装软包的界面，这是找寻和安装软件的最佳方法。但对于追求效率和服务器管理员来说，使用命令行工具查找/搜索软件包才是正途。

|      系统       |           命令            |            备注            |
| :-------------: | :-----------------------: | :------------------------: |
| Debian / Ubuntu | apt-cache search 搜索内容 |                            |
|     CentOS      |    yum search 搜索内容    |                            |
|                 |  yum search all 搜索内容  | 搜索所有内容，包括包描述。 |
|     Fedora      |    dnf search 搜索内容    |                            |
|                 |  dnf search all 搜索内容  | 搜索所有内容，包括包描述。 |

### 查看某个软件包信息

在决定安装哪个包之前，我们往往都需要查看该软件包的详细说明。包的说明文件中通常包括：包名、版本号及依赖列表等元数据，可以使用如下命令来查看。

|      系统       |             命令             |             备注             |
| :-------------: | :--------------------------: | :--------------------------: |
| Debian / Ubuntu |     apt-cache show 包名      | 显示有关软件包的本地缓存信息 |
|                 |         dpkg -s 包名         |     显示包的当前安装状态     |
|     CentOS      |        yum info 包名         |                              |
|                 |       yum deplist 包名       |         列出包的以来         |
|     Fedora      |        dnf info 包名         |                              |
|                 | dnf repoquery –requires 包名 |         列出包的以来         |


```
# 通过 rpm 命令查看已安装软件包的信息
$ rpm -qi rabbitmq-server
Name        : rabbitmq-server
Version     : 3.8.3
Release     : 1.el7
Architecture: noarch
Install Date: Sat 11 Apr 2020 03:16:18 PM CST
Group       : Development/Libraries
Size        : 14010653
License     : MPLv1.1 and MIT and ASL 2.0 and BSD
Signature   : RSA/SHA256, Mon 09 Mar 2020 11:24:36 PM CST, Key ID 6b73a36e6026dfca
Source RPM  : rabbitmq-server-3.8.3-1.el7.src.rpm
Build Date  : Mon 09 Mar 2020 11:24:34 PM CST
Build Host  : b0cb34e7-576c-46ec-669f-7b518b2352e1
Relocations : (not relocatable)
URL         : https://www.rabbitmq.com/
Summary     : The RabbitMQ server
Description :
RabbitMQ is an open source multi-protocol messaging broker.

# 通过 rpm 查看未安装的软件包的信息
$ rpm -qpi rabbitmq-server

# 通过 yum 查看软件包信息
$ yum info rabbitmq-server
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
Installed Packages
Name        : rabbitmq-server
Arch        : noarch
Version     : 3.8.3
Release     : 1.el7
Size        : 13 M
Repo        : installed
From repo   : rabbitmq_rabbitmq-server
Summary     : The RabbitMQ server
URL         : https://www.rabbitmq.com/
License     : MPLv1.1 and MIT and ASL 2.0 and BSD
Description : RabbitMQ is an open source multi-protocol messaging broker.
```

### 从软件仓库安装包

一旦我们知道某个软件包的名称之后，便可以使用如下命令从软件仓库安装包。

|      系统       |              命令              |       备注       |
| :-------------: | :----------------------------: | :--------------: |
| Debian / Ubuntu |   sudo apt-get install 包名    |                  |
|                 | sudo apt-get install 包1 包2 … | 安装所有列出的包 |
|                 |  sudo apt-get install -y 包名  | 无需提示直接安装 |
|     CentOS      |     sudo yum install 包名      |                  |
|                 |   sudo yum install 包1 包2 …   | 安装所有列出的包 |
|                 |    sudo yum install -y 包名    | 无需提示直接安装 |
|                 |    yum install yum-plugin-downloadonly  包名    | 只下载包而不安装 |
|                 |    sudo yumdownloader 包名    | 下载包到当前目录 |
|     Fedora      |     sudo dnf install 包名      |                  |
|                 |   sudo dnf install 包1 包2 …   | 安装所有列出的包 |
|                 |    sudo dnf install -y 包名    | 无需提示直接安装 |

### 从本地文件系统直接安装包

很多时候，我们在进行测试或从某个地方直接拿到软件包之后需要从本地文件系统直接安装包。Debian 及衍生系统可以使用 **dpkg** 进行安装，CentOS 和 Fedora 系统使用 **yum** 和 **dnf** 命令进行安装。

|      系统       |                        命令                         |            备注             |
| :-------------: | :-------------------------------------------------: | :-------------------------: |
| Debian / Ubuntu |                sudo dpkg -i 包名.deb                |                             |
|                 | sudo apt-get install -y gdebi&& sudo gdebi 包名.deb | 使用gdebi检索缺少的依赖关系 |
|     CentOS      |              sudo yum install 包名.rpm              |                             |
|     Fedora      |              sudo dnf install 包名.rpm              |                             |

### 移除已安装的包

包管理器知道哪些文件是由哪个包提供的，所以卸载不需要的软件包之后可以获得一个干净的系统。

|      系统       |           命令           |          备注          |
| :-------------: | :----------------------: | :--------------------: |
| Debian / Ubuntu | sudo apt-get remove 包名 |                        |
|                 | sudo apt-get autoremove  | 自动移除已知不需要的包 |
|     CentOS      |   sudo yum remove 包名   |                        |
|     Fedora      |   sudo dnf erase 包名    |                        |

### 锁定软件包版本

有些时候，我们在对系统进行更新操作时，不需要对某些软件包进行升级操作，要把该包锁定在某个特定版本下。这个时候我们就需要用到相关的插件，以yum为例：

```
yum install yum-plugin-versionlock
```

安装 **yum-plugin-versionlock** 之后，系统新增一个配置文件：*/etc/yum/pluginconf.d/versionlock.list*  

可以直接编辑此文件，往其中添加锁定项，也可以通过下面的命令添加锁定项
```
yum versionlock gcc-*

```
上述配置不允许将gcc软件包升级到大于执行锁定时安装的软件包的版本。

## 制作包

我们知道 rpm/deb 包都是存储在仓库中的可以运行的包，使得我们安装软件非常的简单和方便。  

如果我们需要安装的软件，在互联网上找不到对应的包，怎么办？通常的做法是下载源码编译安装。

编译安装可以解决我们自身安装软件的问题，但我们无法给他人共享我们的安装成功，因此我们如果可以自己制作 rpm/deb 包，然后发布到互联网上，一定有很多人下载，这样分享自己的创作成果毫无疑问会得到极大的收获和鼓舞。

下面我们以 RPM 包为例，详细介绍制作过程（[参考来源](https://rpm-packaging-guide.github.io/)）。

### 知识

**安装颗粒度**

与安装相关的技术知识颗粒度由小到大分别为：Make 编译 > RPM 包制作 > 包仓库建设。  
颗粒度越大，受惠的人群越广。  

**spec 文件**

Spec 文件是 RPM 包的编排文件，简单理解为制作脚本，它是制作 RPM 包最核心的内容。  

下面是一个简单的 Spec 文件（假设名称为 hello.spec）：

```
Name:       hello-world
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME

%description
This is my first RPM package, which does nothing.

%prep
# we have no source, so nothing here

%build
cat > hello-world.sh <<EOF
#!/usr/bin/bash
echo Hello world
EOF

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello-world.sh %{buildroot}/usr/bin/hello-world.sh

%files
/usr/bin/hello-world.sh

%changelog
# let's skip this for now
```

将以上文件的内容保存到 Spec 文件后，运行如下的命令，便完成一个 RPM 包的制作。
```
rpmdev-setuptree
rpmbuild -ba hello.spec
```

通过 `tree` 命令查询安装结果：
```
$ tree rpmbuild
rpmbuild
|-- BUILD
|   `-- hello-world.sh
|-- BUILDROOT
|-- RPMS
|   `-- x86_64
|       `-- hello-world-1-1.x86_64.rpm
|-- SOURCES
|-- SPECS
`-- SRPMS
    `-- hello-world-1-1.src.rpm

7 directories, 3 files

```

从以上的范例，可以直接得出几个坚定的结论：

* RPM 包制作中的 Build 不一定是编译，它也可以是其他动作，例如：拷贝一个文件
* RPM 包名称会根据描述信息自动名词，非常规范，可读性也很好
* 生成 RPM 包的同时，也会生成一个 SRPM 包
* Spec 语法基本就是 Shell 语法
* 依赖组件不是必须的

**Makefile**

Makefile 顾名思义是 `make` 时所需的一个编排文件，如果用不着 `make`，那么 Makefile 也就不需要。

> 关于 Make 命令，参考官方文档：[GNU Make](https://www.gnu.org/software/make/)

**交叉编译**


## 工具

在云计算发展的今天，包管理丰富多彩。在实践中，有一些非常好用好玩的工具：

* packagecloud.io: 提供包管理托管的网站，范例参考：[RabbitMQ on packagecloud](https://packagecloud.io/rabbitmq/rabbitmq-server/)
* 软件分发即服务：https://bintray.com/
* C/C++编译工具: https://conan.io/
* 包检索工具：https://pkgs.org/

## 按发行版

下面总结主流 Linux 发行版上的包管理相关的独特性

### RedHat

RedHat 系统免费，但是仓库需要订阅。  

下面重点介绍 RedHat 如何使用 CentOS-base 仓库的方案

### CentOS

CentOS 是 RedHat 的同步办法，完全免费。

### Ubuntu

### OracleLinux

[OracleLinux](http://yum.oracle.com/) 是 RedHat 家族的分支，与 CentOS 非常类似，但完全基于 RedHat 内核。  

```
[root@iZj6c6izdnwbwt5jb0i2r0Z ~]# cat /proc/version
Linux version 4.14.35-1902.305.4.el7uek.x86_64 (mockbuild@jenkins-10-147-72-125-9cc530f8-159f-444e-98e9-d1e5d2b5e4e2) (gcc version 4.8.5 20150623 (Red Hat 4.8.5-16.0.3) (GCC)) #2 SMP Tue Aug 4 14:17:05 PDT 2020

```

OracleLinux 非常注重打造自己的生态，官方提供了大量在线安装包，并用心维护，基本能够方便用户快速的安装主流软件。

运行命令 `yum list *release-el7` 查看所有可用的源：

```
mysql-release-el7.x86_64                                           1.0-3.el7                          ol7_latest
oracle-ceph-release-el7.x86_64                                     1.0-2.el7                          ol7_latest
oracle-epel-release-el7.x86_64                                     1.0-3.el7                          ol7_latest
oracle-gluster-release-el7.x86_64                                  1.0-6.el7                          ol7_latest
oracle-golang-release-el7.x86_64                                   1.0-6.el7                          ol7_latest
oracle-nodejs-release-el7.x86_64                                   1.0-5.el7                          ol7_latest
oracle-olcne-release-el7.x86_64                                    1.0-5.el7                          ol7_latest
oracle-openstack-release-el7.x86_64                                1.0-2.el7                          ol7_latest
oracle-ovirt-release-el7.x86_64                                    1.0-1.el7                          ol7_latest
oracle-php-release-el7.x86_64                                      1.0-4.el7                          ol7_latest
oracle-release-el7.x86_64                                          1.0-3.el7                          ol7_latest
oracle-softwarecollection-release-el7.x86_64                       1.0-3.el7                          ol7_latest
oracle-spacewalk-client-release-el7.x86_64                         1.0-4.el7                          ol7_latest
oracle-spacewalk-server-release-el7.x86_64                         1.0-4.el7                          ol7_latest
oraclelinux-developer-release-el7.x86_64                           1.0-5.el7                          ol7_latest
oraclelinux-release-el7.x86_64                                     1.0-12.1.el7                       ol7_latest
```

### AmazonLinux

AmazonLinux 官方对其发行版的性质描述非常少，似乎刻意回避。实际上，AmazonLinux 也是 RedHat 家族的分支，非常类似 CentOS。  

经过实践探索，CentOS 相关的仓库（例如：CentOS-base.repo）也是可以在 AmazonLinux 上使用的。  

值得注意的是，AmazonLinux 默认的源会设置优先级（priority=10），导致 yum 无法自主灵活的选择其他仓库的安装包。  

* amzn2-extras.repo
* amzn2-core.repo

所以，建议删除以上两个官方默认仓库的优先级设置，把安装的自主权交还给 yum。


## 常见问题

#### 下载的RPM包中可否包含其他RPM包的依赖地址？

可以，这是很常见的场景

#### 仓库文件(例如：/etc/yum.repos.d/docker-ce.repo) 是仓库的最小单元吗？

不是，最小单元是文件中的每个[]维护的信息：

```
[docker-ce-stable]
name=Docker CE Stable - $basearch
baseurl=https://download.docker.com/linux/centos/7/$basearch/stable
enabled=1
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg
```

实际上，我们可以把 /etc/yum.repos.d 下所有的文件合并成一个文件

#### yum install 如何排除某个仓库？

运行如下的命令，参数 --disablerepo 的值是 repo 文件中仓库单元的名称，不是 repo 文件的名称。

```
yum install docker --disablerep="docker-ce-stable"
```

#### yum 安装时 priority=* 的逻辑？

优先级设置是双刃剑：

* priority=10 优先级低于 priority=9，即数字越小优先级高
* 依赖会从优先级较高的仓库中寻找：如果找到的版本不匹配，系统就会报错；如果找不到所需的软件，系统会从优先级较低的仓库中继续寻找
* 优先级设置会导致依赖的安装难以匹配最佳

#### rpm -ivh ×××.rpm 和yum install ×××.rpm 安装命令有什么区别？

rpm 安装只针对单个rpm文件安装，不会安装相关的依赖；yum install 安装会安装rpm包以及所需的依赖

#### .noarch.rpm 和 .x64_64.rpm 包有什么区别？

.noarch 是通用的rpm包，其中没有二进制文件和库文件，就是说与服务器硬件和操作系统版没有太大的关系，通常用于安装一个脚本或仓库地址  
.x64_64 是包含二进制等文件的安装包，与服务器CPU类型有关，通常用于安装某个软件  

#### 在两个仓库中存在通一个软件包，yum/apt如何处理其中的优先级关系？

Linux 发行版比较多，同时还有很多个人或组织维护了某些特定用途的安装/升级源。Yum Priorities 插件可以用来强制保护源。它通过给各个源设定不同的优先级，使得系统管理员可以将某些源（比如 Linux 发行版的官方源）设定为最高优先级，从而保证系统的稳定性（同时也可能无法更新到其它源上提供的软件最新版本）。

1. 安装优先级插件
    ```
    rpm -q yum-priorities
    ```
2. 编辑 /etc/yum.repos.d/目录下的*.repo 文件来设置优先级
    ```
    [base]
    name=CentOS-$releasever – Base
    baseurl=http://mirror.centos.org/centos/$releasever/os/$basearch/
    gpgcheck=0
    priority=1
    ```

#### 本地的rpm/deb数据库中是否包含已安装的软件的仓库来源地址？

#### 如何查看软件所需的依赖？

以RabbitMQ为例，命令以及结果如下：
```
[root@iZ8vb7it5p19lxxol367u0Z rpm]# yum deplist rabbitmq-server
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
package: rabbitmq-server.noarch 3.8.3-1.el7
  dependency: /bin/sh
   provider: bash.x86_64 4.2.46-33.el7
  dependency: /usr/bin/env
   provider: coreutils.x86_64 8.22-24.el7
  dependency: config(rabbitmq-server) = 3.8.3-1.el7
   provider: rabbitmq-server.noarch 3.8.3-1.el7
  dependency: erlang >= 21.3
   provider: erlang.x86_64 22.3.2-1.el7
  dependency: logrotate
   provider: logrotate.x86_64 3.8.6-17.el7
  dependency: socat
   provider: socat.x86_64 1.7.3.2-2.el7
  dependency: systemd
   provider: systemd.x86_64 219-67.el7_7.4
```

> yum deplist 命令与被查询的软件包是否安装没有关系，即没有被安装的软件包也可以查询其依赖


#### yum list 获取是软件清单是实时的还是缓存？

#### 如何解压 rpm 包？

#### 什么是 SCL 源？

SoftwareCollections.org 是为 Red Hat Enterprise Linux，Fedora，CentOS 和 Scientific Linux 创建软件集合（SCL）的项目的所在地。您可以在此处创建和托管软件集合，以及与管理 SCL 的开发者建立联系。SCL 是在保证不与原有软件冲突的情况下运行的，也就意味着用户默认 Bash 是无法调用 ，如果想开机自动调用 SCL， 需要设置好环境变量。

#### 什么是 IUS 源？

IUS is a community project that provides RPM packages for newer versions of select software for Enterprise Linux distributions.IUS只为RHEL和CentOS这两个发行版提供较新版本的rpm包。如果在os或epel找不到某个软件的新版rpm，软件官方又只提供源代码包的时候，可以来ius源中找，几乎都能找到。

#### 什么是 https://buildlogs.centos.org/？

This server contains a mix of raw/unsigned packages and/or build logs
It should be used mainly for testing purposes



