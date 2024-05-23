#  MNIST tutorial (handwritten printed digits recognition tutorial)
#  modified from
#  https://elitedatascience.com/keras-tutorial-deep-learning-in-python
#  for SDSC SI2017

# ----------- IMPORT STATEMENTS ---------------
import numpy as np
np.random.seed(1)  # for reproducibility

from keras.models import Sequential               #Sequential models are the standard stack of layers models
from keras.layers import Dense, Dropout, Activation, Flatten   #These are core layer specification functions
from keras.layers import Convolution2D, MaxPooling2D           #These are convolution layer functions
from keras.utils import np_utils                         #Some utilities
from keras import optimizers                             #For training algorithm
#---------------------------------------------

#--------------- LOAD and PREPARE DATA STATEMENTS ----------------
# Load some numpy arrays that have the MNIST data
#  (these are subsets extracted from the MNIST data set in Keras)
X_train=np.load('X_train5k.npy')
Y_train=np.load('Y_train5k.npy')
X_test =np.load('X_test.npy')
Y_test =np.load('Y_test.npy')

print(X_train.shape)     #review the dimensions

#save a few training images with the label in the file name 
from PIL import Image
for i in range(0,10):
   im = Image.fromarray(X_train[i,:,:])
   im.save("Ximage_num"+str(i)+"_cat_"+str(Y_test[i])+".jpeg")


# --------- Reshape input data ------------
#  b/c Keras expects N-3D images (ie 4D matrix)
X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test  = X_test.reshape(X_test.shape[0],   1, 28, 28)

#To confirm, we can print X_train's dimensions again:
print(X_train.shape)

#convert and put into 0-1 range
X_train  = X_train.astype('float32')
X_test   = X_test.astype('float32')
X_train /= 255
X_test  /= 255

# Convert 1-dimensional class arrays to 10-dimensional class matrices
Y_train = np_utils.to_categorical(Y_train, 10)
Y_test  = np_utils.to_categorical(Y_test,  10)

# ------------- End loading and preparing data --------------

# --------------Set up Model ---------------------
model = Sequential()

#add convolution layer of 32 filters, 3x3 each, 
#     input shape for 1 image, using 'theano' ordering 
model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(1,28,28), dim_ordering='th'))

#Now add more layers
model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2))) #get Max over 2D region,and slide

#optional?
model.add(Dropout(0.25))
 
model.add(Flatten())            #reorganize 2DxFilters output into 1D
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
               optimizer='sgd',
               metrics=['accuracy'])
model.fit(X_train, Y_train, 
          batch_size=32, nb_epoch=15, verbose=1)

# get overall prediction score
trainscore = model.evaluate(X_train, Y_train, verbose=0) # get overal score
testscore = model.evaluate(X_test, Y_test, verbose=0) # get overal score

print('train set score:'+str(trainscore))
print('test set score:'+str(testscore))

#pred  = model.predict(X_test,verbose=0)           # get predicted labels


#todo
#get smaller mnist datasets
#try 1 vs 2 conv layer as exercise
#get predictions and some plot of activaiotns?
#ie activation for some input or plot of weights?
#any chance for notebook? how to run/edit scritps