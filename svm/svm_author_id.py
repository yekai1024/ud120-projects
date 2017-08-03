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
from time import time
from email_preprocess import preprocess
from sklearn.svm import SVC

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#reduce the training data to 1%
full_training_set = 0
if not full_training_set :
    features_train = features_train[:len(features_train)/100]
    labels_train = labels_train[:len(labels_train)/100]

#clf = SVC(kernel="linear")
"""
SVC linear is quite slow compare to GNB, but a bit higher accuracy
training time: 125.967 s
predict time: 13.041 s
accuracy:  0.984072810011
"""

clf = SVC(kernel="rbf", C=10000)
"""
With %1 training data
C=1 default
training time: 0.076 s
predict time: 0.838 s
accuracy:  0.616040955631
C=10000
training time: 0.072 s
predict time: 0.677 s
accuracy:  0.892491467577
"""

"""
SVC(kernel="rbf", C=10000)
Full training set
training time: 83.669 s
predict time: 8.566 s
accuracy:  0.990898748578
no. of Chris test emails: 877
no. of Sara test emails: 881

%1 training set
training time: 0.077 s
predict time: 0.682 s
accuracy:  0.892491467577
no. of Chris test emails: 1018
no. of Sara test emails: 740
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
