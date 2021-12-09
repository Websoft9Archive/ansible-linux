# FAQ

## 语言

#### PHP extension 与 PHP Package有什么区别？
为了便于理解，我们认为PHP extension是一种编译后的二进制文件，放在php的bin目录下，供所有应用调用
PHP Package是一种源码包，用户的项目若要用到源码包，需要通过Github下载，并引入到自己的项目中，或者通过composer工具下载

#### 字符编码问题
Ubuntu参考：https://help.ubuntu.com/community/Locale

#### Systemd 是可以用于处理开机一次性运行脚本？

可以，将 Tpye=oneshot 即可

```
[Unit]
Description=Switch-off Touchpad

[Service]
Type=oneshot
ExecStart=/usr/bin/touchpad-off

[Install]
WantedBy=multi-user.target
```

#### 如何查询当前服务器的连接数？
```
ps aux | grep httpd | wc -l
```

#### 如何设置 /tmp, /var/tmp 目录的清理策略？

以CentOS为例，修改 */usr/lib/tmpfiles.d/tmp.conf* 即可

#### Linux 系统有哪些时间？

```
$ timedatectl status
Local time: Tue 2021-11-23 10:08:06 CST
Universal time: Tue 2021-11-23 02:08:06 UTC
RTC time: Tue 2021-11-23 10:08:04
    Time zone: Asia/Shanghai (CST, +0800)
    NTP enabled: yes
    NTP synchronized: yes
    RTC in local TZ: yes
    DST active: n/a
```

* Local time: 你自己手表上的时间
* Universal time：世界统一时间
* Real Time Clock：RTC, CMOS or BIOS clock
* System clock：系统时间，开机的时候读取 RTC 时间

NTP 是指网络时间服务，用于校对时间。 