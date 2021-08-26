# 故障处理

#### 如何判断端口是否放通？
除了检查本机防火墙和云控制台安全组之外，可以通过 **telnet** 去连接

#### root账户修改文件权限， 报错 "Operation not permitted"，不允许操作
使用root修改文件权限，如下。查看文件属性也不是 i 属性导致。

```
[root@iZ2ze3eh720u9x5c1hdhwyZ yanbian]# chmod 750 index.php
chmod: changing permissions of ‘index.php’: Operation not permitted
[root@iZ2ze3eh720u9x5c1hdhwyZ yanbian]# lsattr index.php
-------------e-- index.php

```

出现这种情况有可能是云平台的安全防护导致。
如 阿里云的云安全中心有【网页防篡改】保护，如果为文件/目录添加了该保护，在系统中修改文件/目录 权限就会被禁止。

![](https://libs.websoft9.com/Websoft9/blog/zh/2020/12/linux-safe-websoft9.png)


#### 磁盘满了如何查询哪些文件比较大？

```
# 查看当前目录下各文件、文件夹的大小
du -h –max-depth=1 *

# 查询当前目录总大小
du -sh

# 显示直接子目录文件及文件夹大小统计值
du -h –max-depth=0 *
```

#### 如何查询服务器日志？

运行命令`tailf /var/log/messages`

#### 服务启动失败怎么办？

当linux服务启动失败的时候，系统会提示我们使用 `journalctl -xe` 命令来查询详细信息，定位服务不能启动的原因。


#### 同一IP反复刷新页面导致服务器403错误处理
mod_evasive是Apache防御攻击的模块，有助于防止DoS、DDoS以及对Apache服务器的暴力攻击。它可以在攻击期间提供规避行动，并通过电子邮件和系统日志工具报告滥用行为。该模块的工作原理是创建一个IP地址和URI的内部动态表，并拒绝以下任何一个IP地址：
- 每秒请求同一页多次
- 每秒对同一个孩子发出50多个并发请求
- 暂时列入黑名单时提出任何要求

如果满足上述任何条件，则发送403响应并记录IP地址。
##### 查看Apache模块清单
```
apachectl -M
```
##### 修改配置项
在conf.d目录下找到mod_evasive.conf文件，进行配置（根据网站安全实际需求来）
![](https://libs.websoft9.com/Websoft9/blog/zh/2020/12/Apache-403-mod_evasive-conf-websoft9.png)

