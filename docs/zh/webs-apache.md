---
sidebarDepth: 3
---
# Apache

## 安装

### 安装Apache


```
# Installing on Fedora/CentOS/Red Hat Enterprise Linux
sudo yum install httpd
sudo systemctl enable httpd
sudo systemctl start httpd

# Installing on Ubuntu/Debian
sudo apt install apache2
sudo service apache2 start
```

### 安装Apache模块

## 工作模式

Apache工作模式有event,prefork,worker等单重

## 语言支持

### PHP

我们知道Apache被广泛用于PHP环境，Apache有两种PHP处理机制：

- php-fpm
- mod_php

### Java

## 配置

### 配置文件

主配置文件

```
/etc/httpd/conf/httpd.conf
```

扩展配置文件

```
1./etc/httpd/conf.d/*.conf
2.当Apache启动时，会加载/etc/httpd/conf.d/目录中的所有以.conf结尾的文件，做为配置文件来使用，所以管理员可以将配置推荐写在.conf中，如果将配置项写入主配置文件，系统升级时，配置项还要重新修改一遍，如果写在扩展配置项，则不存在此问题，同时也可以从繁杂的主配置文件中脱离出来。
```



### 配置说明

ServerTokens OS

```
系统信息,在访问出错时出现;把OS改为Minor,就不显示系统信息
```

ServerSignature On

```
把On改为Off就连普通的系统都给隐藏起来;改为Email就会显示管理员的邮箱(邮箱需要另外配置 ServerAdmin 
```

ServerAdmin root@localhost

```
管理员邮箱
```

ServerName localhost

```
服务器的主机名,一般是用虚拟机来设置,通常这个值是自动指定的，推荐显式的指定它以防止启动时出错
```

UseCanonicalName Off

```
设置为"On",Apache会使用ServerName指令的值
设置为 "Off"时,Apache会使用用户端提供的主机名和端口号。 
如果有虚拟主机，必须设置为Off
```

ServerRoot "/etc/httpd"

```
配置项的根目录，类似html里面的base;默认到这个路径里面找;
```

PidFile run/httpd.pid

```
进程PID,位置在 /etc/httpd/run/httpd.pid,主进程决定着子进程  
```

Timeout 60

```
若60秒后没有收到或送出任何数据就切断该连接
```

KeepAlive Off

```
是否开启持久化链接,访问网站时要对网站的很多资源,如css,js,image等等创建不同的链接;事实上我们可以建立一个持久化链接来应对多个请求;
```

MaxKeepAliveRequests 100

```
一个持久化链接最多能应对多少个请求
```

KeepAliveTimeout 15

```
15秒不链接就断开
```

Listen 80

```
监听端口,默认是80,一般不同改变;

如果要改变,注意以下几点:
1. 如果修改为192.168.1.22:8080,表示只能通过192.168.1.22:8080访问
2. 如果这里要更改为其他端口比如88的话,下面的ServerName localhost:88也得更改(如果是注释掉的,要取消注释)
3. 如果要监听多个端口,就多写几个Listen
```

Include conf.d/*.conf

```
扩展配置文件 /etc/httpd/conf.d/
我们一般在配置文件尾部再加上一句Include conf/vhosts/*.conf,把其他虚拟主机的配置分离开
```

User apache

```
Apache子进程所有者
```

Group apache

```
Apache子进程所属组
```

DirectoryIndex index.html index.html.var

```
默认主文件,
```

DocumentRoot "/var/www/html"

```
网站数据根目录。		
```

ErrorDocument 404 /404.html

```
创建404文件 echo ":) File Not Found!" >/var/www/html/404.html
404可以通过PHP程序来处理(在框架中),可以通过rewrite来处理,但是最理想的模式是让Apache来处理	
```

Directory

```
<Directory />
Options Indexes FollowSymLinks		
AllowOverride None
</Directory>

Directory /
定位目录 /(也就是Apache网站根目录)

Indexes
如果访问的文件不存在，显示目录文件列表；要禁止的话前面加上一个 - （-indexes）

FollowSymLinks	
在目录下创建a.html软链接，
ln -s /ab/index.html  /var/www/html/a.html
Options Indexes FollowSymLinks时软链接可用,可以直接在根目录下访问这个软连接
Options Indexes –FollowSymLinks软链接不可用

AllowOverride 
是否允许目录配置文件.htaccess有效ALL有效，None无效

Order allow，deny
Allow from all
deny from 192.168.1.106
↑↑ 先匹配allow允许，后匹配deny禁止，虽然192.168.1.106满足Allow，但deny是在allow后匹配的，所以192.168.1.106不允许访问

Order deny,allow
deny from all
allow from 192.168.1.106
↑↑ 只允许192.168.1.106访问
```

IfModule

```
如果存在模块mod_userdir.c

<IfModule mod_userdir.c> 
UserDir disabled       #句首加上#号,就表示开启家目录
#UserDir public_html   #设置家目录的文件夹,在此文件夹里面的文件可以访问得到,前提是有读写权限
</IfModule>

<Directory /home/*/public_html>
.*  #跟上面配合,设置可访问家目录的权限
</Directory>
```

### 配置注意事项

1.Apache对文件的操作就会用系统给的一个临时账号Apache作为第三方other来运行,所以要注意ugo的o的权限设置;

2.Apache的配置规则是 **后出现,先应用** 后面的出现的配置会覆盖前面的。

3.以上配置都应该在扩展配置里面覆盖更改或增加;

### 问题：关闭Apache Test Page 欢迎页面

### 问题：关闭缺省情况目录列表可查看

Apache httpd服务器在缺省的情况下，开启了基于目录列表的访问，这是一个存在安全隐患的问题，因此可以关闭这个功能。

## 伪静态

使用伪静态有三个步骤：

1. 确保Rewrite模块（apache模块配置文件：/etc/httpd/conf.modules.d/00-base.conf）已经被加载（去掉LoadModule rewrite_module modules/mod_rewrite.so前面的#）。
2. 虚拟主机配置文件中增加AllowOverride All
3. 网站根目录中增加.htaccess文件，并配置伪静态规则

### 场景：重定向

1. 开启Apache的rewrite模块
1. 在网站根目录中增加.htaccess文件
```shell

<IfModule mod_rewrite.c>
RewriteEngine On
Redirect 301 "/empirecmsall-image-guide" "/xdocs/empirecms-image-guide"
Redirect 301 "/wordpress-image-guide" "/xdocs/wordpressold-image-guide"

</IfModule>

```

### 场景：隐藏后缀名

```
<IfModule mod_rewrite.c>
RewriteRule ^test$ test.php
ErrorDocument 404 /404.txt

</IfModule>

```



## 虚拟主机
Apahce中的虚拟主机是通过VirtualHost进行配置的

### HTTP VirtualHost template

```
<VirtualHost *:80>
ServerName www.mydomain.com
ServerAlias other.mydomain.com
DocumentRoot "/data/wwwroot/zdoo"
ErrorLog "/var/log/httpd/www.mydomain.com_error_apache.log"
CustomLog "/var/log/httpd/www.mydomain.com_apache.log" common
<Directory "/data/wwwroot/zdoo">
Options Indexes FollowSymlinks
AllowOverride All
Require all granted
</Directory>
</VirtualHost>
```

### Apache Alias template

```
Alias /path /data/wwwroot/zdoo
<Directory "/data/wwwroot/zdoo">
Options Indexes FollowSymlinks
AllowOverride All
Require all granted
</Directory>
```

### Apache HTTPS VirtualHost template

```
<VirtualHost *:443>
ServerName  www.mydomain.com
DocumentRoot "/data/wwwroot/zdoo"
#ErrorLog "logs/www.mydomain.com-error_log"
#CustomLog "logs/www.mydomain.com-access_log" common
<Directory "/data/wwwroot/zdoo">
Options Indexes FollowSymlinks
AllowOverride All
Require all granted
</Directory>
SSLEngine on
SSLCertificateFile  /data/cert/www.mydomain.com.crt
SSLCertificateKeyFile  /data/cert/www.mydomain.com.key
SSLCertificateChainFile  /data/cert/root_bundle.crt
</VirtualHost>
```
### HTTP跳转HTTPS
#### 方案一：修改.htaccess文件
#### 方案二：修改vhost文件

要想开启自动跳转功能，请确保 Apache 的 Rewirte 模块加载，然后按照以下方案进行设置：
1. 整站跳转
    如果需要整站跳转，则在网站的配置文件（/etc/http/vhost/vhost.conf）的 \<Directory\> 标签内添加：
    
        
        RewriteEngine on
        RewriteCond %{SERVER_PORT} !^443$
        RewriteRule ^(.*)?$ https://%{SERVER_NAME}/$1 [L,R=301]
2. 只对某个目录的页面进行自动跳转，请将 **yourfolder** 改成自己的目录名 
    
        RewriteEngine on
        RewriteBase /yourfolder
        RewriteCond %{SERVER_PORT} !^443$
        #RewriteRule ^(.*)?$ https://%{SERVER_NAME}/$1 [L,R]
        RewriteRule ^.*$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R=301]
3. 只将带 www 的 URL 跳转至 HTTPS，请将 **www.yourdomain.com** 改成自己想要设置跳转的域名
    
        RewriteEngine On 
        RewriteRule ^/(.*)$ www.yourdomain.com/$1 [R=301]
4. 对除了某一个页面的其他所有页面进行 HTTPS 跳转

        RewriteEngine on 
        RewriteCond %{SERVER_PORT} !^443$ 
        RewriteCond %{REQUEST_URI} !^/tz.php 
        RewriteRule (.*) https://%{SERVER_NAME}/$1 [R]
    这段配置的作用是指除了 /tz.php 页面用 http 访问，其他页面均为 https 访问，/tz.php 可改为自己实际要 http 访问的后缀。



### 默认首页

默认访问目录之时，系统会自动根据顺序寻找列出的页面，并显示其中一个。
```
<VirtualHost *:80>
ServerName win.websoft9.com
<IfModule dir_module>
  DirectoryIndex index.hmtl defalut.html README.html readme.html about.html
</IfModule>
DocumentRoot "/data/wwwroot/default/site"
...
```
### 禁用IP访问,防止恶意解析
------------------------------------------------
1. 给指定网站程序设置域名
2.  将一下内容加入 `/etc/httpd/conf/httpd.conf` 的末尾或者在 `/etc/httpd/conf.d/` 目录下新建一个 `deny-ip.conf`的文件将内容写入
     ```
    <VirtualHost *:80>
       ServerName 服务器IP地址
       <Location />
            Order Allow,Deny
            Deny from all
       </Location>
     </VirtualHost>

    <VirtualHost *:443>
        ServerName 服务器IP地址
        SSLEngine on
        SSLCertificateFile /etc/pki/tls/certs/localhost.crt
        SSLCertificateKeyFile /etc/pki/tls/private/localhost.key
        <Location />
          Order Allow,Deny
          Deny from all
        </Location>
     </VirtualHost>
    ```
3. 重启 apache
    `systemctl restart httpd`

### 访问权限

## 代理

## 服务启停

```
#CentOS or Redhat
systemctl start httpd
systemctl stop httpd
systemctl restart httpd
systemctl status httpd

# Ubutnu
systemctl start apache2
systemctl stop apache2
systemctl restart apache2
systemctl status apache2
```

## 日志

Apache 访问日志在实际工作中非常有用，比较典型的例子是进行网站流量统计，查看用户访问时间、地理位置分布、页面点击率等。Apache 的访问日志具有如下4个方面的作用：

- 记录访问服务器的远程主机IP 地址，从而可以得知浏览者来自何处；
- 记录浏览者访问的Web资源，可以了解网站中的哪些部分最受欢迎；
- 记录浏览者使用的浏览器，可以根据大多数浏览者使用的浏览器对站点进行优化；
- 记录浏览者的访问时间；

## 缓存