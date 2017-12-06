#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
import random
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# svc = SVC(kernel='linear')
# svc = SVC(C = 1000,kernel="rbf") # radial
t1 = time()
# train on a small dataset
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 
Costs = [10.0,100.0,1000.0,10000.0]
accuracy = []
for i in xrange(4):
	svc = SVC(C = Costs[i],kernel="rbf")
	svc.fit(features_train,labels_train) # fit the training data
	print "training time:",round(time() - t1,2)
	ypred = svc.predict(features_test) # predicting test data
	t2 = time()
	print "predicting time:", round(time() - t2,2)
	print "Accuracy Score is :"
	# print accuracy_score(ypred,labels_test)
	accuracy.append(accuracy_score(ypred,labels_test))

print accuracy # C = 10000, accuracy is highest

# Use optimized params
svc = SVC(C = 10000, kernel="rbf")
svc.fit(features_train,labels_train) 
ypred = svc.predict(features_test)
print "Accuracy Score is :"
print accuracy_score(ypred,labels_test) # 0.990898748578

# Extracting Predictions from SVM
svc = SVC(C = 10000, kernel="rbf")
svc.fit(features_train,labels_train) 
ypred = svc.predict(features_test)
print "Accuracy Score is :"
print accuracy_score(ypred,labels_test)
print "predict for element of the test set 10th,26th,50th:",ypred[10],ypred[26],ypred[50]

# count Chris (1) class
count = 0
for i in ypred:
	if i == 1:
		count += 1
print "Number of Chris class in full training dataset:", count