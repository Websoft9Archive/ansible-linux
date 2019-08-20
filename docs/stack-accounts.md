
# Usernames and Passwords

These accounts are required for Image Stack installation and configuration when using AWX:

## AWX

Administrator Username is: `admin`  
Administrator Password is: `admin`

## PostgreSQL

* Administrator Username is: *`postgre`*
* The database password was storaged in the file of your VM: *`/credentials/password.txt`*. Suggest you log in Azure Portal and using the online SSH terminal to run the the `cat` command to get the password：
   ![Run cat](https://libs.websoft9.com/Websoft9/DocsPicture/zh/common/catdbpassword-websoft9.png)
* PostgreSQL Web-GUI: *http://Internet IP:9090*

## Linux

* Host address: Public IP address
* Connection method: Cloud Console terminal or SSH tool
* Administrator password: Set it when you create the server. If you don't remember the password, you need to reset it through the cloud console.
* Administrator account: Different cloud platforms have certain differences
   |  Cloud Platform   |  Administrator Username   |
   | --- | --- |
   |  Azure   |  created by yourself   |
   |  AWS   |  ubuntu   |
   |  AlibabaCloud, HUAWEI CLOUD, Tencent Cloud |  root   |
