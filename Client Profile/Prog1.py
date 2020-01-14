__author__ = 'Márcio Ciolfi'
__copyright__ = 'Copyright 2020'
__license__ = 'Ciolfi'
__version__ = '1.0'
__maintainer__ = 'Márcio Ciolfi'
__email__ = 'ciolfi@gmail.com'
__username__ = 'mciolfi'
__description__ = 'Customer profile'
__status__ = 'Development'


# Open dataset
def arq(name, ndata, types):
    import csv

    listt = []  # Define listt as matrix
    with open(name, newline='') as csvfile:  # csv module will detect new lines
        if types == ' ':  text = csv.reader(csvfile, delimiter=' ')  # classify by space
        if types == ',':  text = csv.reader(csvfile, delimiter=',')  # classify by comma
        if types == '\t': text = csv.reader(csvfile, delimiter='\t') # classify by tab
        for line in text:
            for t in range(len(line) - ndata): line.remove('')  # Removes zeros inside data
            listt.append(line)  # Define listt as the data inside file
    return (listt)


# Main program
from numpy import exp, array, random, dot

listt = array(arq('perfil_cliente.csv', 37, ';'))  # Define listt as the data inside the file
inputs = []
training_set_outputs = []
for cont in range(len(listt)):
    # Define one value for each classification: Iris-setosa = 0,Iris-versicolor = 1
    if listt[cont][4] == 'Iris-setosa':
        inputs.append([float(listt[cont][i]) for i in range(4)])
        training_set_outputs.append([0])
    if listt[cont][4] == 'Iris-versicolor':
        inputs.append([float(listt[cont][i]) for i in range(4)])
        training_set_outputs.append([1])
    # if listt[cont][4] == 'Iris-virginica':  don't include on list
inputs = array(inputs)  # Define inputs as matrix to transpose after
training_set_outputs = array(training_set_outputs)  # Define outputs as matrix to transpose after
print('Iris')
txlearning = 0.01  # Define learning rate
perceptron(inputs, training_set_outputs, txlearning)  # Run perceptron
# Show differencies between Iris setosa and versicolor
print('Iris-setosa')
data0 = classificator(inputs,training_set_outputs,0)
print('Iris-versicolor')
data1 = classificator(inputs,training_set_outputs,1)
# Plot results
plot (data0[0], data0[1], data0[2], data0[3], 'Iris-setosa',data1[0], data1[1], data1[2], data1[3], 'Iris-versicolor')
