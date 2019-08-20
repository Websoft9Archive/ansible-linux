# 数据库

Using the Websoft9 OwnCloud (LAMP), you should have some skills for configure [MySQL](https://dev.mysql.com/doc/refman/8.0/en/server-administration.html) like below:

- Manage MySQL by GUI tool phpMyAdmin
- Manage MySQL by command
- Modify password, create user, create database
- Import and Export database
- Don't remember password, need to reset it
- MySQL configuration
- Enable MySQL remote connection 

For the above content, we have prepared the [**MySQL Quik Start **](https://en.websoft9.com/docs/mysql)for users.

------

Top3 MySQL configuration you must use when using this Image

<a name="44afaaa9"></a>
#### #1 Modify the MySQL root password
Using the Chrome or FireFox to visit http://Internet IP/phpmyadmin to login, change the password on the dashboard directly

[![](https://cdn.nlark.com/yuque/0/2019/png/152462/1554199408257-9fe14b76-94bf-472d-bfc3-66b3ee662732.png#align=left&display=inline&height=351&originHeight=453&originWidth=962&status=done&width=746)](http://libs.websoft9.com/Websoft9/DocsPicture/en/phpmyadmin/phpmyadmin-changepwds-websoft9.png)

<a name="bb311254"></a>
#### #2 Reset the MySQL root password
Using the SSH to connect Cloud Server, run the following command

```shell
sudo git clone https://github.com/Websoft9/linuxscript.git; cd linuxscript/Mysql_ResetPasswd_Script;sudo sh reset_mysql_password.sh
```



<a name="aa276cf5"></a>
#### #3 Import and Export database

In phpMyAdmin, Export is to back up the database, import and restore the database.

--Export

1. Login to phpMyAdmin, select your database then click "Export" tab on the top menu

[![](https://cdn.nlark.com/yuque/0/2019/png/152462/1552893080852-998cabe4-c3e3-4e62-8b1c-8c1f906056de.png#align=left&display=inline&height=426&originHeight=568&originWidth=960&size=0&status=done&width=720)](http://libs.websoft9.com/Websoft9/DocsPicture/en/phpmyadmin/phpmyadmin-export-websoft9.png)
1. Select suitable Export method,Format for you, then click the "Go" button to start export
1. After the database backup file (.sql suffix) is generated, save it to the local computer

--Import

1. Restore the database, corresponding to the "Import" operation, refer to the following<br /> [![](https://cdn.nlark.com/yuque/0/2019/png/152462/1552893338514-ee63eab8-17ec-4613-8685-d57e111026a2.png#align=left&display=inline&height=659&originHeight=881&originWidth=962&size=0&status=done&width=720)](http://libs.websoft9.com/Websoft9/DocsPicture/en/phpmyadmin/phpmyadmin-import-websoft9.png)
1. Import files should pay special attention to character set compatibility
