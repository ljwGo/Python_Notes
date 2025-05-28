'''
mysql 下载地址
https://dev.mysql.com/downloads/repo/apt/

mysql 解压(deb后缀文件)
sudo dpkg -i 文件名

更新软件包资源
sudo apt-get update

最后一步mysql
sudo apt-get install mysql-server

启动mysql:
方式一:sudo /etc/init.d/mysql start
方式二:sudo service mysql start

停止mysql
方式一:sudo /etc/init.d/mysql stop
方式二:sudo service mysql stop

重启mysql
方式一:sudo /etc/init.d/mysql restart
方式二:sudo service mysql restart
'''

'''
# ### windows 安装参照视频
创建一个my.ini文件
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8
[mysqld]
# 设置3306端口
port = 3306
# 设置mysql的安装目录
basedir= 文件路径
# 设置mysql数据库的数据的存放目录
datadir= 上一个文件路径 + /data
# 允许最大连接数
max_connections = 200
# 服务端使用的字符集默认为8比特编码的Latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB

设置好后
以管理员身份运行cmd,进入bin目录，执行
2 初始化，创建mysql默认的roof账户
mysqld --initialize-insecure --user=mysql 命令。不执行这一步，安装完成后无法启动服务
3 执行mysqld install命令安装 完成后会提示安装成功
4 执行net start mysql 命令启动mysql服务
5 修改环境变量，添加之前的文件路径 + \bin
6 cmd中执行 mysql -uroof -p 命令，默认没有密码，回车进入
7 若要卸载，需要先停止服务，再删除
8 停止mysql net stop mysql

mysql 具象化软件
Navicat Premium 12
使用该软件链接linux中的mysql数据库的方法
参照视频
'''