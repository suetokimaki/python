#求逆矩阵
import numpy as np
 
kernel = np.array([0.8, -0.2, -0.214,  -0.16, 0.7667,-0.142,  -0.32,-0.183,0.8714]).reshape((3, 3))
print(kernel)
print(np.linalg.inv(kernel))
