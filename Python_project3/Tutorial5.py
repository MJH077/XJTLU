import numpy as np


# Sigmoid activation function 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Derivative of Sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)


# ReLU activation function
def relu(x):
    return np.maximum(0, x)


# Derivative of ReLU
def relu_derivative(x):
    return np.where(x > 0, 1, 0)


# Mean Squared Error loss
def binary_cross_entropy_loss(y_true, y_predicted):
    y_predicted = np.clip(y_predicted, 1e-7, 1 - 1e-7)
    loss = -np.mean(y_true * np.log(y_predicted) + (1 - y_true) * np.log(1 - y_predicted))
    return loss  # Data: Normalize for simplicity in this example


def binary_cross_entropy_loss_derivative(y_true, y_predicted):
    return ((1 - y_true) / (1 - y_predicted) - (y_true / y_predicted)) / y.shape[1]


X = np.array([
    [3.5, 3, 4],
    [1, 3, 0],
])  # Shape: 2x3

y = np.array([[1, 0, 1]])
# Output: Admitted (1) or Not Admitted (0), no normalization applied here for output

# Initialize weights and biases
np.random.seed(42)
W1 = np.ones((3, 2))  # Input to Hidden Layer Weights
b1 = np.zeros((3, 1))  # Hidden Layer Biases
W2 = np.ones((1, 3))  # Hidden to Output Layer Weights
b2 = np.zeros((1, 1))  # Output Layer Bias

# Training parameters
learning_rate = 0.1
epochs = 1000  # Number of iterations

for epoch in range(epochs):
    # Forward pass
    Z1 = np.dot(W1, X) + b1
    A1 = relu(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)

    # Compute the loss
    loss = binary_cross_entropy_loss(y, A2)

    # Backward pass
    dA2 = binary_cross_entropy_loss_derivative(y, A2)
    dZ2 = dA2 * sigmoid_derivative(A2)
    dW2 = dZ2.dot(A1.T)
    db2 = dZ2.dot(np.ones((1, Z2.shape[1])).T)

    dA1 = W2.T @ dZ2
    dZ1 = dA1 * relu_derivative(Z1)
    dW1 = dZ1.dot(X.T)
    db1 = dZ1.dot(np.ones((1, Z1.shape[1])).T)

    # Update weights and biases
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    print("W2=", W2)
    print("b2=", b2)

    print("W1=", W1)
    print("b1=", b1)

    break

# Output final weights and biases after training
# print(W1)
# print(b1)
# print(W2)
# print(b2)

# Forward pass
# Z1 = np.dot(W1, X) + b1
# A1 = relu(Z1)
# Z2 = np.dot(W2, A1) + b2
# A2 = sigmoid(Z2)


# print(A2)