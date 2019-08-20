# Desktop

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

![image.png](https://cdn.nlark.com/yuque/0/2019/png/152462/1563094109592-7af08613-10af-46cf-9bec-593c6fb2d239.png#align=left&display=inline&height=325&name=image.png&originHeight=325&originWidth=488&size=24216&status=done&width=488)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/152462/1563094135476-46a57729-4ac0-45ae-b079-6df7fab051b2.png#align=left&display=inline&height=322&name=image.png&originHeight=322&originWidth=535&size=30488&status=done&width=535)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/152462/1563094602211-b0e87351-249b-4564-b99d-82c67bff4c78.png#align=left&display=inline&height=640&name=image.png&originHeight=640&originWidth=936&size=25602&status=done&width=936)

![image.png](https://cdn.nlark.com/yuque/0/2019/png/152462/1563094675125-dbf67597-e90c-4c5e-b364-f3525310e662.png#align=left&display=inline&height=624&name=image.png&originHeight=624&originWidth=933&size=334623&status=done&width=933)


### 常见问题

远程连接出现 "由于安全设置错误, 客户端无法连接到远程计算机. 确定你已登录到网络后.” 错误<br />
![image.png](https://cdn.nlark.com/yuque/0/2019/png/152462/1563094823763-1f3c0a0c-c4bd-43e3-b8b6-e3ef76a71a1b.png#align=left&display=inline&height=373&name=image.png&originHeight=373&originWidth=549&size=30947&status=done&width=549)

解决方法如下：

第一步：打开"本地安全策略"- Win+R 并输入 secpol.msc (或者在"管理工具"中打开)；<br />第二步：在本地安全策略中，打开“本地策略”下的“安全选项”；<br />           在右边的策略中，找到“系统加密：将FIPS算法用于加密 、哈希和签名”点击右键属性；<br />           将“本地安全设置”设置为“已禁用”，在单击“应用”，后”确定”，即可远程控制<br />![image.png](https://cdn.nlark.com/yuque/0/2019/png/152462/1563094860493-f2372b1b-7dca-4e76-b772-da8393bcd35d.png#align=left&display=inline&height=550&name=image.png&originHeight=550&originWidth=847&size=95285&status=done&width=847)