# 自动化运维

Linux 命令行操作由于具备可编程，可控制的特征，天生就适合自动化管理。

Linux自动化运维技术有多种，比较流行的包括：Shell脚本、Ansible、Chef等自动化技术。

Websoft9提供的自动化部署以Ansible为核心技术，集合Shell脚本，实现复杂软件部署的全过程自动化。

同时，Linux系统也是非常重要的开发平台，延伸到开发领域的自动化，就诞生了DevOps技术：

![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/devops-process.png)

> 自动化技术的基石仍然是Linux命令

## Ansible 

本节不是讲述Ansible的原理，而是用接近文科式的语言，阐述Ansible在实践中容易犯错的技术盲点，纠正错误的认知。  

### 箴言

如何成为Ansible高手？

Shell命令是根本，夯实基础稳步走；  
晦涩理论看一遍，动手实验是正道。  
经典教材床头放，官方文档经常看；  
闲时看书有收获，勤动笔来总结多。  
三人成行有我师，学会提问收获多；  
疑难问题要会诊，切莫独钻死胡同。  
稳定简约见功底，数据结构来撑腰；  
软件没有终结日，长久迭代价值高。  

学会驾驭Ansible，用通用的软件方法论去理解Ansible，千万不要被Ansible的技术术语所牵制。

### Ansible 之 50 问

#### Ansible受控端是否必须提前安装Python？

不是。Ansible的[raw](https://docs.ansible.com/ansible/latest/modules/raw_module.html#raw-module)模块和[script](https://docs.ansible.com/ansible/latest/modules/script_module.html#script-module)模块不依赖于客户端安装的Python来运行。从技术上讲，您可以使用Ansible使用raw模块安装兼容版本的Python ，然后使用该模块使用其他所有模块。例如，如果需要将Python 2引导到基于RHEL的系统上，则可以按以下方式安装它：  

```
ansible myhost --become -m raw -a "yum install -y python2"
```
#### 主控端如何安装Ansible最方便？

推荐采用 pip install ansible

#### Ansible 的应用模块好用吗？例如：Docker, MySQL等

建议弃用，直接使用命令更为稳定可靠，这样可以避免这边模块的版本兼容性问题

#### Ansible中的变量优先级有哪些？

有高到低：ansible命令带入的变量 > cfg配置文件的变量 > 主项目的var变量 > role中的var变量 > role default 变量

#### Ansible有全局变量的概念吗？

没有，但我们可以将：ansible命令带入的变量 | cfg配置文件的变量 | 主项目的var变量 视为全局变量。但特别需要注意的是：Ansible项目中即使有同名变量，它们不会共享一个内存区域，而是各自独占内存（区别于Java等语言变量指针的概念）。

#### Ansible 如何实现模块化？

Ansible Galaxy 就是模块化唯一的方案

#### Ansible 中经常会出现 python-urllib3 之类的报错，如何处理？

python-urllib3 报错大部分情况下，通过 yum install python-urllib3 解决，而不是 pip install

#### Ansible 中的条件判断有哪些可能性？

True, not False, !=none, !="", 

#### Ansbile 中Python Pip apt/yum 总结

1. 客户端和服务端 python版本可以不一致
2. 升级最新pip版本会导致 pip 命令无法使用 官方解释使用 python3 -m pip install xxx
3. apt lock 问题可以在脚本中预处理

#### Ansbile 客户端和服务端 Python版本是否可以不一致？

可以

#### pip和pip3共存吗？

可以共存。但建议通过：python3 -m pip install xxx 这样的方式使用Python3下的pip，启用pip3这种表达方式


#### 为什么Ansible中apt升级容易导致 lock？

AWS上非常容易出错，建议在脚本中预处理

#### Ansible 之PIP模块是否可以制定Python版本？

可以，参考如下

```
# Install (Bottle) for Python 3.3 specifically,using the 'pip3.3' executable.
- pip:
    name: bottle
    executable: pip3.3
```

#### dnf 模块现在可以用吗？

现在不建议使用dnf模块

#### 一个Ansible项目中，主入口文件中 *vars_files* 与 *vars* 哪个变量优先级高？

vars_files的优先级更高。需要注意的是Ansible的变量是无法覆盖的，即同名变量在内存中都有单独的存储区域，而Ansible只是通过优先级的方式使用。