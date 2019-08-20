# 故障处理

<a name="f10a43fd"></a>
#### MySQL Service Not Start
The most common reasons why MySQL can't start include: insufficient disk space, insufficient memory, configuration file errors...

```shell
# view the disk space
df -lh

# view the memory used
free -lh
```


<a name="ea1a371d"></a>
#### PhpMyAdmin Timeout Errors
If you try to import a zipped database, you might see a timeout error because phpMyAdmin takes too long to execute the script.To fix this:

- Set the max_execution_time of `php.ini` to larger value
- Try to import the file again.

Remember to change the ExecTimeLimit setting back to its original value once the import process ends.

<a name="657a59cd"></a>
#### Website pictures loading very slowly?
Please make sure that your brandwith of Server is more than 5M

<a name="8504d445"></a>
#### Apache httpd service restart error
Please make sure the vhost.conf is correct for you, and you can track and analyze log files from _/var/log/httpd_<br />_
<a name="e34e1049"></a>
#### Redirects Error
Check your `.htaccess` file in your application root directory, make sure there not any cycle redirects settings
