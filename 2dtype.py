#!/usr/bin/env python
#coding: utf-8
import numpy as np 

# NumPy 作为 Python 的扩展包，它提供了比 Python 更加丰富的数据类型，如表 1 所示：

# 表1：NumPy数据类型
# 序号	数据类型	语言描述
# 1	bool_	布尔型数据类型（True 或者 False）
# 2	int_	默认整数类型，类似于 C 语言中的 long，取值为 int32 或 int64
# 3	intc	和 C 语言的 int 类型一样，一般是 int32 或 int 64
# 4	intp	用于索引的整数类型（类似于 C 的 ssize_t，通常为 int32 或 int64）
# 5	int8	代表与1字节相同的8位整数。值的范围是-128到127。
# 6	int16	代表 2 字节（16位）的整数。范围是-32768至32767。
# 7	int32	代表 4 字节（32位）整数。范围是-2147483648至2147483647。
# 8	int64	表示 8 字节（64位）整数。范围是-9223372036854775808至9223372036854775807。
# 9	uint8	代表1字节（8位）无符号整数。
# 10	uint16	2 字节（16位）无符号整数。
# 11	uint32	4 字节（32位）的无符号整数。
# 12	uint64	8 字节（64位）的无符号整数。
# 13	float_	float64 类型的简写。
# 14	float16	半精度浮点数，包括：1 个符号位，5 个指数位，10个尾数位。
# 15	float32	单精度浮点数，包括：1 个符号位，8 个指数位，23个尾数位。
# 16	float64	双精度浮点数，包括：1 个符号位，11 个指数位，52个尾数位。
# 17	complex_	复数类型，与 complex128 类型相同。
# 18	complex64	表示实部和虚部共享 32 位的复数。
# 19	complex128	表示实部和虚部共享 64 位的复数。
# 20	str_	表示字符串类型
# 21	string_	表示字节串类型

# 数据类型对象
# np.dtype(object)
a= np.dtype(np.int64) 
print(a)  

## 数据类型标识码
# NumPy 中每种数据类型都有一个唯一标识的字符码，如下所示：

# 数据类型标识码
# 字符	对应类型
# b	代表布尔型
# i	带符号整型
# u	无符号整型
# f	浮点型
# c	复数浮点型
# m	时间间隔（timedelta）
# M	datatime（日期时间）
# O	Python对象
# S,a	字节串（S）与字符串（a）
# U	Unicode
# V	原始数据（void）

# 创建数据类型score
dt = np.dtype([('score','i1'), ('height','i1')])
print(dt)
# 将上述的数据类型对象 dt，应用到 ndarray 中：
a = np.array([(55,True),(75,False),(85,True)], dtype = dt)
print(a.dtype)
print(a['height'])

# 定义结构化数据
teacher=np.dtype([('name','a20'),('age','i1'),('salary', 'f4')])
print(teacher)
b = np.array([('lyy', 32, 6357.50),('xjl', 28, 6856.80)], dtype = teacher) 
print(b)