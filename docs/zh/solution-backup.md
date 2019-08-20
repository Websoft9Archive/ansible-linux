# 备份与恢复

Routine backup (archives) of the database and application setup is essential to ensure failover is smooth.

Backup is based on the server snapshot automatic backup,manual local backup,using plugin to backup in three ways, three of which have their own advantages and disadvantages, it is recommended to use together

> Automatic Backup is very useful and efficient for your system maintenance.


<a name="abcd88fb"></a>
## Snapshot of Cloud Server Backup

Cloud Server provider have the Snapshot or Cloud Server Backup Service, the snapshot is for the Server disk. Snapshot tool can record the specified point in time the hard disk data, all backed up, and can achieve a key recovery.

> Different Cloud vendor snapshot settings slightly different


- Backup scope: Operation System,Runing environment,Database,OwnCloud Codes
- Backup effect: Very Good
- Backup frequency: Automatic backup per hour if you need
- Recommended reason : Done a snapshot backup, a key to restore to the backup point of time state. That is, on-site reduction, very good function.

<a name="be80573e"></a>
## Manual Backup

Some times you can use the manual Backup for OwnCloud if you need.<br />Just download the entire OwnCloud files by SFTP and export database by phpMyAdmin,you have completed the backup

- Backup scope: Database,OwnCloud Codes
- Backup effect: Good

- Backup frequency: You can operate when you need
- Recommended reason : Manual looks more insurance


<a name="VeWAO"></a>
## Using Backup Interface of OwnCloud

When you backup your OwnCloud server, there are four things that you need to copy:

1. Your `config/` directory.
1. Your `data/` directory.
1. Your ownCloud database.
1. Your custom theme files, if you have any.

<a name="e312245f"></a>
### Automatic Backup & Restore
If you have installed the "OwnBackup" app ( [install it first](http://en.websoft9.com/xdocs/owncloud-image-guide/#using-apps)) you can backup use interface

1. Admin->Admin->OwnBackup

[![](https://cdn.nlark.com/yuque/0/2019/png/152462/1552220698513-66f6d65b-f46e-4b12-88c7-76ac0fcbbe3e.png#align=left&display=inline&height=323&originHeight=717&originWidth=1600&size=0&status=done&width=720)](http://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-ownbackup-websoft9.png)<br />
1. Click the “Create Backup”-Yes,backup successful
1. If you want to Restore owncloud,Select the backup you want to restore tables from and Select the tables you want to restore,then click the button “Restore Tables”

[![](https://cdn.nlark.com/yuque/0/2019/png/152462/1552220698521-8d0aa3cb-9a83-4081-822b-c2c11d566693.png#align=left&display=inline&height=594&originHeight=768&originWidth=931&size=0&status=done&width=720)](http://libs.websoft9.com/Websoft9/DocsPicture/en/owncloud/owncloud-restore-websoft9.png)

