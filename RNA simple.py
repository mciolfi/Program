def act_func(input,type):
    '''Define the activation function'''
    # Calculate the value for the output of the relu function: output
    if type == 'relu': output = max(input, 0)
    elif type == 'tan': output = np.tanh(input)

    # Return the value just calculated
    return (output)

def predict_with_network(input_data, weights):
    # Calculate node 0 value
    node_0_input = (input_data * weights['node_0']).sum()
    node_0_output = act_func(node_0_input, 'relu')

    # Calculate node 1 value
    node_1_input = (input_data * weights['node_1']).sum()
    node_1_output = act_func(node_1_input, 'relu')

    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])

    # Calculate model output
    input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
    model_output = input_to_final_layer

    # Return model output
    return (model_output)

import numpy as np

#input_data = np.array([2, 3])
input_data = ([3, 5], [1, -1], [0, 0], [8, 4])
weights = {'node_0': np.array([1, 1]),
           'node_1': np.array([-1, 1]),
           'output': np.array([2, -1])}

r = predict_with_network(input_data, weights)
print (input_data, '\t', weights, '\t', r)