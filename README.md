# Implementation of perceptron algorithm with MNIST dataset. 

## Understanding the algorithm

The Perceptron algorithm is used for supervised learning of binary classifiers. It adjusts its weights based on misclassifications in the training data until a correct classification is achieved for all training examples.

The perceptron model takes an input, aggregates it (weighted sum), and returns 1 only if the aggregated sum is more than some threshold else returns 0. Rewriting the threshold as shown above and making it a constant input with a variable weight, we would end up with something like the following:

The Perceptron algorithm guarantees to converge if the data is linearly separable; if a hyperplane can be drawn to separate the positive and negative examples. However, it might not converge if the data is not linearly separable.

## Dataset Description

Here is the link to the data - https://redirect.cs.umbc.edu/courses/graduate/678/fall22/mnist_data.txt

Link to the labels - https://redirect.cs.umbc.edu/courses/graduate/678/fall22/mnist_labels.txt

Each row in the data file has 784 integers that represent the grayscale values of a 28x28 handwritten digit. Each row in the labels file is a single digit in the range 0-9 and is in a 1-to-1 correspondence with rows in the data file. 

## Experimentation 

The accuracy of the classifier on the training data is 89.52%

The accuracy of the classifier on the test data is 87.36% 

For the implementation, first, the required libraries are imported. Then the required data and label files were extracted and read line by line. For the bias term, 1 was added at the beginning of the x. Then I initialized 10 weight vectors for each digit from 0-9. After that, I split the data into half, for training and testing purposes. For training the data, whenever a prediction is wrong, the weights for the correct class are increased by x and the weights for the incorrectly predicted class are decreased 
by x. After checking for various convergence criteria, I chose 1900000 as the value, because the loop was iterating for a longer amount of time when the value was less, about 1000000 i.e. the model was underfitting and if we take the value to be greater than 1900000, the model was overfitting. So to find a balanced model, I chose the convergence criteria to be 1900000. And then the model was tested and the accuracy of the test data was 87.36% indicating that the model is neither underfit nor overfit. 

Reference - https://towardsdatascience.com/perceptron-learning-algorithm-d5db0deab975 (One of the best explanations I have read)
