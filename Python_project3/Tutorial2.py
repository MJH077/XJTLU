import numpy as np
# 得到一个2*2的矩阵
X = np.array([[1, 2], [3, 4]])
print(np.matrix(X))
# inverse 得到x的逆矩阵，逆矩阵与原矩阵相乘可以获得单位矩阵
X_inv = np.linalg.inv(X)
print(np.matrix(X_inv))
# transpose 矩阵的转置，第1行就变成了第1列
X_trans = X.T
print(np.matrix(X_trans))
# multiply
y = [2, 4]
y_mul = y @ X
print(np.matrix(y_mul))
# given dataset
X = np.array([[1, 1.0, 3],
              [1, 1.5, 2],
              [1, 2.0, 4],
              [1, 2.5, 3]])
y = np.array([300, 330, 369, 400])
# applying the normal equation to find theta
theta = np.linalg.inv(X.T @ X) @ X.T @ y
print(theta)

x = np.array([[1, 1500, 3, 10],
              [1, 2000, 4, 5],
              [1, 1800, 3, 20],
              [1, 2200, 4, 2],
              [1, 1300, 2, 30],
              [1, 1600, 3, 15]])
y = np.array([300, 350, 280, 400, 250, 310])
theta = np.linalg.inv(x.T @ x) @ x.T @ y
x_predict = [1, 2300, 4, 1]
y_predict = theta @ x_predict
print(theta)
print(y_predict)
