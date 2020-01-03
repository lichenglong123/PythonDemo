import numpy as np
#当函数括号内没有参数时，则返回一个数字数
x=np.random.rand()
#当函数括号内有一个参数时，则返回2个随机数
x2=np.random.rand(2)
#当函数括号内有两个参数时，则返回2行3列的随机数
x3=np.random.rand(2,3)


#当函数括号内没有参数时，则返回一个数字数
y1=np.random.standard_normal()
#当函数括号内有一个参数时，则返回2个随机数
y2=np.random.standard_normal(2)
#当函数括号内有两个参数时，则返回2行3列的随机数,参数为元组
y3=np.random.standard_normal((2,3))

#返回3个值为1的数  ones(shape, dtype=None, order='C')
np.ones(3);
#返回3行2列值为1
np.ones((3,2),dtype=int);
#查看用法
help(np.ones)



