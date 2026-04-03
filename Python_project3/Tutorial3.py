import numpy as np
x, w1, w2, b1, b2 = [np.array(arr) for arr in ([[3.5, 3.0, 4.0], [1, 3, 0]], [[1.5, -1.5], [0.3, 1.7], [-0.2, -0.2]], [2.6, -1, -0.5], [[0.2], [-0.1], [0]], [-0.1])]
"""
x = np.array([[3.5, 3.0, 4.0], [1, 3, 0]])
w1 = np.array([[1.5, -1.5], [0.3, 1.7], [-0.2, -0.2]])
w2 = np.array([[2.6, -1, -0.5]])
b1 = np.array([[0.2], [-0.1], [0]])
b2 = np.array([-0.1])
"""
def relu(x):
    return np.maximum(x, 0)
def sigmoid(x):
    return 1/(1 + np.exp(-x))
y = sigmoid(w2@relu(w1@x+b1)+b2)
"""
a1 = relu(w1 @ x + b1) y = sigmoid(w2 @ a1 + b2)
"""
print("y-hat: ", y)
# y-hat:  [0.99945816 0.00415202 0.99999967]