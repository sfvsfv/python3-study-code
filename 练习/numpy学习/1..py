# 1.
# import numpy as np
#
# a = np.array([1, 2, 3])
# print(a)


# 1.	object 任何暴露数组接口方法的对象都会返回一个数组或任何（嵌套）序列。
# 2.	dtype 数组的所需数据类型，可选。
# 3.	copy 可选，默认为true，对象是否被复制。
# 4.	order C（按行）、F（按列）或A（任意，默认）。
# 5.	subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
# 6.	ndmin 指定返回数组的最小维数。


#2. 多于一个维度
# import numpy as np
#
# a = np.array([[1, 2], [3, 4]])
# print(a)


# 3.最小维度2
# import numpy as np
#
# a = np.array([1, 2, 3, 4, 5], ndmin=2)
# print(a)


# 4.dtype 参数
# import numpy as np
#
# a = np.array([1, 2, 3], dtype=complex)  #https://www.cnblogs.com/hhh5460/p/5129032.html 学习dtype各种类型
# print(a)


# 5.使用数组标量类型
# import numpy as np
# #
# # dt = np.dtype(np.int32)
# # print(dt)


# 6.int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，'i8'
# import numpy as np
#
# dt = np.dtype('i8')
# print(dt)


# 7.使用端记号
# import numpy as np
#
# dt = np.dtype('>i2')
# print(dt)


# 8.首先创建结构化数据类型。
# import numpy as np
#
# dt = np.dtype([('age', np.int64)])  #int8==i1,int16==<i2,int32==<i4,int64==<i8就这四个
# print(dt)


# 9.现在将其应用于 ndarray 对象
# import numpy as np
#
# dt = np.dtype([('age', np.int8)])
# a = np.array([(10,), (20,), (30,)], dtype=dt)
# print(a)


# 10.文件名称可用于访问 age 列的内容
# import numpy as np
#
# dt = np.dtype([('age', np.int8)])
# a = np.array([(10,), (20,), (30,)], dtype=dt)
# print(a['age'])

# 11.定义名为 student 的结构化数据类型，其中包含字符串字段name，整数字段age和浮点字段marks
# import numpy as np
#
# student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
# print(student)


# import numpy as np
#
# student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
# a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
# print(a)

#12.ndarray.shape这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。
# import numpy as np
#
# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a.shape)

# print(a)


# 13.这会调整数组大小
# import numpy as np
#
# a = np.array([[1, 2, 3], [4, 5, 6]])
# a.shape = (3, 2)
# print(a)

#NumPy 也提供了reshape函数来调整数组大小。

# import numpy as np
#
# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = a.reshape(3, 2)
# print(b)

# 数组的 dtype 为 int8（一个字节）
# import numpy as np
# x = np.array([1,2,3,4,5], dtype = np.int16)
# print (x.itemsize)

# 数组的 dtype 现在为 float32（四个字节）
# import numpy as np
# x = np.array([1,2,3,4,5], dtype = np.float32)
# print (x.itemsize)



# 1.	C_CONTIGUOUS (C) 数组位于单一的、C 风格的连续区段内
# 2.	F_CONTIGUOUS (F) 数组位于单一的、Fortran 风格的连续区段内
# 3.	OWNDATA (O) 数组的内存从其它对象处借用
# 4.	WRITEABLE (W) 数据区域可写入。 将它设置为flase会锁定数据，使其只读
# 5.	ALIGNED (A) 数据和任何元素会为硬件适当对齐
# 6.	UPDATEIFCOPY (U) 这个数组是另一数组的副本。当这个数组释放时，源数组会由这个

# import numpy as np
# x = np.array([1,2,3,4,5])
# print (x.flags)


# numpy.empty(shape, dtype = float, order = 'C')   构造函数

# import numpy as np
# x = np.empty([3,2], dtype =  int,order='C')
# print (x)

# 含有 5 个 0 的数组，默认类型为 float
# import numpy as np
# x = np.zeros(5)
# print(x)

# import numpy as np
# x = np.zeros((5,), dtype = np.int)
# print (x)

# 自定义类型
# import numpy as np
# x = np.zeros((2,2), dtype =  [('x',  'i2'),  ('y',  'i2')])
# print(x)

# 含有 5 个 1 的数组，默认类型为 float
# import numpy as np
# x = np.ones(5)
# print(x)

# import numpy as np
# x = np.ones([1,4], dtype =  int)
# print(x)

# 将列表转换为 ndarray
# import numpy as np
#
# x =  [1,2,3]
# a = np.asarray(x)
# print(a)

# 设置了 dtype
# import numpy as np
# x =  [1,2,3]
# a = np.asarray(x, dtype =  float)
# print(a)

# 来自元组的 ndarray
# import numpy as np
#
# x =  (1,2,3)
# a = np.asarray(x)
# print(a)

# 来自元组列表的 ndarray
# import numpy as np
# #
# # x =  [(1,2,3),(4,5)]
# # a = np.asarray(x)
# # print(a)

#numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)此函数将缓冲区解释为一维数组。 暴露缓冲区接口的任何对象都用作参数来返回ndarray。
# 1.	buffer 任何暴露缓冲区借口的对象
# 2.	dtype 返回数组的数据类型，默认为float
# 3.	count 需要读取的数据数量，默认为-1，读取所有数据
# 4.	offset 需要读取的起始位置，默认为0

# numpy.arange(start, stop, step, dtype)包含给定范围内的等间隔值。

# import numpy as np
# x = np.arange(5)
# print(x)

# import numpy as np
# # 设置了 dtype
# x = np.arange(5, dtype =  float)
# print(x)