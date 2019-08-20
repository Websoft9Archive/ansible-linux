# HTTPS访问

Websoft9 OwnCloud(LAMP) have enabled the Nginx SSL module, you just need to add the HTTPS profile to vhost configuration file .Before setting up HTTPS access, please open port 443 of the security group. if not, HTTPS access is not available.

Here are two configuration schemes for HTTPS, please choose according to the actual situation:

<a name="f7f3b410"></a>
## Configuration Method 1: Using your own certificate

If you have already applied for a certificate (please ensure that the certificate is available), please refer to the following configuration:

1. Upload the certificate to the certificate Directory: _/data/cert_ (no cert directory can be created by yourself)
1. Copy the HTTPS profile template below into the _`vhost.conf`_ file and save
```shell
<VirtualHost *:443>
ServerName  www.mydomain.com
DocumentRoot "/data/wwwroot/owncloud"
#ErrorLog "logs/www.mydomain.com-error_log"
#CustomLog "logs/www.mydomain.com-access_log" common
<Directory "/data/wwwroot/owncloud">
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

3. Modify the related items in the configuration file and save
| **Items** | **Description** |
| --- | --- |
| ServerName | Primary domain |
| DocumentRoot | The real website storage directory |
| Directory | The real website storage directory |
| ErrorLog | error logs directory |
| CustomLog | visit logs directory |
| SSLCertificateFile | SSLCertificateFile directory, suffix name is .crt or .pem |
| SSLCertificateKeyFile  | SSLCertificateKeyFile directory, suffix name is .key |
| SSLCertificateChainFile  | SSLCertificateChainFile  directory, suffix name is .cer |

> The incorrect directory will cause the service to fail to restart, view the ErroLog to troubleshoot


3. Restart HTTP Services
```shell
#~ systemctl restart httpd
```


<a name="f09ba4e3"></a>
## Configuration Method 2: Using Let's Encrypt

You can use the free SSL/TLS Certificate [Let's Encrypt](https://letsencrypt.org/) in this Image, Let's Encrypt is a free, automated, and open Certificate Authority.

Before using Let's Encrypt Certificate for your site, you should make sure that your site have already bound to the domain name, it's means that the ServerName parameter have correct domain in HTTP profile template.<br />E.g. The domain of your site is test.websoft9.cn, here are the steps to configure the HTTPS:

1. Start up the Let's Encrypt configuration just need one command
```shell
certbot
```

2. Enter the corresponding content according to the prompt
> You can select multiple domain by the method 1,2 when come to the step "Which names would you like to activate HTTPS for?"



3. After the above steps are completed, certbot will automatically configure the certificate to the directory _/etc/letsencrypt/live/_

4. Visit the HTTPS to confirm you have configured successfully

---


<a name="FAQ"></a>
## FAQ

<a name="aa9423d7"></a>
### Note on the application of the certificate

- domain.com is a wildcard domain name method and cannot be used to apply for a free certificate
- When applying for a certificate, please resolve the domain name first. some certificates will bind the IP address corresponding to the domain name, that is, the IP address cannot be replaced once applied, otherwise the certificate will not be available

<a name="cb873aa0"></a>
### Why is the setup successful, showing "the connection established with this site is not completely secure "?
If https can be visited, you can make sure that your HTTPS settings are successful, just because there are static files containing http access, or external links, etc. in the website, the browser alarms that your website is not completely safe.
