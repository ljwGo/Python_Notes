# ### 对象 字符串对象
'''
<script>
var = "hello";
console.log(str);

字符串的对象内置属性
length 计算字符串的长度
console.log(str.length);
字符串对象内置方法
toUpperCase(); 字母大写转换
toLowerCase(); 字母小写转换

indexOf 获取指定字符在字符串中第一次出现的索引值
console.log(str.indexOf("e"));

match 正则匹配
var str = str.match(/\d{11}/);

replace 正则替换
var ret = str.replace(/.*?/,"$1****$2"):; 正则$1$2表示的是第二个小括号捕获的内容
console.log(ret);

search 正则查找,如果找不到,则返回-1

slice 切片

split 分割

substr 截取

trim 一处字符串首尾空白

'''