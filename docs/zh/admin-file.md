# 磁盘与文件

## SFTP

## FTP

1. 检查所属用户和属组
    检查需要使用FTP上传目录的用户和用户组,假设上传目录为 `/data/wwwroot/default` 

    执行命令  `ls -l /data/wwwroot/`  查看  `default`  目录的用户和用户组,如下图所示

    ![1524795775448](http://libs.websoft9.com/Websoft9/DocsPicture/zh/lamp/ftp-install-websoft9.png)

    第一个 `apache` 为用户,第二个 `apache` 为用户组

2. 安装  `pure-ftpd`

    `yum -y install pure-ftpd`

3. 配置 `pure-ftpd`

    修改 `/etc/pure-ftpd/pure-ftpd.conf`  内容如下:

    ```
    ChrootEveryone              yes
    MaxClientsNumber            50
    MaxClientsPerIP             8
    DisplayDotFiles             no
    AnonymousOnly               no
    NoAnonymous                 yes
    DontResolve                 yes
    MaxIdleTime                 10
    PureDB                      /etc/pure-ftpd/pureftpd.pdb
    LimitRecursion              2000 10
    AnonymousCanCreateDirs      no
    Umask                       133:022
    AllowUserFXP                no
    AllowAnonymousFXP           no
    ProhibitDotFilesWrite       no
    ProhibitDotFilesRead        no
    AnonymousCantUpload         yes
    MaxDiskUsage                80
    IPV4Only                    yes
    ClientCharset               utf-8
    ```

4. 创建 虚拟用户 生成用户数据 db (可用于创建多用户)

    执行命令(创建虚拟用户): 

     `pure-pw useradd www_user_name -u apache -d /data/wwwroot/default`  

    > 执行后会提示设置密码,密码输入不会显示

    > www_user_name 为虚拟用户名  apache 为步骤1所查看 /data/wwwroot/default 为FTP上传目录

     执行命令(生成用户数据):  
     `pure-pw mkdb /etc/pure-ftpd/pureftpd.pdb`

5. 开启服务 设置开机启动
    执行一下命令:
    `systemctl start  pure-ftpd.service`
    `systemctl enable pure-ftpd.service`

## 分区与格式

## 挂载