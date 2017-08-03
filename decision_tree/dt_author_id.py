#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from time import time
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
#reduce the training data to 1%
full_training_set = 1
if not full_training_set :
    features_train = features_train[:len(features_train)/100]
    labels_train = labels_train[:len(labels_train)/100]

print "Feature percentile: ", len(features_train[0])

#exit(0)

clf = DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predict time:", round(time()-t0, 3), "s"
accuracy = clf.score(features_test, labels_test)

print "accuracy: ", accuracy
print "no. of Chris test emails:", sum(pred)
print "no. of Sara test emails:", len(pred) - sum(pred)

"""
selector = SelectPercentile(f_classif, percentile=1)
Feature percentile:  379
training time: 2.378 s
predict time: 0.001 s
accuracy:  0.965870307167
no. of Chris test emails: 885
no. of Sara test emails: 873

selector = SelectPercentile(f_classif, percentile=10)
Feature percentile:  3785
training time: 31.582 s
predict time: 0.01 s
accuracy:  0.978953356086
no. of Chris test emails: 862
no. of Sara test emails: 896
"""