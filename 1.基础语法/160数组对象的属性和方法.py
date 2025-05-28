'''
var arr = ["a","b","c","d"];
// 内置属性
console.log(arr.length);
//指定获取下标的成员
console.log(arr[arr.length-1])
//获取最后一个成员

内置方法
concat() 把两个或者多个数组合并

filter() 高阶函数,对数组的每一个成员进行过滤
var arr2 = [4,5,7]
function func(num){
    if(num%2==0){
        return num;
    }
}

var ret = arr2.filter(func);
console.log(ret)

find() 高阶函数,返回符合条件的第一个成员

forEach() 高阶函数,对数组中每一个成员进行遍历
arr2.forEach((iter,key)=>{
    console.log(`成员:${item},下标:${key}`)
})

includes() 查看指定数据是否在数组中存在

indexOf() 判断指定数据在数组中第一次出现的位置

isArray() 判断变量是否是数组
var res = Array.isArray(num);
console.log(res)

join()

map() 对数组中的每一个成员进行处理,返回处理结果
var arr = [1,2,3];
var res = arr.map(function(num){
    return num**3;
})

pop() 出站,删除素组最后一个成员并且将其返回

push() 给数组后面追加成员
var arr = [1,2,3,4];
arr.push("a");
console.log(arr)

reverse() 反转排列
var arr = [1,2]
arr.reverse()
console.log(arr);

slice 切片

sort 排序
var arr = [1,2,3,4,5];
console.log(arr);
arr.sort();
console.log(arr);
是字符的排序,不是熟知的排序

数值升序
var arr = [1,5,2,,55,41];
arr.sort(function(a,b){
    return a-b;
})
console.log(arr)

数值降序
var arr = [1,5,2,,55,41];
arr.sort(function(a,b){
    return b-a;
})
console.log(arr)

splice() 添加或者删除指定的成员 (操作位置的小标,删除操作的成员长度,"替换或者添加的成员1","替换或者添加的成员2")
var arr = [1,2,3];
arr.splice(1,1);
console.log(arr);

unshift() 在数组前面插入指定成员



'''