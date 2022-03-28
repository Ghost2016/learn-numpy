#!/usr/bin/env python
#coding: utf-8
import numpy as np 

# numpy.empty()
# numpy.empty() 创建未初始化的数组，可以指定创建数组的形状（shape）和数据类型（dtype）
# numpy.empty(shape, dtype = float, order = 'C')
# 它接受以下参数：
# shape：指定数组的形状；
# dtype：数组元素的数据类型，默认值是值 float；
# order：指数组元素在计算机内存中的储存顺序，默认顺序是“C”(行优先顺序)。
arr = np.empty((3,2), dtype = int) 
print(arr)
# 输出结果：
# [[-2305843009213693952 -2305843009213693952]
#  [                   3                    8]
#  [                  24      844424930131976]]
# numpy.empty() 返回的数组带有随机值，但这些数值并没有实际意义。切记 empty 并非创建空数组