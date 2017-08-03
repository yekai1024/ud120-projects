#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


# My Codes
#reduce the training data to 1%
full_training_set = 1
if not full_training_set :
    features_train = features_train[:len(features_train)/100]
    labels_train = labels_train[:len(labels_train)/100]

clf = GaussianNB()
"""
training time: 0.592 s
predict time: 0.077 s
accuracy:  0.973265073948
"""

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

# equal to below for loop
# print map(lambda x: clf.predict(features_test[x]), [10,26,50])

#for x in [10,26,50]:
#    print clf.predict(features_test[x])
