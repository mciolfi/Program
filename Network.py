class network(object):

    def __init__(self, sizes):
        self.num_layers = len(sizes)
        # sizes is the neuron number by layer
        self.sizes = sizes
        # Random bias and weights average 0 and standard deviation 1. No bias for 1st layer
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights =  [np.random.randn(y,x) for x,y in zip(sizes[:-1], sizes[1:])]

    def feedfoward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a

    # SGD methode (Stochastic Gradient Descent)
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data = None):
        training_data = list(training_data)
        n = len(training_data)

        if test_data:
            test_data ==list(test_data)
            n_test = len(test_data)

        for j in range(epochs):
            random.shuffle(training_data)
            mini_batch = [training_data[k:k + mini_btach_size] for k in range(0, n, mini_batch_size)]

            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)

            if test_data:
                print('Epoch {} : {} / {}'.format(j, self, evaluate(test_data), n_test)):
            else:
                print('Epoch {} finalizada'.format(j))

def sigmoid(z):
    return 1 / 1 +np.exp(-z)

import numpy as np
net1 = network [2, 3, 1]