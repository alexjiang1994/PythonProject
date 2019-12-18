'''
-*- coding: utf-8 -*-
@Author  : alex_jiang
@Time    : 2019/12/13 15:57
@Software: PyCharm
@File    : common.py
'''
import os
import re


def indexSort(elem):
    a = re.findall(r'第\d*章', elem)
    if not a:
        return float('inf') # 返回一个无穷大的数，表示最大
    else:
        return int(a[0][1:-1])


"""
获取指定目录下的文件
filePath: 要遍历的目录
fileList_out: 要输出的文件列表
file_ext: 文件的拓展名，默认为任何类型的文件"""


def getfilenames(filePath='', fileList_out=[], file_ext='all'):
    # 遍历filePath下的所有文件
    for filename in os.listdir(filePath):
        fi_d = os.path.join(filePath, filename)
        if file_ext == '.doc':  # 遍历word文档文件
            if os.path.splitext(fi_d)[1] in ['.doc', '.docx']:
                # 返回的前者是文件名，后者是后缀
                fileList_out.append(fi_d)

        else:
            if file_ext == 'all':
                fileList_out.append(fi_d)
            elif os.path.splitext(fi_d)[1] == file_ext:
                fileList_out.append(fi_d)
            else:
                pass

    fileList_out.sort(key=indexSort)
    return fileList_out
