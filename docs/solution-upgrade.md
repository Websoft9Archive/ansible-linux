# Upgrade

The complete upgrade of this Image includes: Operating System patch upgrade, Running Environment patch vulnerability upgrade and OwnCloud upgrade three parts

> Website technology is changing with each passing day. Updates and upgrades are one of the maintenance tasks. Programs that are not upgraded for a long time, like buildings that are not maintained for a long time, will accelerate aging and gradually lose functionality until they are unavailable.


Start any upgrade,you should complete the backup first

<a name="88cf1437"></a>
## Operating System &  running environmen Upgrade

If you are using the Zentao on Linux Image of us,upgrade is very simple,just only one command
```shell
yum update -y
```

<a name="18a6c2f4"></a>
## OwnCloud Upgrade

OwnCloud provides a very user-friendly upgrade (update) portal, which can complete the update of the main version and APP plug-in according to the update prompt of the system.

<a name="VJtUG"></a>
### Plugin Upgrade


![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updatenotify-websoft9.png#align=left&display=inline&height=336&originHeight=336&originWidth=960&status=done&width=960)


![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updatelist-websoft9.png#align=left&display=inline&height=522&originHeight=522&originWidth=960&status=done&width=960)

3. Click the "update" button and the system goes to "update" and wait patiently for the update
4. When all updates are completed, the update list shows "all apps are up to date"

> If there is a problem with the upgrade process, such as: unable to download the upgrade package/no read and write permissions, make sure that the network is connected/OwnCloud Directory has read and write permissions


<a name="17e37f04"></a>
#### Master Program Upgrade

1. Once have upgrade message "OwnCloud" *** is available. Get more information on how to update.", you should upgrade it now
1. Go to Admin->Setting->..，<br />
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-openupdater-websoft9.png#align=left&display=inline&height=678&originHeight=678&originWidth=960&status=done&width=960)
1. Go to Updater<br />
![](http://libs.websoft9.com/Websoft9/DocsPicture/zh/owncloud/owncloud-updater-websoft9.png#align=left&display=inline&height=678&originHeight=678&originWidth=960&status=done&width=960)
1. Click the button "Create a checkpoint" first
1. Click the button "Start"
