# 1
'''
<link rel='icon' href=''> 设置网页图标
form交互表格标准格式
<form action='' method=''> 两个属性表格连接的对象 客户端发送给服务端请求的方法
    <input type='text' name=''> 文本输入框
    <input type='password' name=''> 设置密码
    <div>
        <input type='checkbox' name='' value=''> 设置多项选项框
    </div>
    <div>
        <input type='radio'> 单选框
    </div>
    <div>
        <input type='button' value='按钮' onclick='alert(123)'> 空白按钮，可以绑定事件，按钮的名称，触发的事件...
    </div>
    <select name='pro' size='3' multiple id=''> 选项栏
        <option value='hebei'>河北省<option>
        <option value='hubei' selected='selected'>湖北省<option>
        <option value='beijing'>北京省<option>

    <input type='file'> 选择文件的发送
    <input type='hidden' name='token' value='ewf'> 隐藏框 用于用户和服务器间识别是否是正常连接
    <input type='reset'> 重设
    <input type='submit'> 提交数据

    <div>
        <textarea name='per' cols='30' rows='10' placeholder=''></textarea>
    </div>

    <p>
        <label for='abc'>姓名</label>
        <input type='text' name='user' id='abc' maxlength='51'>
    </p>
</form>

总结
    点击submit按钮，浏览器会将该form表单中的有效控件的数据组成键值对按着method设置的
    请求方式以及action设置的url最总组成符合http协议格式的字符串发送给对应的服务器
'''