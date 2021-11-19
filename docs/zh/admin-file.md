---
sidebarDepth: 3
---

# 磁盘与文件

## 磁盘管理

### 存储类型

Linux 支持多种接口类型的存储设备：

- hd：IDE 设备，实际名称为 hda, hdb，即第一个 IDE 设备，第二个 IDE设备，以此类推
- sd：SATA, USB, SCSI 设备，实际名称为 sda, sdb，同上

每个设备又可以被分区，例如第一个 IDE 设备的第一个分区，就被命名为 hda1，以此类推...  

以上就是关于设备、分区在 Linux 系统中的命名。  

命令 `lsblk` 可以非常清晰的展示上面描述的信息和规则

```
$ lsblk
NAME               MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
vda                251:0    0   40G  0 disk
├─vda1             251:1    0  800M  0 part /boot
├─vda2             251:2    0 28.7G  0 part
│ ├─rootvg-rootlv  252:0    0 18.7G  0 lvm  /
│ └─rootvg-crashlv 252:1    0   10G  0 lvm  /var/crash
├─vda14            251:14   0    4M  0 part
└─vda15            251:15   0  495M  0 part /boot/efi


$ lsblk
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
vda    253:0    0  40G  0 disk
└─vda1 253:1    0  40G  0 part /
```

TYPE 项中的：disk 表示磁盘， part 表示分区， lvm 

### 分区

磁盘分区可用区域，例如将一块SSD磁盘划分：sda1、sda2、sda3、sda4等4个分区。  

#### 分区类型

在Linux系统下，磁盘的分区大致可以分为三类，分别为**主分区、扩展分区和逻辑分区**。

传统的 MBR 分区方式一块硬盘最多只能有四个主分区，需要更多分区，就必须引入扩展分区的概念。  

> 弥补 MBR 分区形式的局限性，又诞生了一种逐渐取而代之的格式 GPT

下面这张图就非常清晰的说明了这三种分区之间的关系：  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-partition001-websoft9.png)

```
#查看磁盘分区
$ fdisk -l
Disk /dev/vda: 42.9 GB, 42949672960 bytes, 83886080 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x000c5246

   Device Boot      Start         End      Blocks   Id  System
/dev/vda4            2048    83886079    41942016    5  Extended
```

其中：Disk label type: dos 表示 MBR 分区，相对应 Disklabel type: gpt 就表示 GPT 分区类型。  

#### 分区扩容

实践中，我们要对云服务器的系统盘进行扩容，除了先通过云控制台购买更大的磁盘空间之外，还需要进行如下的操作：

1. 规划好新增的磁盘应该对应的分区，假设为 /dev/vda1 分区

2. 对分区进行扩容操作
   ```
   #1 安装分区扩容软件 growpart
   yum install -y cloud-utils-growpart

   #2 分区扩容操作
   growpart /dev/vda 1

   #3 增大或收缩 ext2/ext3/ext4 文件系统
   resize2fs /dev/vda1  
   ```

#### LVM

LVM 是一个新的磁盘虚拟化管理技术，将多个**真实的物理分区**虚拟为一个**逻辑上物理分区**，以便更多的对磁盘进行伸缩和备份。  

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-lvm-websoft9.jpg)

下面直接列出 LVM 常见的用法：

```
#1 显示 LV 分区
$ lvdisplay

  --- Logical volume ---
  LV Path                /dev/rootvg/crashlv
  LV Name                crashlv
  VG Name                rootvg
  LV UUID                2MectT-GQ0J-FkVJ-Phue-7X0S-lH0U-2iJclg
  LV Write Access        read/write
  LV Creation host, time localhost, 2021-10-13 16:53:19 +0000
  LV Status              available
  # open                 1
  LV Size                10.00 GiB
  Current LE             2560
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  Block device           252:1

  --- Logical volume ---
  LV Path                /dev/rootvg/rootlv
  LV Name                rootlv
  VG Name                rootvg
  LV UUID                bdLRb7-a1WN-DKRR-XNpX-sE5B-1IsA-XtsDfq
  LV Write Access        read/write
  LV Creation host, time localhost, 2021-10-13 16:53:19 +0000
  LV Status              available
  # open                 1
  LV Size                <18.73 GiB
  Current LE             4794
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  Block device           252:0

  #2 扩容 PV
  lv
  pvresize
```

实战案例学习：[《阿里云系统盘LVM扩容》](https://help.aliyun.com/document_detail/131143.htm)。  

下面是对案例的简述：

1. 云控制台通过购买，新增20G系统盘空间
2. 对根目录所在分区进行扩容操作
   ```
   #1 安装分区扩容软件 growpart
   yum install -y cloud-utils-growpart

   #2 分区扩容操作
   growpart /dev/vda 2

   #3 增大或收缩 ext2/ext3/ext4 文件系统
   resize2fs /dev/vda2 
   ```
3. 运行 `lvdisplay` 查看是否存在 LVM 的分区
   ```
      --- Logical volume ---
   LV Path                /dev/rootvg/crashlv
   LV Name                crashlv
   VG Name                rootvg
   LV UUID                2MectT-GQ0J-FkVJ-Phue-7X0S-lH0U-2iJclg
   LV Write Access        read/write
   LV Creation host, time localhost, 2021-10-13 16:53:19 +0000
   LV Status              available
   # open                 1
   LV Size                10.00 GiB
   Current LE             2560
   Segments               1
   Allocation             inherit
   Read ahead sectors     auto
   - currently set to     8192
   Block device           252:1
   ```
4. 先扩容 PV
   ```
   pvdisplay
   pvresize <pvname>
   pvs
   ```

5. 扩容 LV （最终所需的分区）
   ```
   lvextend -l +100%FREE <LV's Path>
   lvdisplay
   lvs
   ```

6. 修正文件系统
   ```
   # ext4 文件系统
   resize2fs <LV's Path>

   # xfs文件系统
   xfs_growfs  <LV's Path>
   ```

### 格式化

格式化指将磁盘分区格式化成不同的文件系统，以方便操作系统集中组织和管理文件。

```
#将/dev下的 sda5 磁盘格式化为 ext2 的格式类型
mkfs.ext2 /dev/sda5
```
### 挂载

对于Linux系统来说，挂载是将格式化后的分区与系统中的目录匹配起来，使得访问这个目录就相当于访问这个分区。

```
#将 /dev/sda5 挂载到 test 中
mount /dev/sda5/test
```
### 文件系统

Linux除支持Ext4文件系统外，还支持其他各种不同的文件系统，例如集群文件系统以及加密文件系统等。Linux将各种不同文件系统的操作和管理纳入到一个统一的框架中，使得用户程序可以通过同一个文件系统界面，也就是同一组系统调用，能够对各种不同的文件系统以及文件进行操作。这样，用户程序就可以不关心各种不同文件系统的实现细节，而使用系统提供的统一、抽象、虚拟的文件系统界面。这种统一的框架就是所谓的虚拟文件系统转换（Virtual Filesystem Switch），一般简称虚拟文件系统 (VFS)。虚拟文件系统描述如下所示：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vfs-websoft9.png)

Linux系统核心可以支持十多种文件系统类型，比如Btrfs、JFS、ReiserFS、ext、ext2、ext3、ext4、ISO9660、XFS、Minx、MSDOS、UMSDOS、VFAT、NTFS、HPFS、NFS、SMB、SysV、PROC等。

```
#将系统内所有的文件系统列出来
df -T
Filesystem     Type     1K-blocks     Used Available Use% Mounted on
udev           devtmpfs   4047124        0   4047124   0% /dev
tmpfs          tmpfs       815312     8252    807060   2% /run
/dev/vda1      ext4      61795304 49591808   9461040  84% /
tmpfs          tmpfs      4076556        0   4076556   0% /dev/shm
tmpfs          tmpfs         5120        0      5120   0% /run/lock
tmpfs          tmpfs      4076556        0   4076556   0% /sys/fs/cgroup

#将系统内的所有特殊文件格式及名称都列出来

df -aT
Filesystem    Type 1K-blocks    Used Available Use% Mounted on
/dev/hdc2     ext3   9920624 3823112   5585444  41% /
proc          proc         0       0         0   -  /proc
sysfs        sysfs         0       0         0   -  /sys
devpts      devpts         0       0         0   -  /dev/pts
/dev/hdc3     ext3   4956316  141376   4559108   4% /home
/dev/hdc1     ext3    101086   11126     84741  12% /boot
tmpfs        tmpfs    371332       0    371332   0% /dev/shm
none   binfmt_misc         0       0         0   -  /proc/sys/fs/binfmt_misc
sunrpc  rpc_pipefs         0       0         0   -  /var/lib/nfs/rpc_pipefs
```


## 文件管理

### 拥有者

规定文件只能被指定用户访问访问  

范例：

```
# 修改wwwroot文件夹所属的用户和用户组为nginx
chown -R nginx.nginx /data/wwwroot
```

### 权限

Linux系统对不同的用户访问同一文件（包括目录文件）的权限做了不同的规定。  



范例：

```
# 分别修改文件和文件夹的读、写、执行权限
find /data/wwwroot/default -type f -exec chmod 640 {} \;
find /data/wwwroot/default -type d -exec chmod 750 {} \;
```

### 操作

对文件典型操作包括：

cp 拷贝文件和目录  
rm 移除文件或目录  
mv 移动文件与目录，或修改名称  

查看文件有多种命令：

cat  由第一行开始显示文件内容  
tac  从最后一行开始显示  
nl   显示的时候，同时输出行号  
more 一页一页的显示文件内容  
less 一页一页的显示文件内容+往前翻页 
head 只显示头几行  
tail 只显示尾几行  

### 目录

接下来我们就来看几个常见的处理目录的命令吧：

ls: 列出目录
cd：切换目录
pwd：显示目前的目录
mkdir：创建一个新的目录
rmdir：删除一个空的目录
cp: 复制文件或目录
rm: 移除文件或目录
mv: 移动文件与目录，或修改文件与目录的名称

### FTP

FTP就是文件传输协议。用于互联网双向传输，控制文件下载空间在服务器复制文件从本地计算机或本地上传文件复制到服务器上的空间。

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/sftp-structure-websoft9.png)

使用Linux，常见有SFTP和FTP两种文件传输模式。其中SFTP更为广泛，下面先介绍SFTP

#### SFTP

SFTP 即 SSH File Transfer Protocol，又称之 Secret File Transfer Protocol。SFTP是使用SSH协议的FTP模式，也称之为安全增强型的FTP。SFTP工具是Linux用户最喜欢的一种操作方式，Linux系统默认支持SFTP（即免安装）

下面以WinSCP这款SFTP工具为例，详细说明SFTP的使用。


##### 配置WinSCP

1. 下载[WinSCP](https://winscp.net/) ，安装后，启动并新建一个连接
2. 根据云服务器的 **密码验证和秘钥对** 两种验证方式分别说明：
   - 密码验证方式设置（最常见的方式）
     ![密码验证方式](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-newsite.png)
   - 秘钥对验证方式设置
     ![秘钥对验证方式](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-secrets-websoft9.png)
3. 验证方式设置好之后，点击"登录"。登录中过程中，系统提示您是否保存登录信息，选择"是"
4. 成功连接后的界面
   ![WinSCP管理界面](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-success.png)

##### 管理文件

WinSCP 通过拖拽，就可以方便上传下载文件，可以对文件（夹）可以对进行多种设置与操作

1. 一般来说网站的文件都放在 */data/wwwroot* 目录下夹
   ![upload files](http://libs.websoft9.com/Websoft9/DocsPicture/en/winscp/winscp-dragfile-websoft9.png)

2. 右键单击服务器上一个文件或文件夹，可以对云服务器进行多种操作
   ![管理文件](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-youjian.png)

3. 以修改文件权限为例的相关界面如下

   ![管理文件](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-quanxian.png)

##### 运行命令

WinSCP是自带命令运行功能的，虽然命令功能仅限于运行非交互式命名（即命令执行过程中无需反馈和过程中的输入），但对于初学者确简单实用。

1. WinSCP登录到服务器，点击菜单来的命令窗口图标（快捷键Ctrl+T也可以）
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/winscp-ucmd-websoft9.png)
2. 在弹出的命令运行窗口执行命令（每次一条命令），以查询内存使用为例，运行命令 `free -m`
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/wincp-showmemory-websoft9.png)

##### 集成Putty

在某些特定的常见下，可能需要使用Putty来运行命令。由于Putty是一个命令操作界面，每次使用的时候都需要输入root密码，如果密码比较复杂，会让人感觉比较麻烦。其实WinSCP是可以集成Putty的，集成后，通过WinSCP就可以打开Putty，自动登录到服务器。

1. 打开Winscp-选项-集成-应用程序。Putty/terminal客户端路径这里为你本地putty.exe程序的路径
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-putty.png)
2. 集成成功后，只需要通过Winscp的窗口快捷方式即可打开Putty
   ![命令行工具](http://libs.websoft9.com/Websoft9/DocsPicture/zh/winscp/websoft9-winscp-puttyopen.png)

> 通过Winscp打开Putty操作与直接打开putty没有区别

##### FTP

Linux 系统默认情况下，并没有预制安装FTP。如果需要使用FTP，需要手工安装，具体步骤如下：

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
