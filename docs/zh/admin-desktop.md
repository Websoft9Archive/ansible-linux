# 桌面

Linux系统的桌面就是指类似Windows系统的图形化管理界面，一般来说Linux默认情况下并不会安装桌面，需要用户自主安装配置才可以使用。

* 主流的桌面有：GNOME, KDE, Unity  
* 连接桌面方式：VNC, Windows远程桌面

![ubuntu界面](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-ubuntuui-websoft9.png)

## 图形化登录

一般来说，可选的图形化登录方式有如下两种：

### VNC

VNC（Virtual Network Computing）是一种远程显示系统，使用VNC，您可以在远程计算机上运行图形应用程序，并且仅将显示内容从这些应用程序发送到本地计算机。VNC与平台无关，并且作为服务器和客户端都支持多种操作系统和体系结构。

[Websoft9](https://www.websoft9.com) 提供的图形化系统镜像，默认预装了 [TigerVNC](https://tigervnc.org)，且已设置开机自启的 vncserver 服务。

如下的命令可能会对你有帮助：

```
# 查看已经运行的桌面编号
vncserver -list

# 终止2号桌面进程
kill -9 :1

# 管理桌面服务
systemctl start vncserver@:1.service
systemctl stop vncserver@:1.service
systemctl status vncserver@:1.service
systemctl restart vncserver@:1.service
```

接下来，我们介绍如何通过本地电脑的VNC连接桌面：

1. 使用SSH登录服务器，设置你的VNC访问密码
    ```
    sudo su
    rm -rf /root/.vnc/passwd
    vncpasswd
    ```
2. 本地电脑安装 [VNC viewer](https://www.realvnc.com/download/viewer/)

3. 登录云控制台，为你的云服务器所在的安全组中开启 **5901** 端口

4. 打开VNC，创建一个VNC连接（服务器公网IP地址：5901）
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-connection001-websoft9.png)

5. 点击【Continue】进入下一步
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-connection002-websoft9.png)

6. 输入VNC密码后登录即可进入图形化界面
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-connection003-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-setlanguage-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-startuse-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-gnomehome-websoft9.png)

7. 如果服务器处于下图所示的锁定状态，请输入你的**服务器的密码**进行解锁
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-connection-rootlogin-websoft9.png)


### 远程桌面登录

CentOS 7.4 64位+GNOME图形化界面。请使用本机Windows自带的远程桌面工具登录即可

1. 打开本地电脑Windows的远程桌面工具，输入服务器公网IP开始连接
  ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-remoteip-websoft9.png)
2. 确认继续连接  
  ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-remotereminder-websoft9.png)
3. 根据提示，输入服务器root账号和密码
  ![enter image description here](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gnome/gnome-login-websoft9.png)
4. 成功登录
4. 修改语言（范例：中文），进入Setting->Region&Lanuage->Language,选择中文，根据系统提示重启后生效
  ![enter image description here](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gnome/gnome-changelanguage-websoft9.png)

## 常见问题

#### 不知道VNC密码？

输入如下的命令重置密码即可

```
vncpasswd
systemctl restart vnc
```

#### 图形化界面锁定状态是否支持秘钥解锁？

不支持

#### Gnome的开机Logo是否可以修改？

可以，甚至可以修改整套主题，具体参考[此处](https://www.dazhuanlan.com/2020/03/01/5e5ab2a1bd7d8/)

#### 预装的是哪个 VNC Server？

[TigerVNC](https://github.com/TigerVNC/tigervnc)

#### 采用远程桌面连接出现 "由于安全设置错误, 客户端无法连接到远程计算机.."  
![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-errorsafe-websoft9.png)

解决办法：

1. 打开"本地安全策略"- Win+R 并输入 secpol.msc (或者在"管理工具"中打开)；
2. 在本地安全策略中，打开“本地策略”下的“安全选项”；
3. 在右边的策略中，找到“系统加密：将FIPS算法用于加密 、哈希和签名”点击右键属性；
4. 将“本地安全设置”设置为“已禁用”，在单击“应用”，后”确定”，即可远程控制  
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/windows/windows-remoteanquan-websoft9.png)
