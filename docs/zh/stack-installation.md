# 初始化安装

在云服务器上部署了 AWX 镜像之后，请参考下面的步骤来使用它。

## 准备

1. 在云控制台获取您的 **服务器公网IP地址** 
2. 在云控制台安全组中，检查 **inbound（入）规则** 下的 **TCP:80** 端口是否开启
3. 如果您打算通过域名访问Metabase软件，请通过域名控制台完全一个域名解析（非必须）

## AWX 安装向导

1. 使用本地电脑的 Chrome 或 Firefox 浏览器访问网址：http://domain name 或 http://Internet IP, 就进入了软件的登录页面（[查看账号密码](/zh/stack-accounts.md)）
![AWX登录页面](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awx-login-websoft9.png)

2. 登录到AWX到管理界面
![AWX后台界面](https://libs.websoft9.com/Websoft9/DocsPicture/en/awx/awxui-websoft9.png)

3. 分别创建：Credentials,Inventories,Project，然后创建一个Template关联它们，就完成了一个自动化项目的配置

## 常见问题

#### 浏览器打开IP地址，无法访问AWX（白屏没有结果）？

您的服务器对应的安全组80端口没有开启（入规则），导致浏览器无法访问到服务器的任何内容

#### 第一次加载速度很慢？

是的，AWX加载的需要近一分钟，加载后运行流畅
