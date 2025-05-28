# ### 常用标签
"""
标准的标签格式
<!DOCTYPE html> 用于确定浏览器识别数据的模式
<html lang='en'>
<head>
    <meta charater = 'utf-8'>
    <title>myserver<title>
</head>
<body>
    网页代码逻辑
    ...
</body>
</html>

<meta charset='utf_8'> 设置编码集
<title>明日方舟<title>
<link rel='icon' href=''> 设置图标
<meta name='keywords' content='meta总结'> 再浏览器中设置索引字段
<meta name='description' content='非常难'> 设置备注描述
<meta http-equiv='Refresh' content='2;URL=https://www.oldboy.com'> 设置刷新界面

## 页面标签
# 基本标签
块级标签
    1独占一行
    2可设置长宽
<h1>一级标签</h1>
<h2>二级标签</h2>
<h3>三级标签</h3>
<h4>四级标签</h4>
<h5>五级标签</h5>
<h6>六级标签</h6>
<hr> 显示分割线

<br> 换行标签
<p></p> 分段落标签

内联标签
    1只占用内用部分
<b></b> 字体变粗标签
<i></i> 字体变斜标签

标签嵌套基本原则:
    块级标签可以嵌套块级标签，也可以嵌套内联标签:内联标签只能嵌套内联标签

&nbsp 空格的特殊符号

<img 图片 src='' 路径 alt 图片加载失败时显示 title 鼠标移动到图片时显示 height 图片高度 width 图片宽度>

<a href=''></a> 超链接标签
'''
href 所谓的超链接是指从一个网页指向一个目标的连接关系，这个目标可以是另一个网站，也可以是相同网页上
的不同位置，还可以是一个图片，一个电子邮件地址，一个文件，甚至是一个应用程序
'''
属性:
    target = '_blank' 设置不关闭当前页面，另开启其他标签

无序列表
<ul>
    <li>111</li> 列表单项
    <li>111</li> 列表单项
    <li>111</li> 列表单项
    <li>111</li> 列表单项
</ul>

有序列表
<ol>
    <li>111</li>
    <li>111</li>
    <li>111</li>
<ol>

表格
# border = 'l'显示边框
<table>
    <thead>
        <tr>
            <td>姓名</td>
            <td>年龄</td>
            <td>薪水</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>张三</td>
            <td>23</td>
            <td>3000</td>
        </tr>
        <tr>
            <td>李四</td>
            <td colspan='2' 具体数据独占两列>50</td>
            <td rowspan='2' 具体数据独占两行>5000</td>
        </tr>
    </tbody>
</table>












"""

