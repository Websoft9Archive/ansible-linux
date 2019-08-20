# 系统

We summarize the basic principles, components and command operations of the Linux system required for the Images use practice process, and summarize them into a documentation which included the following content

- **Basic Operations**: server restart, run script, etc.
- **File Management**: download files, enter directories, delete files/folders, compress and unzip, modify folder permissions/users (groups), etc.
- **Package Management**: component installation, component upgrade, component uninstallation, system upgrade, etc.
- **Maintaining Linux**: service start|stop|restart, set crontab, view disk space/memory used, etc.

For the above content, we have prepared the[ Linux Quick Start](https://en.websoft9.com/docs/linux/) for you.

------

Top3 Linux commands you must use when using this Image

```shell
#1 modify file&folder permissions:users (groups)
chown -R apache.apache /data/wwwroot

#2 Upgrade Linux
yum update -y

#3 view disk space/memory used
df -lh
free -lh
```
