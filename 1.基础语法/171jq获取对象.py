'''
jQuery提供了大量让开发者获取页面元素的方法,都是通过$()函数来完成的.返回值都是一个jQuery对象,也叫jQuery集合.是一个伪数组对象.
基本
    #id id选择符
    element 元素选择符
    .class class选择符
    * 万能选择符
    select1,select2,selectN 同时获取多个元素的选择符

层级
    ancestor descendant #包含选择符
    parent > child # 父子选择符
    prev + next # 下一个兄弟选择符
    prev ~ siblings # 兄弟选择符

基本
    :first 从获取的元素集合中提取第一个元素
    :even 从获取的元素集合提取下标为偶数的元素
    :odd 从获取的元素集合提取小标为奇数的元素
    :eq(index) 从获取的元素集合提取指定下标index对应的元素
    :gt(index) 从获取的元素集合提取下标大于index对应的元素
    :last 从获取的元素集合提取最后一个元素
    :lt(index) 从获取的元素集合提取下标小于index对应的元素

内容
    :has(selector) 从获取的元素集合提取拥有指定选择符的元素

属性
    []
...


'''