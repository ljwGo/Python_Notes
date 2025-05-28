'''
获取和操作元素的样式,首先我们要明白,样式有行内和行外[内部和外部样式]之分
获取元素的行内样式
var box = document.getElementByClassName("类名")[0];
console.log(box.style.width);
console.log(box.style.background-color)是错误的,如果获取的css属性是多个单词,则横杠必须去掉,横杠后面的单词首字母要大写

//web中,表示颜色样式有三种方式:单词,rgb,十六进制表示法
rgb (255,0,0)
三个参数表示的是三种单元色(r red 红色 g green 绿色 b blue 蓝色)颜色的深浅度

console.log(box.style.border); 无法通过style来获取行外的样式

获取元素的行外样式 window.getComputedStyle()来进行获取指定元素的所有样式
console.log(window.getComputedStyle(box).border); 获取到内部部样式
console.log(window.getComputedStyle(box).fontSize); 获取对象box内部样式中的font-size属性
console.log(window.getComputedStyle(box)["fontsize"]); 获取到内部样式,js中所有的对象都可以用数组的格式来表示

//修改样式
var btn1 = document.getElementById("btnl");
btn1.onclick = function(){
    var box = document.getElementsByClassName("box")[0];
    box.style["background-color"] = "#000000";
    box.style.backgroundColor = "#000000";
}

var btn2 = document.getElementById("box2");
btn2.onclick = function(){
    var box2 = document.getElementsByClassName("box")[0];
    box2.style.display = "none";
}

var btn3 = document.getElementById("box3");
btn3.onclick = function(){
    var box3 = document.getElementsByClassName("box")[0];
    box3.style.display = "block";

动态变化
var btn4 = document.getElementById("box4");
btn4.onclick = function(){
    var box = document.getElementByClassName("box")[0];
    let point = 0;
    let t = setInterval(function(){
        box.style.borderRadius = `${point}%`;
        if(point<50){
            point+=1;
        }
        else{
            clearInterval(t)
        }
    },25);
}

也可以通过class属性,采用字符串拼接的方式来完成样式的修改
标签对象.className+=" box2",在css中的类名中添加新的类分组
[因为js中存在与css中class的关键字,所以在js中一律使用classname对应css中的class]
'''