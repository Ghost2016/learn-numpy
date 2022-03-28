#!/usr/bin/env python
#coding: utf-8

# 教程：http://c.biancheng.net/numpy/ndarray.html

import numpy
import numpy as np

# 创建ndarray对象
# numpy.array(object, dtype = None, copy = True, order = None,ndmin = 0)

# 创建一维数组：
a=numpy.array([1,2,3])
print(a)
print(type(a))

# 创建多维数组：
b=numpy.array([[1,2,3],[4,5,6]])
print(b)
print(type(b))

# c=numpy.array([2,4,6,8],dtype="数据类型名称")
c=numpy.array([2,4,6,8],dtype="complex")
print(c)

# ndim查看数组维数
arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]]) 
print(arr.ndim) 

# 使用 ndim 参数创建不同维度的数组：
a = np.array([1, 2, 3,4,5], ndmin = 2)
print(a)