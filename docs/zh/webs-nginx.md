---
sidebarDepth: 3
---

# Nginx

以Nginx在云服务器上最常见的应用场景为切入点，结合具体的操作，让没有基础的用户也能够快速上手。

Nginx公司还有企业级的商业产品：
NGINX Plus
NGINX Controller
NGINX Unit
NGINX Amplify
NGINX WAF

## 安装

安装Nginx有在线安装和源码编译安装两种方式，在线安装通常称之为yum安装，源码安装即需要下载源码然后进行编译后方可使用。

在线安装非常简单，下面是在线安装的范例：

```
# Installing on Fedora/CentOS/Red Hat Enterprise Linux
sudo yum install httpd
sudo systemctl enable httpd
sudo systemctl start httpd

# Installing on Ubuntu/Debian
sudo apt install apache2
sudo service apache2 start
```

## 模块

Nginx是模块化的设计，安装模块：

### 安装模块

```
# Installing on Fedora/CentOS/Red Hat Enterprise Linux


# Installing on Ubuntu/Debian

```

### 查询模块

```bash
~# nginx -V
nginx version: nginx/1.12.2
built by gcc 4.8.5 20150623 (Red Hat 4.8.5-16) (GCC)
built with OpenSSL 1.0.2k-fips  26 Jan 2017
TLS SNI support enabled
configure arguments: 
--prefix=/usr/share/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib64/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --http-client-body-temp-path=/var/lib/nginx/tmp/client_body --http-proxy-temp-path=/var/lib/nginx/tmp/proxy --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi --http-scgi-temp-path=/var/lib/nginx/tmp/scgi --pid-path=/run/nginx.pid --lock-path=/run/lock/subsys/nginx --user=nginx --group=nginx --with-file-aio --with-ipv6 --with-http_auth_request_module --with-http_ssl_module --with-http_v2_module --with-http_realip_module --with-http_addition_module --with-http_xslt_module=dynamic --with-http_image_filter_module=dynamic --with-http_geoip_module=dynamic --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_random_index_module --with-http_secure_link_module --with-http_degradation_module --with-http_slice_module --with-http_stub_status_module --with-http_perl_module=dynamic --with-mail=dynamic --with-mail_ssl_module --with-pcre --with-pcre-jit --with-stream=dynamic --with-stream_ssl_module --with-google_perftools_module --with-debug --with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic' --with-ld-opt='-Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -Wl,-E'
```

## 更新

## 请求处理机制

Nginx有三种可选的并行处理机制：多进程方式、多线程方式和异步方式

## 语言支持

### PHP

Nginx默认不支持PHP，需要搭配php-fmp使用

### Java

Nginx需要搭配Tomcat来运行Java程序

### Python

### Node.js

### Go

### Ruby

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