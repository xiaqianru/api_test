#从excel中读取数据库
import xlrd   # 只读不写
import os
from config import basedir

class Excel(object):
    def __init__(self,file_name):    #只有文件名file_name，没有路径
        file_path = os.path.join(basedir,"data",file_name)   # 文件的路径
        self.wb = xlrd.open_workbook(file_path)    # 加self变成实例的属性，其他也能用，不然不能用


    def get_sheet_data(self,sheet_name):    # 获取数据，需要一个表的名字
        sh = self.wb.sheet_by_name(sheet_name)  # 打sheet页数据
        # case_list =[]
        # for i in range(1,sh.nrows):
        #     case_list.append(sh.row_values(i))
        return [sh.row_values(i) for i in range(1,sh.nrows)]   #列表推导式，同上面三条

        # [第二行数据，第三行数据，....]






