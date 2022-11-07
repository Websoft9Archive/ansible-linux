# Linux-Desktop Cloud Installer

![](https://libs.websoft9.com/common/websott9-cloud-installer.png) 

## Introduction

[English](/README.md) | [简体中文](/README-zh.md)  

**Linux-Desktop Cloud Installer**, developed by [Websoft9](https://www.websoft9.com), is an automatic installation program of [Linux-Desktop](https://www.gnome.org/) based on Ansible and shell. It helps user install Linux-Desktop and pre-configure required items automatically and users only need to run a command on Linux. It simplifies the complicated installation and initialization process.  

## System Requirement

System Requirement to install this repository are as following：

| Conditions       | Details                               | Notes                |
| ------------------- | --------------------------------| -------------------- |
| Operating System   | CentOS7.x, Ubuntu20.04, Amazon Linux2 | Optional                 |
| Public Cloud     | AWS, Azure, Alibaba Cloud, HUAWEI ClOUD, Tencent Cloud    | Optional                 |
| Private Cloud     | KVM, VMware, VirtualBox, OpenStack    | Optional                 |
| Server Configuration | vCPU no less than 1 core, Memory no less than 1 GIB, Storage no less than 10 GB, Swap no less than 2GB |Bandwidth no less than 100M|

To learn more information, please view [Installation & Configuration](https://help.gnome.org/).

## Ecosystem

Core components of this repository:  GNOME, KDE, Xfce, Mate, VNC, Xrdp 

Learn more about [Parameters](/docs/stack-components.md).

## Installation

You can install it by thi Cloud Installer solution all in one. In addition, you can deploy image published on major Cloud Platform by Websoft9.

#### All-in-one Installer

Run the automatic installation script with **root** authority to start the installation. If necessary, users need to make interactive choices, and then wait patiently until the installation is successful.

```
$ sudo su -
$ wget -N https://raw.githubusercontent.com/Websoft9/ansible-linux/main/scripts/install.sh; bash install.sh -r linux
```

If the network is broken or blocked, SSH will be interrupted and the installation will fail. Please reinstall.

#### Image on Cloud 

Follow our [Linux-Desktop image](https://apps.websoft9.com/linux) for installation on major Cloud Platform.

## Documentation

**[Administrator Guide](https://support.websoft9.com/docs/linux)** 

## License

[LGPL-3.0](/License.md), Additional Terms: Without authorization from Websoft9, it is not allowed to publish free or paid image based on this program in any Cloud platform's Marketplace.

Copyright (c) 2016-present, Websoft9

This program provided by Websoft9 contains a series of software with separate copyright notices and license terms. Your use of the source code for the software included is subject to the terms and conditions of its own license.

## FAQ

#### How to install and view the latest release?

This repository install way is Package install, you can  view the version from [Official URL](https://github.com/GNOME/gnome-shell/tags).  
We will check [Release version](https://github.com/Websoft9/ansible-linux/releases) regularly. Update and test this project to ensure that users can successfully install the required version of Linux-Desktop.

#### Can I run this repository on Ansible Tower? 

Yes.

#### Although the results of the deploy by image are consistent with the results of deploy by script, what is the difference between the two deployment methods?

Suggest you read the document [Deploy by Image vs Deploy by Script](https://support.websoft9.com/docs/faq/bz-product.html#deployment-comparison).

