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

## PHP处理

我们知道Apache被广泛用于PHP环境，Apache有两种PHP处理机制：

- php-fpm
- mod_php

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