# 迁移

OwnCloud is installed in the system disk default,if there not enough storage space for this disk,you must delete unused files or add data disk for OwnCloud,then migrate all data to data disk 

> Be sure to make a snapshot backup before migrating data, otherwise the consequences of the migration will be unimaginable.


To migrate to the data disk, we offer two options:

<a name="38c5814d"></a>
### Solution1:Change the storage path of OwnCloud to the data disk

OwnCloud's document data is stored by default to: /data/wwwroot/owncloud/data. This solution implements the target by adding a directory (corresponding to the data disk) under OwnCloud and then modifying the default storage path. The specific operations are as follows:

1. Buy the data disk in advance, and then go to the cloud vendor console to do a data disk mount to the server
1. Stop the Apache Service
```shell
systemctl stop httpd
```

1. Create a new folder in the /data/wwwroot/owncloud directory via the SFTP tool. The name suggests: bigdata，this bigdata folder is the default document storage location after migration.
1. Mount the data disk to: _/data/wwwroot/owncloud/bigdata_
1. Copy or Cut _owncloud/data_  to _owncloud/bigdata_
> If the data is large, clipping or copying may fail.


1. Modify the data storage directory location in the Owncloud configuration file(_/data/wwwroot/owncloud/config_)
1. Enable the Apache Service
```shell
systemctl start httpd
```


<a name="b512eb42"></a>
### Solution2:Transfer the server's /data directory to the data disk

This scenario will transfer all the sites (including OwnCloud) and databases on the server to the data disk.
