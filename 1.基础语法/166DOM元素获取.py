'''
DOM document Object Model 文档对象类型
主要提供给开发者用于操作网页的标签,css内容的一些方法或者数据
# 获取元素 [2种方式]
直接获取元素
var box = document.getElementById("box"); 通过id值获取元素
var p1 = document.getElementsByClassName("p1"); 获取指定class值得所有元素,返回值是一个html元素对象,是类似数组的对象
var p2 = document.getElementsByTagName("div"); 根据标签名来获取所有对应的元素
var p3 = document.getElementsByName("username"); 根据name数值来获取所有的元素[一按只会使用表单项,所以很少使用]
var p4 = document.querySelector(".p1") 根据css选择符来获取查找到的第一个元素
var p5 = document.querySelector("input[name=username]")
var p6 = document.querySelectorAll("input") 根据css获取所有值

间接获取元素
一个元素和另一个元素之间如果存在父子嵌套或者兄弟并列的情况下才可以使用
整个html文档,会保存一个文档对象document
console.log(document); 获取当前文档对象
console.log(document.documentElement); 获取html根标签
.children[0] 获取当前标签下的子标签

获取一个标签的后面的兄弟节点[节点:node,表示组成网页的html内容,包括了元素,元素的属性,元素的内容以及元素与元素之间的空白部分]
var input_next = 标签名.nextSibling

获取元素的父元素
var p0 = password.parentElement;
获取下一个元素兄弟
var p1 = p0.nextElementSibling;
获取上一个元素兄弟
var p2 = p1.previousElementSibling;
'''