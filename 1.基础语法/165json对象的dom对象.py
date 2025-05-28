'''
js经常会接收到来自其他服务端的数据,这些数据往往都是通过http协议或者websocket发送过来的.
而数据发送过来给到js的格式,往往就是json格式.json翻译成中文为 javascript对象表示法

json是一种数据格式,语法
必须是{}或者[]包含起来
内部成员以英文逗号隔开,最后一个成员不能使用逗号
可以是结对之,也可以是列表成员
内容样式,一般是数值,数组,另外一个json,字符串
json中的成员如果是键值对,则简明必须是字符串.而json中的字符串必须使用双引号圈起来
json数据也可以保存到文件中,一般以.json结尾
前端项目中,一般使用json作为配置文件

{
    "name":"xiaoming",
    "age":12
    "son":{
        "name":"xiaohuihui",
        "age":2
    }
    [22,52,8,48]
}

javascript中,提供了一个json对象,可以让我们把数据转化成json数据,也可以把json数据转化成对象格式

实例
    js对象,因为这种声明的对象格式很像json,所以也叫json对象
    var data = {
        name:"xiaoming",
        age:22
    }

    把json对象转换成json字符串
    var ret = JSON.stringify(data);
    把json字符串转换成json对象
    var str = JSON.parse(ret)

.xml 早期用于不同语言的数据交流中
<name>xiaoming</name>
<age>17</age>
'''

'''
BOM操作
全称 Browser object model
浏览器提供我们开发者在javascript用于操作浏览器的对象

### window对象
js中最大的对象,整个浏览器中窗口出现的所有东西都是window对象的内容
console.log(window);
alter 弹出窗口
alter("hello")

var ret = confirm("您确定要删除当前文件么?")
确认返回true,取消返回false

prompt("弹出一个消息输入框")
可以接收到用户在输入框中填写的内容,如果取消则返回null

窗口的内部宽高
window.innerHeight()
window.innerWidth()

打开一个新的浏览器窗口
window.open("http://www.baidu.com","_self",500,500);

window.close();关闭浏览器

计时器[间隔函数,这种函数可以让我们指定某一段代码指定以后执行一次或者多次]
//定时执行多次
function func(){
    num += 1;
    console.log(num);
}
window.setInterval(func,1000);  [函数名,间隔时间s] # 1000单位为毫秒

//定时执行一次 setTimeout
//取消定时 window.clearInterval() window.clearTimeout()

在js中,我们生命的的全局变量或者函数

### navigator 浏览器信息对象
console.log(navigator.appVersion);

### history
console.log(history);
console.log(history.length); //历史纪录的页面数量
history.back()返回上一页 相当于history.go(-1)
history.forward()返回下一页 相当于history.go(1)
刷新页面 history.go(0)

console.log(location);
地址栏对象控制和操作地址栏
所谓地址就是当前页面所在地址
地址结构;
协议://域名:端口/路径/文件名?查询字符串#描点
location.href 获取网页路径全部信息

<p onclick="func1" ></p>
<script>
    function func1(){
        location.href="网站地址"
        //location.assign("网站地址")
    }
</script>

location.reload() 刷新页面

localStorage 本地永久存储
localStorage.setItem("变量名","变量值"); 保存一个数据到存储对象
localStorage.变量名 = 变量值

localStorage.getItem("变量名"); 获取存储对象中保存的指定变量对应的数据
localStorage.变量名

localStorage.removeItem("变量名") 从存储对象中删除一个指定变量对应的数据
localStorage.clear()

sessionStorage 本地会话存储
'''






