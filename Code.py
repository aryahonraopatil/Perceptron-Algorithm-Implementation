#Importing Libraries
import numpy as np
import pandas as pd

data=[]
labels=[]
with open('dataset.txt') as l:
    for line in l:
        data.append([line.strip()]) # Reading line by line of dataset file

with open('labels.txt') as l:
    for line in l:
        labels.append(line.strip()) # Reading line by line of text file

print(len(labels)) #Printing the label length to check if correct
print(len(data))   #Printing the data length to check if correct

data_tab=[]
for i in data:
    data_mod=[int(x) for x in i[0].split(' ')]   # Splitting each value of the rows and converting it to integer
    data_mod.insert(0,1)   # Adding 1 as the bias term at beginning of every X
    data_tab.append(data_mod) 

data_df=pd.DataFrame(data_tab)
data_df

labels_mod=[int(x) for x in labels] # Converting y values to integer

weights=np.zeros([10,len(data_tab[0])]) # Initializing 10 weight vectors for 10 classes for 10 digits from 0-9

from sklearn.model_selection import train_test_split
X=data_df
y=labels_mod
print(len(data_df[0]))
# Splitting the dataset into half for training and half for testing
(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size = .5, random_state=25)
print(len(X_train), len(X_test))
print(len(y_train),len(y_test))

from copy import deepcopy 

r=0
weights_prev=np.full((10,len(data_tab[0])),1000) # Initializing previous weight to enter into while loop for the first time
while np.sum(np.abs(np.subtract(weights,weights_prev)))>1900000: #looping with the convergence criteria
    print(r)
    weights_prev=deepcopy(weights) 
    for i in range(len(X_train)):   # Iterate over the X_train data
        max_a=0 
        max_class=0
        for j in range(len(weights)): # Weights for every class
            a=np.matmul(weights[j].transpose(),X_train.iloc[i]) # calculating the value of W^T.X
            if a>max_a: # If a is max make that as the predicted class
                max_a=a
                max_class=j 

        pred_class=max_class 
        true_class=int(y_train[i])
    
        if pred_class!=true_class:   #updating the weights 
            weights[true_class]=np.add(weights[true_class],X_train.iloc[i])  #the weight for the correct class are increased
            weights[pred_class]=np.subtract(weights[pred_class],X_train.iloc[i])  #the weights for the incorrectly predicted class are decreased by x
    r+=1
    
 #training the data
 y_train_predicted=[]
for i in range(len(X_train)):
    max_a=0
    max_class=0
    for j in range(len(weights)):
        a=np.matmul(weights[j].transpose(),X_train.iloc[i])
        if a>max_a:
            max_a=a
            max_class=j
    pred_class=max_class
    y_train_predicted.append(pred_class)
  
  from sklearn.metrics import accuracy_score

accuracy_train=accuracy_score(y_train, y_train_pred)
print(accuracy_train)

#testing the data
y_test_predicted=[]
for i in range(len(X_test)):
    max_a=0
    max_class=0
    for j in range(len(weights)):
        a=np.matmul(weights[j].transpose(),X_test.iloc[i])
        if a>max_a:
            max_a=a
            max_class=j
    pred_class=max_class
    y_test_predicted.append(pred_class)
 
 accuracy_test=accuracy_score(y_test, y_pred)
print(accuracy_test)

