# ### 标签属性和选择符
'''
id
class
可以在单个标签内定义一个唯一的id
一个标签可以指向多个类，类也能指向多个标签

使用内部样式时
可以使用 #id 或 .class{ 属性 }对标签进行修饰

* 代表所有标签

# 关系选择符
1包含选择符
可以控制到内部所有的标签，不管是子级或者隔代

2父子选择符
#id 或者.class > 具体标签名

# 属性选择符
标签 #id .class[属性]

# 伪类选择符
用于控制标签在某一个特殊的环境下的样式
标签名:active{/* 当标签被点击时 */}
标签名:hover{/* 当指针悬停时 */}
标签名:nth-child(1) 处于第一的元素
nth-child(odd) 技术位置的标签 nth-child(even) 表示偶数位置的
last-child 处于最后一个元素

# 伪对象选择符
E:before / E::before
E:after / E::after
E:selection / E::selection

'''

# ### css的属性
'''
文本属性
text-align 文本水平对齐方式
text-indent 文本的首行缩进
letter-spacing 字符间距[一般在图片排版时使用]
vertical-align 文本垂直对齐方式
line-height 文本行高
text-decoration 文本的装饰线

字体属性
font-size 字体
font-family 字体族
font-weight 字体粗细
font-style 字体正斜
font 字体属性的缩写
color 字体颜色

元素外观
opacity 不透明度
border-width 边框的宽度
border-style 边框的样式
border-color 边框的颜色
border
box-shadow 元素的阴影
border-radius 元素的圆角
background-color 背景颜色
background-image 背景图片
background-repeat 背景的平铺方式
background-position 背景定位位置
background-size 背景的大小
background
width 元素的宽度
height 元素的高度
min-width
max-width
min-height
max-height
margin 元素与元素的外边框
padding 元素与子元素或者内容之间的内边框
position 元素的定位
top 定位元素的距离顶部的距离
bottom 定位元素离底部的距离
right 定位元素离右边的距离
left 定位元素离左边的距离
z-index 元素在z轴上的高度[高的元素覆盖低的元素]

布局属性
display 元素的显示模式
float 元素的浮动效果
clear 清除元素的浮动效果
overflow 处理元素的溢出内容效果
flex 设置元素的弹性方式

动画相关
transition 元素切换样式值时的过渡效果
animation 元素的动画效果

列表相关
list-style 列表的项目符号效果

表格属性
border-collapse 表格的边框合并

光标属性
cursor 光标属性
'''