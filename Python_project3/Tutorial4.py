import numpy as np

# Given data and parameters
alpha = 0.1  # Learning rate
W1 = np.array([[1, 0], [0, 1]])  # Weights for layer 1
W2 = np.array([[1, 0], [0, 1]])  # Weights for layer 2
W3 = np.array([[1, 1]])  # Weights for layer 3
b1 = np.array([[0], [0]])  # Biases for layer 1
b2 = np.array([[0], [0]])  # Biases for layer 2
b3 = np.array([[0]])  # Bias for layer 3
Y = np.array([[2]])  # Actual output
X = np.array([[1], [2]])  # Input


# ReLU activation function
def relu(x):
    return np.maximum(0, x)


# Derivative of ReLU
def relu_derivative(x):
    return np.where(x > 0, 1, 0)


for i in range(100):
    # Forward Propagation
    Z1 = W1.dot(X) + b1
    A1 = relu(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = relu(Z2)
    Z3 = W3.dot(A2) + b3
    A3 = relu(Z3)

    # Compute Loss
    m = Y.shape[0]  # Number of examples, here it's 1
    loss = (1 / m) * np.sum((A3 - Y) ** 2)
    print("loss", i, loss)

    # Backward Propagation
    # Hidden Layer 2
    dA3 = (1 / m) * 2 * (A3 - Y)
    dZ3 = dA3 * 1
    dW3 = dZ3.dot(A2.T)
    db3 = dZ3.dot(np.ones(Z3.shape))

    # Hidden Layer 1
    dA2 = W3.T @ dZ3
    dZ2 = dA2 * relu_derivative(Z2)
    dW2 = dZ2.dot(A1.T)
    db2 = dZ2.dot(np.ones(Z3.shape))

    # Input Layer
    dA1 = W2.T @ dZ2
    dZ1 = dA1 * relu_derivative(Z1)
    dW1 = dZ1.dot(X.T)
    db1 = dZ1.dot(np.ones(Z3.shape))

    # Update Parameters
    W3 = W3 - alpha * dW3
    b3 = b3 - alpha * db3
    W2 = W2 - alpha * dW2
    b2 = b2 - alpha * db2
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1

    if i == 0:
        print("W3=", W3)
        print("b3=", b3)
        print("W2=", W2)
        print("b2=", b2)
        print("W1=", W1)
        print("b1=", b1)
        break
