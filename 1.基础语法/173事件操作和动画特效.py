'''
三种方法:
    1.on 和 off
        绑定事件
        $().on("事件名",function(){})

        解除事件
        $().off("事件名")

    2 直接通过事件名来进行调用
        $().事件名(匿名函数)

    3 组合事件,模拟事件
        $().ready() 入口函数
        $().hover(mouseover,mouseout) 是onmouseover和onmouseout的组合
        $().trigger(事件名) 用于让js自动触发指定元素身上已经绑定的事件

'''