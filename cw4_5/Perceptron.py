import numpy as np


def step(x):
    return np.where(x >= 0, 1, 0)


def perceptron_learn(inputs, targets, learning_rate, epochs):
    weights = np.zeros(inputs.shape[1])

    for epoch in range(epochs):
        for input, target in zip(inputs, targets):
            output = step(np.dot(input, weights))
            error = target - output
            weights += learning_rate * error * input

    return weights


and_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
and_targets = np.array([0, 0, 0, 1])

and_weights = perceptron_learn(and_inputs, and_targets, 0.1, 100)

and_outputs = step(np.dot(and_inputs, and_weights))
print("Perceptron AND:")
print("Weights:", and_weights)
print("Outputs:", and_outputs)

not_inputs = np.array([[0], [1]])
not_targets = np.array([1, 0])

not_weights = perceptron_learn(not_inputs, not_targets, 0.1, 100)

not_outputs = step(np.dot(not_inputs, not_weights))
print("Perceptron NOT:")
print("Weights:", not_weights)
print("Outputs:", not_outputs)

and2_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
and2_targets = np.array([0, 0, 1, 0])

and2_weights = perceptron_learn(and2_inputs, and2_targets, 0.1, 100)

and2_outputs = step(np.dot(and2_inputs, and2_weights))
print("Task 2 perceptron:")
print("Weights:", not_weights)
print("Outputs:", not_outputs)
