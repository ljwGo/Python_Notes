# ctrl + l 清屏
### 安装vm-tools
# 1 进入文件夹vmware-tools ..,
# 2 鼠标右键 -> 打开终端
# 3 sudo ./vmware-install.pl(输入vm后点击Tab键补全文件名)
# 4 yes(除第一个为yes,其他全为默认)
# 5 enjoy 代表完成
# 6 reboot 重启

# 测试自己电脑是否可以上网
# ping www.baidu.com

# 输入python3查看版本

# exit , exit()退出

# sudo add-apt-repository ppa:jonathonf/python-3.6 (如果超时,在运行一次)
# sudo apt-get updata (更新软件列表,拿去最新资源)
# sudo apt-get install python3.6 (安装python3.6版本)
# 调整python3的优先级,使得3.6优先级较高
# sudo updata-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
# sudo updata-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

# 验证结果: 右键打卡终端 -> 输入 python3 -> 如果出现如下3.6.7 版本的提示,证明安装成功,exit()退出
#	Python 3.6.7(default,Oct 25 2018, 09:16:13)
#	[GCC 5.4.0 20160609] on linux
#	Type 'help','copyright','credits'or'license' for more information.
#	>>>


### 设置共享文件夹
# 虚拟机,设置,选项,共享文件夹 , 添加共享文件夹(盘符较大的位置 启用->添加->确定)
# cd /mnt/hgfs/gongxiang8 gongxiang8 出现了共享的数据,代表设置成功 (ls查看)

# cd 切换目录 / 根目录 ls 查看目录
'''
/bin 存放普通用户的命令文件
/boot 存放系统启动文件
/cdrom 存放读取光盘的相关文件
/dev 设备文件
/etc 配置文件
/home 家目录
/lib 库文件
/lib64 64库文件
/lost+found 系统异常产生错误是,丢失文件放在这
/media 媒体目录
/mnt 挂载目录
/opt 安装软件时的默认目录
/proc 内存中相关数据文件
/root root用户登录的家目录
/run 系统运行时候 用到的文件
/sbin 服务启动之后需要访问的数据目录
/sys 系统文件
/tmp 应用程序存放目录
/var 放置系统执行过程中经常变化的文件,如随时更改的日志文件

linux 系统中 一切皆文件
(常用的比如:普通文件,目录文件,链接文件,设备文件)
'''

'''
相对路径:
.	相对于当前路径
..	相对于上一级路径
结对路径:
以/开头的就是结对路径

pwd 查看当前路径
cd .. 回到上一级
cd 切换目录 /home/wangwen
cd - 回到上一个你操作的那一个目录
cd ~ 回到家目录
cd 默认切换到家目录
. 但凡是点开头的文件 都是隐藏文件

-a all 所有文件(包括隐藏文件) ls -a
-l list 以列表的形式呈现
-h 可以让文件大小带上单位
ll 相当于 ls -al
man是帮助命令 比如:man ls 或 man cp

mkdir 文件夹名称(创建文件夹)
touch 创建文件
ln -s 创建连接 (ln -s 指定你想要创建的连接,放到那个目录下面,需要绝对路径)
ifconfig 查看linux下面的ip

mkdir ceshi100 创建文件夹(目录)
cd ceshi100 切换目录
touch 111.txt 创建文件
ln -> link 链接 -s soft
ln -s 路径1 路径2
ln -s /home/laijianwei/ceshi100 /home/laijianwei/ceshi200

# centos redhat ubuntu linux分支













'''



