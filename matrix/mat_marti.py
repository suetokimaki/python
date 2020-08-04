# 矩阵乘法计算器
import numpy as np

#data1
i = 2
j = 2
data1 = [1/3, -1/3, -1/5,  2/5]
kernel1 = np.array(data1).reshape((i, j))

#data2
k = 2
l = 1
data2 = [3,2]
kernel2 = np.array(data2).reshape((k, l))

ans = np.dot(kernel1,kernel2)
print(ans)
