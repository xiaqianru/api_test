import xlrd


# 打开excel
wb = xlrd.open_workbook("../data/加油卡完整用例.xls")   #打开xls文件

# sh = wb.sheet_by_index(0)    # 用索引定位，不推荐
sh = wb.sheet_by_name("添加加油卡")   #用sheet页的名字定位

print(sh.nrows)   # 输出行数
print(sh.ncols)   # 输出列数
print(sh.cell(0,0).value)  # 获取A1单元格的值
title = sh.row_values(0)   #获取一行数据
case_data = sh.row_values(1)
data = dict(zip(title,case_data))    # 组合成一个字典，也可以组合成list，data = list(zip(title.case_data))
print(data)
url = data["接口地址(名称)URL"]
data2 = data["入参"]
print(url)
print(data2)





