install.sh 是我们提供的一键安装脚本，用于部署基于Ansible的应用项目

## 使用示例

```
#安装项目，用户生产镜像
wget -N https://raw.githubusercontent.com/Websoft9/ansible-linux/master/scripts/install.sh; bash install.sh -r magento -i 1


#安装项目，非生产镜像
wget -N https://raw.githubusercontent.com/Websoft9/ansible-linux/master/scripts/install.sh; bash install.sh -r magento -i 0 
```
install.sh 支持两个参数：

* -r 代表项目名称，例如：magento, lamp, lnmp, wordpress, joomla, gitlab 等
* -i 代表是否初始化，支持 0（默认值）和1 两种参数
