"""
Assume the prices for soda bottles are as follows:
Large bottle: 5 units each;
Medium bottle: 3 units each;
Small bottle: 1 unit for every three bottles;
With 100 units and the goal of buying exactly 100 bottles of soda, list all possible ways to achieve this

# 方法1
for i in range(0, 21):
    for j in range(0, 34):
        for k in range(0, 101, 3):
            if (5*i+3*j+k/3 == 100) and (i+j+k == 100):
                print("range:", i, "medium:", j, "small:", k)

# 方法2
for i in range(0, 21):
    for j in range(0, 34):
        k = 100 - i - j
        if 5*i+3*j+k/3 == 100:
            print("range:", i, "medium:", j, "small:", k)
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, accuracy_score
import numpy as np
# Read the CSV data into DataFrame
df = pd.read_csv("diabetes-scaled-std (1).csv")
df = df.fillna(-1)
X = df.drop('Outcome', axis=1)
y = df['Outcome']
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# Initialize the Deep Neural Network Classifier
mlp = MLPClassifier(hidden_layer_sizes=(9, 9), max_iter=2000, random_state=0)
# Train the model
mlp.fit(X_train, y_train)
# Predict the outcomes for the test set
y_pred = mlp.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Read the CSV data into DataFrame
df = pd.read_csv("diabetes-scaled-minmax-remove-outlier.csv")
df = df.fillna(-1)
X = df.drop('Outcome', axis=1)
y = df['Outcome']
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# Initialize the Deep Neural Network Classifier
mlp = MLPClassifier(hidden_layer_sizes=(9, 9), max_iter=2000, random_state=0)
# Train the model
mlp.fit(X_train, y_train)
# Predict the outcomes for the test set
y_pred = mlp.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
