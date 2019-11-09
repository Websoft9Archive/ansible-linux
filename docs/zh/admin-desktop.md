# 桌面

## GNOME

CentOS 7.4 64位+GNOME图形化界面。请使用本机Windows自带的远程桌面工具登录即可

1. 打开本地电脑Windows的远程桌面工具，输入服务器公网IP开始连接
2. 根据提示，输入服务器root账号和密码
  ![enter image description here](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gnome/gnome-login-websoft9.png)
3. 成功登录到图形化界面
4. 修改语言（范例：中文），进入Setting->Region&Lanuage->Language,选择中文，根据系统提示重启后生效
  ![enter image description here](https://libs.websoft9.com/Websoft9/DocsPicture/zh/gnome/gnome-changelanguage-websoft9.png)

## Unity

如果是使用Ubuntu下的UNITY界面，务必使用Windows系统自带的远程桌面工具，参考如下登录

### 登录步骤

1. 打开本地电脑的远程桌面工具  
  ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-remoteip-websoft9.png)

2. 确认继续连接  
  ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-remotereminder-websoft9.png)

3. 输入服务器root账号和密码  
  ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-remoteroot-websoft9.png)

4. 登录到Ubuntu桌面  
  ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-ubuntuui-websoft9.png)


### 故障诊断

问题：远程连接出现 "由于安全设置错误, 客户端无法连接到远程计算机.."  
![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-errorsafe-websoft9.png)

解决办法：

1. 打开"本地安全策略"- Win+R 并输入 secpol.msc (或者在"管理工具"中打开)；
2. 在本地安全策略中，打开“本地策略”下的“安全选项”；
3. 在右边的策略中，找到“系统加密：将FIPS算法用于加密 、哈希和签名”点击右键属性；
4. 将“本地安全设置”设置为“已禁用”，在单击“应用”，后”确定”，即可远程控制  
   ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/zh/windows/windows-remoteanquan-websoft9.png)