import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
from scipy.io import loadmat
from scipy.optimize import minimize

def sigmoid(z):  
    return 1 / (1 + np.exp(-z))

def cost(theta, X, y, learningRate):  
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    reg = (learningRate / 2 * len(X)) * np.sum(np.power(theta[:,1:theta.shape[1]], 2))
    return np.sum(first - second) / (len(X)) + reg

def gradient(theta,X,y,learningRate):
	theta=np.matrix(theta)
	X=np.matrix(X)
	y=np.matrix(y)

	parameters=int(theta.ravel().shape[1])
	error= sigmoid(X * theta.T) - y

	grad= (((learningRate)/len(X))*theta)+ ((X.T*error)/len(X)).T
	grad[0, 0] = np.sum(np.multiply(error, X[:,0])) / len(X)

	return np.array(grad).ravel()

def one_vs_all(X,y,num_labels,learning_rate):
	rows=X.shape[0]
	params=X.shape[1]
	all_theta=np.zeros((num_labels,params+1))
	X = np.insert(data['X'], 0, values=np.ones(rows), axis=1)
	for i in range(1,num_labels+1):
		theta=np.zeros(params+1)
		y_i=np.array([1 if label==i else 0 for label in y])
		y_i=np.reshape(y_i,(rows,1))
		fmin = minimize(fun=cost, x0=theta, args=(X, y_i, learning_rate), method='TNC', jac=gradient)
        all_theta[i-1,:] = fmin.x

    return all_theta    

data=loadmat('data/ex3data1.mat')
all_theta = one_vs_all(data['X'], data['y'], 10, 1) 