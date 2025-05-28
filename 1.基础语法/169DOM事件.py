'''
所谓事件,就是用户对浏览器进行的一次操作,例如:用户点击了按钮,这就是一次事件,用户移动了鼠标,或者按下了
键盘,都是不同的事件.
在js中,提供了Event对象,可以让我们开发者在用户浏览器进行指定的行为时,可以自动执行某些代码
常用事件类型
1 鼠标事件
click 鼠标点击事件
mouseover 鼠标悬浮事件
mousedown 鼠标按下
mouseup 鼠标松开

2 表单事件
onblur 输入框失去焦点事件
onfocus 输入框获取焦点事件
onsubmit 表单提交事件
onchange 输入框改变事件

3 页面窗口事件
onload 页面加载事件

4 键盘事件
onkeydown 键盘按下
onkeyup 键盘松开

//时间的绑定
<button onclick="show()">按钮</button>

function show(){
    console.log("点击了");
}

一个元素可以绑定多个不同的事件,但是如果多次绑定同一个事件,则后面的事件代码会覆盖前面的事件代码.

block 块级元素的移动

对于一个元素绑定事件有两种写法
1 静态绑定,直接把事件写在标签元素中
<button onmouseover="">按钮<button>
2 动态绑定 在js中通过代码获取元素对象,然后给这个对象进行后续绑定
'''