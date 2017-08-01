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
from sklearn.svm import SVC

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#clf = SVC(kernel="linear")
"""
SVC is quite slow compare to GNB, but a bit higher accuracy
training time: 125.967 s
predict time: 13.041 s
accuracy:  0.984072810011
"""

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



#########################################################
### MY test code ###


#########################################################


