---
sidebarDepth: 3
---

# 包管理

Linux 操作系统都提供了一个集中的软件包管理机制，即搜索、安装和管理软件包。 Linux 软件包的基本组成部分通常有：共享库、应用程序、服务和文档。从另外一个角度看，包文件通常包含编译好的二进制文件和其它资源组成的：软件、安装脚本、元数据及其所需的依赖列表。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-rpms-websoft9.png)

包管理通常不仅限于软件的一次性安装，还包括了对已安装软件包进行升级的工具。

## 仓库

多个软件包存储在一个集中位置，就称之为仓库「repository」，这种以仓库方式集中存放，有利于软件开发者或包维护者进行管理。

仓库的网址，称之为仓库地址，专业术语叫”源”。

互联网上有大量的源，比如Redhat官方的源，也有云厂家提供的源。在配置 Linux 服务器或开发环境时，通常都不仅限于使用官方源。相较于现如今软件版本快速更新迭代而言，系统管理员和开发人员掌握常见 Linux 包管理基本操作还是一项必备的常用技能。

本节内容主要来源[此处](https://www.sysgeek.cn/linux-package-management/)

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



### 更新本地包数据

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

包文件是如何制作并发布到包仓库的呢？

## 工具

在云计算发展的今天，包管理丰富多彩。在实践中，有一些非常好用好玩的工具：

* packagecloud.io: 提供包管理托管的网站，范例参考：[RabbitMQ on packagecloud](https://packagecloud.io/rabbitmq/rabbitmq-server/)
* https://bintray.com/

## 常见问题

#### 下载的RPM包中可否包含其他RPM包的依赖地址？

可以，这是很常见的场景

#### rpm和yum安装命令有什么区别？