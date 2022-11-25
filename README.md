# Perceptron_Algo_Implementation
Implementation of perceptron algorithm with MNIST dataset. 

Here is the link to the data - https://redirect.cs.umbc.edu/courses/graduate/678/fall22/mnist_data.txt
Link to the labels - https://redirect.cs.umbc.edu/courses/graduate/678/fall22/mnist_labels.txt

Each row in the data file is 784 integers that represent the grayscale values of a 28x28 handwritten digit. Each row in the labels file is a single digit in the range 0-9 and is in a 1-to-1 correspondence with rows in the data file. 

The accuracy of the classifier on the training data is 89.52%
The accuracy of the classifier on the test data is 87.36% 
For the implementation, first the required libraries are imported. Then the required data and label 
files were extracted and read line by line. For the bias term, 1 was added at the beginning of the x. 
Then I initialized 10 weight vectors for each digit from 0-9. After that I split the data into half, for 
training and testing purposes. For training the data, whenever a prediction is wrong, the weights for 
the correct class are increased by x and the weights for the incorrectly predicted class are decreased 
by x. After checking for various convergence criteria’s, I chose 1900000 as the value, because the 
loop was iterating for longer amount of time when the value was less, about 1000000 i.e. the model 
was underfitting and if we take the value to be greater than 1900000, the model was overfitting. So 
to find a balanced model, I chose the convergence criteria to be 1900000. And then the model was 
tested and the accuracy of the test data was 87.36% indicating that the model is neither underfit nor 
overfit. 
