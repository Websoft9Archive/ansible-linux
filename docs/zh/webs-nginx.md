---
sidebarDepth: 3
---

# Nginx

[Nginx](http://nginx.org/)("engine x")是一款是由俄罗斯的程序设计师Igor Sysoev所开发高性能的Web和反向代理服务器，具有优异的静态资源处理能力，同时也是一个 IMAP/POP3/SMTP 代理服务器。在高连接并发的情况下，Nginx是Apache服务器不错的替代品。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/nginx/nginx-architecture-websoft9.png)

除了NGINX Open Source（即本文档所指的开源Web服务器），Nginx公司还有企业级的商业产品：  

* NGINX Plus  
* NGINX Controller  
* NGINX Unit  
* NGINX Amplify  
* NGINX WAF  

基于Nginx的著名开源项目：

* Tengine：由淘宝网发起的Web服务器项目。它在Nginx的基础上，针对大访问量网站的需求，添加了很多高级功能和特性。
* OpenResty：一个基于 Nginx 与 Lua 的高性能 Web 平台，其内部集成了大量精良的 Lua 库、第三方模块以及大多数的依赖项。用于方便地搭建能够处理超高并发、扩展性极高的动态 Web 应用、Web 服务和动态网关。

## 安装

安装Nginx有在线包安装和源码编译安装两种方式。其中在线安装通常称之为 yum/apt 安装，而源码安装即需要下载源码然后进行编译后方可使用。

相比源码编译安装来说，在线安装非常简单，下面是在线安装的范例：

```
# Fedora/CentOS/Red Hat
sudo yum install nginx
sudo systemctl enable nginx
sudo systemctl start nginx

# Ubuntu/Debian
sudo apt install nginx
sudo service nginx start
```

## 模块

安装模块之前，先查看当前已安装的所有模块，然后再决定是否安装，最后将已安装模块启用或停止。

### 查看

通过 `nginx -V` 命令可以查看已经安装的所有Nginx模块。  

```bash
~# nginx -V
nginx version: nginx/1.12.2
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: 
--prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --http-client-body-temp-path=/var/lib/nginx/tmp/client_body --http-proxy-temp-path=/var/lib/nginx/tmp/proxy --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi --http-scgi-temp-path=/var/lib/nginx/tmp/scgi --pid-path=/run/nginx.pid --lock-path=/run/lock/subsys/nginx --user=nginx --group=nginx --with-file-aio --with-ipv6 --with-http_auth_request_module --with-http_ssl_module --with-http_v2_module --with-http_realip_module --with-http_addition_module --with-http_xslt_module=dynamic --with-http_image_filter_module=dynamic --with-http_geoip_module=dynamic --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_random_index_module --with-http_secure_link_module --with-http_degradation_module --with-http_slice_module --with-http_stub_status_module --with-http_perl_module=dynamic --with-mail=dynamic --with-mail_ssl_module --with-pcre --with-pcre-jit --with-stream=dynamic --with-stream_ssl_module --with-google_perftools_module --with-debug --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic' --with-ld-opt='-Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -Wl,-E'
```

### 安装

### 启停


## 路径

不同的Linux发行版，对应的安装路径有一定的差异：

### CentOS

Nginx 虚拟主机配置文件：*/etc/nginx/conf.d/default.conf*  
Nginx 主配置文件： */etc/nginx/nginx.conf*  
Nginx 日志文件： */var/log/nginx*  
Nginx 伪静态规则目录： */etc/nginx/conf.d/rewrite*

### Ubuntu

Nginx 虚拟主机配置文件：*/etc/nginx/sites-available/default*  
Nginx 主配置文件：*/etc/nginx/nginx.conf*  
Nginx 日志文件：*/var/log/nginx/*


## 更新

## 请求处理机制

Nginx有三种可选的并行处理机制：多进程方式、多线程方式和异步方式

## 伪静态

使用伪静态有三个步骤：

1. 确保Rewrite模块（apache模块配置文件：/etc/httpd/conf.modules.d/00-base.conf）已经被加载（去掉LoadModule rewrite_module modules/mod_rewrite.so前面的#）。
2. 虚拟主机配置文件中增加AllowOverride All
3. 网站根目录中增加.htaccess文件，并配置伪静态规则

### 重定向

1. 开启Apache的rewrite模块
1. 在网站根目录中增加.htaccess文件
```shell

<IfModule mod_rewrite.c>
RewriteEngine On
Redirect 301 "/empirecmsall-image-guide" "/xdocs/empirecms-image-guide"
Redirect 301 "/wordpress-image-guide" "/xdocs/wordpressold-image-guide"

</IfModule>

```

### 隐藏后缀名

```
<IfModule mod_rewrite.c>
RewriteRule ^test$ test.php
ErrorDocument 404 /404.txt

</IfModule>

```



## VirtualHost配置

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

### 默认首页名称顺序

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

## 缓存

## 运行环境

Apache可以作为常见的开发语言的 Web 服务器，集成数据库、应用容器，最后形成一个完整的应用运行环境，例如：Apache+PHP，Apache+Tomcat+Java等

下面我们以常见的开发语言为例，分别介绍它们是如何与Apache一起工作的。

### PHP

Apache被广泛用于PHP环境，Apache有两种PHP处理机制：

- php-fpm：PHP内核中用来处理PHP文件的解释器和进程管理器
- mod_php：Apache的PHP处理模块

mod_php 作为Apache的模块，没有独立的进程，无需额外设置和处理，使用起来非常简单。

PHP-FPM(PHP FastCGI Process Manager)意：PHP FastCGI 进程管理器，用于管理PHP 进程池的软件，用于接受Apache HTTP Server等Web服务器的请求。PHP-FPM提供了更好的PHP进程管理方式，可以有效控制内存和进程、可以平滑重载PHP配置。  

下面是Apache+PHP-FPM共同工作的系统架构图，其中mod_proxy_fcgi用于Apache连接php-fpm

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/apache_event_php-fpm.jpg)

### Java

Apache HTTP Server 无法直接运行Java程序，而是与Tomcat一起组合去部署Java程序。

这种组合下，Apache处理静态资源，JSP等动态程序需转发给Tomcat处理，然后返回给用户。

Apache HTTP Server 与 Tomcat 最常见的连接方式是http_proxy，即利用 Apache 自带的 mod_proxy 模块使用代理技术来连接 Tomcat。 

http_proxy 模式是基于 HTTP 协议的代理，因此它要求 Tomcat 必须提供 HTTP 服务，也就是说必须启用 Tomcat 的 HTTP Connector。一个最简单的配置如下：

```
ProxyPass /images !
ProxyPass /css !
ProxyPass /js !
ProxyPass / http://localhost:8080/
```

更多请参考：[《Apache HTTP Server 与 Tomcat 的三种连接方式介绍》](https://www.ibm.com/developerworks/cn/opensource/os-lo-apache-tomcat/)

### Python

Apache HTTP Server 也可以用于Python环境，通过扩展模块mod_proxy_uwsgi，连接Python的uWSGI服务器或Gunicorn服务器，便可以解析Python程序。

这种组合的的基本配置方法如下：

1. 配置为uwsgi.ini
   ```
   [uwsgi]
   chdir = /home/vagrant/myweb/
   virtualenv = /home/vagrant/env/
   socket = 127.0.0.1:8080
   env = DJANGO_SETTINGS_MODULE=myweb.settings
   module =myweb.wsgi:application
   master = true
   processes = 4
   vacuum = True
   max-requests = 5000
   daemonize = /var/log/uwsgi.log
   pidfile = /var/log/uwsgi.pid
   ```
2. apache的配置文件加载mod_proxy_uwsgi.so
3. apache的配置文件反向代理到uwsgi
   ```
   ProxyPass / uwsgi://127.0.0.1:8080
   ```

### Node.js

Apache HTTP Server 也可以用于Node.js环境，Apache HTTP Server 与 Node.js 最常见的连接方式是http_proxy，即利用 Apache 自带的 mod_proxy 模块使用代理技术来连接 Node.js。   

下面是典型的配置文件范例：

```
server {
        listen 80 default_server;
        server_name _;


        location / {
         proxy_pass http://127.0.0.1:2368;
         proxy_set_header Host $host;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

}
```

### Ruby