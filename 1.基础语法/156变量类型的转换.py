'''
js中,类型转换有两种，一种是强制转换，一种是自动转换
1因为js是一门弱类型的脚本语言，所以变量会在运算符的运行要求，有时候根据运算符的要求，自动进行转换的。//parseInt 把数据转换成整数

转化为数字
//parseFloat 把数据转换成小数
var box1 = "100"
var box2 = parseInt(box1)
console.log(box1);
console.log(box2);
转换失败时，则结果为NAN，NAN也是number类型

转换为字符串
变量.toString()
String(数据)

转换为布尔类型
Boolean()
空数组和空对象的转换值均为true

自动转换
与python相似
var box = 1 + true

var box2 = 1 + "200"
console.log(box2) //1200 原因是，程序中+有两种含义，
第一，两边数值相加，
第二:两边字符串拼接，但是在js中字符串的优先级大于运算符。

var box3 = 1 - "200"
因为-号中表示的就是运算，而没有其它功能

'''