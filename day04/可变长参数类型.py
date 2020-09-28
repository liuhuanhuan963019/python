#encoding=utf-8

def getComputer(*arcgis):    #只有一个参数的时候，会自动在后面加上一个逗号，当作元组来处理
    '''
    :param arcgis: 可变长的参数类型
    :return:
    '''
    # print(arcgis)
    result = 0
    for item in arcgis:
        result += item
        pass
    print(result)
    pass

getComputer(1)
getComputer(1,2,3,4)
getComputer(1,4,5,6,7)