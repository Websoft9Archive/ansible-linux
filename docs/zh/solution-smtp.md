## SMTP发送邮件

经过大量用户实践反馈，只推荐一种Metabase发邮件的方式，即安装邮件插件调用第三方邮件系统的STMP相关账号来进行邮件发送。

> 请忘掉在本机上安装sendmail等邮件服务器的方案，因为邮件系统的路由配置受制与域名、防火墙、路由等多种因素制约，导致不稳定、不容易维护、不好诊断问题。

通过插件发送邮件的具体操作如下：

1. 后台-设置-常规，设置好需要用于发件的邮件地址 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-mailcg-websoft9.png)
2. 安装SMTP插件：[WP Mail SMTP by WPForms](https://wordpress.org/plugins/wp-mail-smtp/)
3. 后台-设置-Email，配置WP Mail SMTTP 插件的参数（本配置以qq邮箱为例，请提前[开通邮箱的SMTP](http://service.mail.qq.com/cgi-bin/help?subtype=1&&no=166&&id=28)功能，并[获取授权码](http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256)） ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-mailconf-websoft9.png)
4. 填写参数后保存，然后最后输入一个收件地址用于测试是否可用，如果测试成功，会看到”Your email was sent successfully!”。如果邮件配置不可用，则会显示“There was a problem while sending the test email.”
 ![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/wordpress/wordpress-mailss-websoft9.png)
5. 测试成功，即邮件系统已经可用，所有的WordPress后台邮件发送就会使用这个配置

### 附：主流邮箱的STMP设置说明

QQ邮箱（mail.qq.com）
* SMTP服务器地址：smtp.qq.com（SSL端口：465或587）
* SMTP身份认证：必须勾选
* SMTP密码：密码不是邮箱密码，而是需要在SMTP服务页面上申请的一个授权码
* SMTP加密：需启用SSL
> 以上仅供快速参考，具体查看[官方SMTP](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=166)

　　   
网易邮箱（163.com）:
* SMTP服务器地址：smtp.163.com（SSL端口：465或994）
* SMTP身份认证：必须勾选
* SMTP密码：密码不是邮箱密码，而是需要在SMTP服务页面上申请的一个授权码
* SMTP加密：需启用SSL
> 以上仅供快速参考，具体查看[官方SMTP](http://help.163.com/09/1223/14/5R7P6CJ600753VB8.html?servCode=6010376)　　

阿里云邮箱（mail.aliyun.com）:
* SMTP服务器地址：smtp.mxhichina.com （SSL端口：465）
* SMTP身份认证：必须勾选
* SMTP密码：邮箱密码
* SMTP加密：需启用SSL
> 以上仅供快速参考，具体查看[官方SMTP](https://help.aliyun.com/knowledge_detail/36576.html)　