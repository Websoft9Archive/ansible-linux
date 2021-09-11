# Desktop

Linux desktop environments are the graphical interfaces used to interact with the operating system.  

* The main Linux Desktop Environments: GNOME, KDE, Xfce, Mate 
* The main connection methods: ：Windows remote desktop, VNC

![ubuntu desktop](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/linux-ubuntuui-websoft9.png)

## Connect Desktop

There are two optional graphical login methods as follows:

### Windows remote desktop

Connect Linux desktop is the same with connect Windows Server

1. Log in Cloud platform console, get you **Internet IP Address of Cloud Server**

2. Choose a way to open a local computer remote desktop (three-in-one):  
   - Open **Start** -> **Remote Desktop**
   - Open **Start**, input "mstsc" directly, the system will search for the Remote Desktop
   - Using the keyboard **Windows Logo** + **R** to start the command windows, input input "mstsc" to open the Remote Desktop

3. Input **Internet IP Address of Cloud Server** and click the 【Connect】button
  ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-remoteip-websoft9.png)
  
2. Click the 【Yes】when you see the below reminder  
  ![image.png](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-remotereminder-websoft9.png)
  
3. Then input your Linux credential to connect Linux Server like below
  ![enter image description here](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-xrdp-login-websoft9.png)
 
4. You can see the Desktop when you login successfully

   * **Gnome Desktop**
   ![Gnome Desktop](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-desktop-gnome-websoft9.jpg)
   
   * **KDE Desktop**
   ![Gnome Desktop](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-desktop-kde-websoft9.jpg)

   * **Mate Desktop**
   ![Gnome Desktop](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-desktop-mate-websoft9.png)

   * **Xfce Desktop**
   ![Gnome Desktop](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/linux-desktop-xfce-websoft9.png)

### VNC

VNC (Virtual Network Computing) allows you to remotely control a Linux computer with another computer through a graphical interface. You will be able to observe a Linux desktop environment and interact with it using the mouse and keyboard from a different computer.  

[Websoft9](https://www.websoft9.com) desktop solution have installed vncserver for you, below steps is for your reference:  

1. Use SSH to connect Server and set you VNC password
    ```
    sudo su
    rm -rf /root/.vnc/passwd
    vncpasswd
    ```
2. Install [VNC viewer](https://www.realvnc.com/download/viewer/) on your local computer

3. Login to your cloud console and enable the **5901** port of security group

4. Open your VNC client and create a VNC connection (Server's Internet IP:5901)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/vnc/vnc-connection001-websoft9.png)

5. Click the【Continue】button to next step
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/vnc/vnc-connection002-websoft9.png)

6. Input your VNC password to connection desktop
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/vnc/vnc-connection003-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/vnc/vnc-setlanguage-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/vnc/vnc-startuse-websoft9.png)
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/en/linux/vnc/vnc-gnomehome-websoft9.png)

7. If your Server is locked, please input your **root** password to unlock it
   ![](https://libs.websoft9.com/Websoft9/DocsPicture/zh/linux/vnc/vnc-connection-rootlogin-websoft9.png)

8. More commands for your VNCServer
   ```
   # List all VNC
   vncserver -list

   # Kil a VNC
   kill -9 :1

   # Manage the VNCServer service
   systemctl start vncserver@:1.service
   systemctl stop vncserver@:1.service
   systemctl status vncserver@:1.service
   systemctl restart vncserver@:1.service
   ```


## FAQ

#### Don't know the VNC password?

Please use SSH to connect Server and set your VNC password by the below commands:  

```
vncpasswd
systemctl restart vnc
```

#### Does the locked state of the graphical interface support secret key unlocking?

No

#### Can I modify the Gnome starting logo?

Yes, refer to [here](https://www.dazhuanlan.com/2020/03/01/5e5ab2a1bd7d8/)

#### Which VNC Server is pre-installed?

[TigerVNC](https://github.com/TigerVNC/tigervnc)

#### How does the server using the key pair use remote desktop?

If you want to use Windows remote desktop to connection Linux Desktop, SSH to connect Server and set your root password
```
passwd
```

#### What should I do if I accidentally lock the screen after logging in as root?

The login password cannot be unlocked, you can only log in after restarting the server.  
