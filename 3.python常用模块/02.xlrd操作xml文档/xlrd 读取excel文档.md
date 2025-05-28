[toc]

# xlrd 读取excel文档(xls和xlsx格式)

## file = xlrd.open_workbook(相对路径或绝对路径) 打开excel文件(一个book.Book对象)

## file.sheets() 获取excel文件下的所有工具表对象(sheet.Sheet对象)

## file.sheet_names() 获取所有sheet工具表的名字

```python
import xlrd

xls_file = xlrd.open_workbook("test.xls")

print(xls_file.sheets())
print(xls_file.sheet_names())
```



### file.sheet_by_index 通过索引获取sheet对象

### file.sheet_by_name 通过sheet文件名获取sheet对象

### file.sheet_loaded(sheet文件名或索引) 判断sheet是否导入成功

```python
import xlrd

xls_file = xlrd.open_workbook("test.xls")
print(xls_file.sheet_by_index(0))
print(xls_file.sheet_loaded("Sheet2"))

# sheet在workbook命令执行后就已经载入了,而非by_index和by_name
Sheet  0:<Sheet1>
True
```



## 单元格数据类型

| 标识 |                 描述                 |
| :--: | :----------------------------------: |
|  0   |             empty表示空              |
|  1   |           string表示字符串           |
|  2   |          number表示数值类型          |
|  3   |             date日期类型             |
|  4   |             bool布尔类型             |
|  5   | error错误(可能是excel表不识别的数据) |



## 单元格类型中的错误(一般是函数参数类型错误)

> 具体参考
>
> [【Excel】Excel错误值大全（一） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/30886044)



## 行操作

### 一般索引都是从0开始的

### sheet.nrows 获取sheet中有效行数

### sheet.row_values(行索引, 可选开始列数, 可选结束列数) 获取指定行的指定列数据

```python
import xlrd

xls_file = xlrd.open_workbook("test.xls")
sheet_obj = xls_file.sheet_by_name("Sheet1")

if sheet_obj.nrows > 0:
    row_cells_list = sheet_obj.row_values(0)
    for i in row_cells_list:
        print(i)


str
123.0
44199.0
0
36
```



### sheet.row(行索引) 获取指定行的所有单元

### sheet.row_slice(行索引, 可选开始列数,可选结束列数) 获取指定行的指定单元格

```python
import xlrd

xls_file = xlrd.open_workbook("test.xls")
sheet_obj = xls_file.sheet_by_name("Sheet1")

if sheet_obj.nrows > 0:
    row_cells_list = sheet_obj.row_slice(0, 1, 3)  # 不包含结束索引
    for i in row_cells_list:
        print(i)

text:'str'
number:123.0
```



### sheet.row_types(行索引, 可选开始列数,可选结束列数) 获取指定行指定单元格的数据类型

```python
import xlrd

xls_file = xlrd.open_workbook("test.xls")
sheet_obj = xls_file.sheet_by_name("Sheet1")

if sheet_obj.nrows > 0:
    row_cells_list = sheet_obj.row_types(0, 1, 3)
    for i in row_cells_list:
        print(i)

1
2
```



### sheet.row_len(行索引) 获取指定行的单元格长度

```python
import xlrd

xls_file = xlrd.open_workbook("test.xls")
sheet_obj = xls_file.sheet_by_name("Sheet1")

if sheet_obj.nrows > 0:
    row_len = sheet_obj.row_len(0)
    print(row_len)

6
```



## 列操作

### sheet.ncols 获取sheet中有效列数

### sheet.col_values(colx,  start_rowx, end_rowx) 获取指定列的指定行数据

### sheet.col_slice(colx, start_rowx, end_rowx) 获取指定行的指定单元格

### sheet.col_types(colx, start_rowx, end_rowx) 获取指定行指定单元格的数据类型



## 单元格操作

### sheet.cell(rowx, colx) 获取指定单元格对象

### sheet.cell_value(rowx, colx) 获取指定单元格的值

### sheet.cell_type(rowx, colx) 获取指定单元格的单元类型



## 单元格对象和单元格

> 其实并**不是真正的对象**
>
> 而是**具有一定格式的数据**
>
> 格式为 **单元类型:单元值**

```python
import xlrd

xls_file = xlrd.open_workbook("test.xls")
sheet_obj = xls_file.sheet_by_name("Sheet1")

if sheet_obj.nrows > 0:
    row_cells_list = sheet_obj.row(0)
    for i in row_cells_list:
        print(i)

"""
输出结果
	empty:''
	text:'str'
	number:123.0
	xldate:44199.0
	bool:0
	error:36
"""
```



## 读取日期类型的方式

### xlrd.xldate_as_tuple(日期和时间, 格式)将时间和日期转换为适用于datetime模块的元组

### xlrd.xldate_as_datetime(日期和时间,格式) 将时间和日期转换为格式化时间输出

```python
import xlrd
import datetime

xls_file = xlrd.open_workbook("test.xls")
sheet_obj = xls_file.sheet_by_name("Sheet1")

# 判断单元格是否是日期格式
# print(sheet_obj.cell_type(0, 3))
if sheet_obj.cell_type(0, 3) == 3:
    date_value = sheet_obj.cell_value(0, 3)
    print(date_value)
    date_time = xlrd.xldate_as_datetime(date_value, xls_file.datemode)
    print(date_time)
    date_tuple = xlrd.xldate_as_tuple(date_value, xls_file.datemode)
    print(date_tuple)
    # 传入的是一系列实参
    date = datetime.date(*date_tuple[:3])
    print(date)
    # 使用strftime格式化输出时间
    format_date = date.strftime("%Y/%m/%d")
    print(format_date)

"""
输出结果
	44199.0
	2021-01-03 00:00:00
	(2021, 1, 3, 0, 0, 0)
	2021-01-03
	2021/01/03
"""
```



## 对单元格合并以及详情具体参考

> [python：xlrd模块 - 简书 (jianshu.com)](https://www.jianshu.com/p/f2c9dff344c6)
