import csv
from src.autoencoder import autoencoder

# Read in CSV file
brca = []
count = 0

# brca is 192 long
with open("brca_toronto_collab_mutect_123_030617.csv") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        row.pop()
        if count != 0:
            floatRow = [float(i) for i in row]
            brca.append(floatRow)
        count += 1
csvFile.close()

sess = autoencoder.startSession()
brcaTensor = autoencoder.listToTensor(brca[0])
autoencoder.printTensor(brcaTensor)

W = tf.get_variable('W', shape[192, 128], initializer = tf.contrib.layers.xavier_initializer())
autoencoder.printTensor(W)
