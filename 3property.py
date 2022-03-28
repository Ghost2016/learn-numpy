#!/usr/bin/env python
#coding: utf-8
import numpy as np 

# ndarray.shape
# 2 行 3 列
a = np.array([[2,4,6],[3,5,7]])
print(a.shape)
# 通过 shape 属性修改数组的形状大小： 
a.shape = (1,6)
print(a)

# ndarray.reshape()
# 一个调整数组形状的 reshape() 函数。
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(6,1)
print(b)

# ndarray.ndim
# 返回的是数组的维数
#随机生成一个一维数组
c = np.arange(24)
print(c)
print(c.ndim)
#对数组进行变维操作
e = c.reshape(2,3,4)
print(e)
print(e.ndim)

# ndarray.itemsize
# 返回数组中每个元素的大小（以字节为单位）
#数据类型为int8，代表1字节
x = np.array([1,2,3,4,5], dtype = np.int8)
print (x.itemsize)
#数据类型为int64，代表8字节
x = np.array([1,2,3,4,5], dtype = np.int64)
print (x.itemsize)

# ndarray.flags
x = np.array([1,2,3,4,5])
print (x.flags)