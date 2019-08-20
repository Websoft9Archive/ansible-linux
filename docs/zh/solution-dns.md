# 绑定域名

If you want to use Domain for OwnCloud, these steps is for you

1. Modify the vhost configuration file
1. Modify the config.php file of OwnCloud. E.g. set the overwritehost to your domain name
```shell
<?php
$CONFIG = array (
  'instanceid' => '***************',
  'passwordsalt' => '**********************************',
  'datadirectory' => '/cloudData',
  'dbtype' => 'mysql',
  'version' => '7.0.1.1',
  'dbname' => 'ownCloud',
  'dbhost' => '127.0.0.1',
  'overwritehost' => 'cloud.our-company.net',
```

> When you share the file from OwnCloud, the domain name part of URL link is overwritehost

