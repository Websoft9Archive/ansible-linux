# 升级

Metabase完整的升级包括：操作系统补丁升级、运行环境补丁漏洞升级和应用程序升级三个部分

> 网站技术日新月异，更新升级是维护工作之一，长时间不升级的程序，就如长时间不维护的建筑物一样，会加速老化、功能逐渐缺失直至无法使用。

## 操作系统&运行环境升级

Websoft9提供的镜像（Linux版）会自动完成操作系统和运行环境的升级，用户只需关注网站的升级。

若计划立即进行升级，请使用WinSCP的终端窗口运行一条升级命令：

``` shell
#For Ubuntu
apt update && apt upgrade -y

#For Centos&Redhat
yum update -y
```

## Metabase升级

Metabase有升级包的时候，后台会及时给出提示。参考下面的步骤完成升级：

1. Metabase后台->设置->升级，如果有新的升级包，系统会给与提示
![Metabase升级提示](http://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereminder-websoft9.png)

2. 点击“更新”按钮后，系统会跳转到Metabase官方的安装页面。
3. 我们提供的部署包采用的是jar包安装模式，因此在安装页面我们选择“Custom install”模式，
![Metabase升级提示](http://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatedl-websoft9.png)

3. 下载Metabase.jar包后，上传到服务器 `/data/wwwroot/metabase`, 覆盖已有的同名文件
![Metabase升级提示](http://libs.websoft9.com/Websoft9/DocsPicture/zh/metabase/metabase-updatereplace-websoft9.png)

4. 重新加载Metabase，升级成功