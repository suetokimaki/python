import matplotlib.pyplot as plt
import numpy as np

A = 364.77
B = 0.043
R = 8.314
T1 = 13.1 + 273.15
T2 = 21.5 + 273.15
T3 = 31.1 + 273.15
T4 = 35.5 + 273.15
T5 = 40.0 + 273.15

plt.rcParams['font.size'] = 16  # 字体大小
plt.rcParams['font.sans-serif'] = ['SimHei']

fig = plt.figure(figsize=(9, 9))  # 画布大小9*9

x1 = np.arange(0.05, 0.5, 0.001)  # x1的取值从0.5到10，步长0.1
y1 = ((R*T1)/(x1-B))-(A/(x1*x1))  # 公式
plt.plot(x1, y1, label='T1 = 13.1')  # 绘制x1,y1

x2 = np.arange(0.05, 0.5, 0.001)
y2 = ((R*T2)/(x2-B))-(A/(x2*x2))
plt.plot(x2, y2, label='T2 = 21.5')

x3 = np.arange(0.05, 0.5, 0.001)
y3 = ((R*T3)/(x3-B))-(A/(x3*x3))
plt.plot(x3, y3, label='T3 = 31.1')

x4 = np.arange(0.05, 0.5, 0.001)
y4 = ((R*T4)/(x4-B))-(A/(x4*x4))
plt.plot(x4, y4, label='T4 = 35.5')

x5 = np.arange(0.05, 0.5, 0.001)
y5 = ((R*T5)/(x5-B))-(A/(x5*x5))
plt.plot(x5, y5, label='T5 = 40.0')

plt.xlabel('Vm/L·mol-1')  # x轴标题
plt.ylabel('p/kPa')  # y轴标题
plt.xticks(np.arange(0.05, 0.3, 0.05))  # x轴
plt.yticks(np.arange(5000, 10000, 1000))  # y轴
plt.axis([0.05, 0.3, 5000, 10000])  # 坐标轴范围（x, x, y, y)
plt.title("二氧化碳范氏方程模拟图")  # 设置标题
plt.legend(loc=0, ncol=1)  # 将图例置于右上角

plt.grid(True)

plt.show()
