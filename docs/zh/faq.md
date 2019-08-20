# FAQ

<a name="1ycWh"></a>
#### How can OwnCloud view&edit file online?
You should complete the [OnlyOffice setting](admin-onlyds) on your OwnCloud

<a name="mbxYH"></a>
#### How do I transfer files from one user to another?
See [transferring files to another user](https://doc.owncloud.org/server/admin_manual/configuration/files/file_sharing_configuration.html#transferring-files-to-another-user).

<a name="sXbab"></a>
#### [](https://doc.owncloud.org/server/admin_manual/faq/#how-do-i-deal-with-problems-caused-by-using-self-signed-ssl-certificates)How do I deal with problems caused by using self-signed SSL certificates?
See [the security section of the OCC command](https://doc.owncloud.org/server/admin_manual/configuration/server/occ_command.html#security).

<a name="zlm5N"></a>
#### [](https://doc.owncloud.org/server/admin_manual/faq/#im-the-admin-and-i-lost-my-password-what-do-i-do-now)I'm the admin and I lost my password! What do I do now!
See [the reset admin password documentation](https://doc.owncloud.org/server/admin_manual/configuration/user/reset_admin_password.html).

<a name="Et08a"></a>
#### [](https://doc.owncloud.org/server/admin_manual/faq/#what-is-a-federated-system)What is a Federated System?
A Federated System is another ownCloud or [OpenCloudMesh](https://oc.owncloud.com/opencloudmesh.html) supporting cloud service.

<a name="5b085d9d"></a>
#### Can I deploy multiple sites on the OwnCloud(LAMP)?
You can deploy unlimited number of websites on LAMP, but you should know that every site need corresponding virtual host profile segment in the file `vhost.conf`

<a name="7d55d680"></a>
#### Can I deploy mys site If there is no domain name？
Yes, you can deploy your site if no domain and visit by http://Internet/mysite 

<a name="34abd8ab"></a>
#### How to bind a domain name to my application?
Using SFTP to modify the vhost.conf file, 

<a name="89946f5b"></a>
#### What is the default character set?
UTF-8

<a name="5cd8198d"></a>
#### What the default mysql password of root?
Using SFTP to connect to Instance,you can get the MySQL password from `_/root/password.txt_`

<a name="f1c5eb6c"></a>
#### Is there a web-base GUI database management tools?
Yes, phpMyAdmin is on this Image, visit by _http://Internet/phpmyadmin_

<a name="26cadc19"></a>
#### Can I use this LAMP if I don't understand the Linux command?
Yes, you can use GUI tool WinSCP to start LAMP, no commands

<a name="6641224a"></a>
#### phpMyAdmin page access blank?
Please try another browser, such as chrome or firefox. If the phpMyAdmin can be opened normally before, and now appears to be incomplete or blank, it is recommended to clean up the browser cache, cookies and other information.

<a name="1aa32c03"></a>
#### How to modify the website root directory?
You should know the root directory is_ /data/wwwroot/www.example.com _and was configured in the `vhost.conf` file, just need to change the Directory,DocumentRoot parameter to you want

<a name="5f2225b2"></a>
#### How to delete 9Panel?
If you don't want to use 9Panel, please delete all files in 9Panel and keep an empty 9Panel folder

<a name="2a66e2a7"></a>
#### Do I need to change the owner(group) for the files which I upload by SFTP?
No, you don't need to change them because LAMP Image have change it automaticly

<a name="194ea5a5"></a>
#### How can I reset my php.ini to return to the initial?
Download the [php.ini](https://github.com/Websoft9/ansible-lamp/blob/master/roles/php/templates/php.ini) from Websoft9 LAMP project on Github, upload to Server and cover _/ect/php.ini_<br />_
<a name="08f4f5e3"></a>
#### How to change the permissions of filesytem?
When install new extension from back-end it will not successful,may be the permissions of file and folder is not appropriate,you should change it
```shell
chown -R apache.apache /data/wwwroot
find /data/wwwroot -type d -exec chmod 750 {} \;
find /data/wwwroot -type f -exec chmod 640 {} \;
```

<a name="2c594c45"></a>
#### How to set Rewrite rules for your application?
LAMP Image has installed Apache rewrite module, you just need to create a `.htaccess` in your application root directory and configure your rewrite rules in it

<a name="ee7a1c51"></a>
#### How to disable Apache Test Page?
Using the # to disable all the content in the file: _/etc/httpd/conf.d/welcome.conf_, then restart service

<a name="83c28318"></a>
#### How to bind a domain name for your application?
Modify the **ServerName,ServerAlias** configuration item of VirtualHost template in the file `vhost.conf`<br />Then, restart the httpd service
