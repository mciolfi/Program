# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# Open dataset
def arq(name, ndata, types):
    import csv

    listt = []  # Define listt as matrix
    with open(name, newline='') as csvfile:  # csv module will detect new lines
        if types == ' ':  text = csv.reader(csvfile, delimiter=' ')  # classify by space
        if types == ',':  text = csv.reader(csvfile, delimiter=',')  # classify by comma
        if types == ';':  text = csv.reader(csvfile, delimiter=';')  # classify by semicolon
        if types == '\t': text = csv.reader(csvfile, delimiter='\t') # classify by tab
        for line in text:
            for t in range(len(line) - ndata): line.remove('')  # Removes zeros inside data
            listt.append(line)  # Define listt as the data inside file
    return (listt)

# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Main program
from numpy import exp, array, random, dot, loadtxt
from keras.models import Sequential
from keras.layers import Dense

listt = array(arq('teste.txt', 8, '\t'))  # Define listt as the data inside the file
X = listt[: 0:1]
y = listt[: 8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim = 2, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(6, activation = 'sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10)

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
