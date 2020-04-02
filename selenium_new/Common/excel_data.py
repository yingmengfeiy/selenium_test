import xlrd,os


# 读excel操作，所有数据存放在字典中
# filename为文件名
# index为excel sheet工作簿索引
def read_excel(filename, index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    dic = {}
    for j in range(sheet.ncols):
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
        dic[j] = data
    # 返回列表data
    return dic


if __name__ == '__main__':
    # 读取Excel操作，返回字典
    data =read_excel(os.path.split(os.path.realpath(__file__))[0].split('C')[0]+"Data\\testdata.xlsx", 0)
    print(data)
    print(data.get(1))