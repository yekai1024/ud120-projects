#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time
from sklearn.metrics import accuracy_score


features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
"""
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="FAST")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
"""
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary



def classify(features_train, labels_train, alg_type = "GNB"):
    print "Algorithm: ", alg_type
    if alg_type == "GNB":
        from sklearn.naive_bayes import GaussianNB
        clf = GaussianNB()
    elif alg_type == "SVM":
        from sklearn.svm import SVC
        clf = SVC(kernel="rbf", C=10000)
    elif alg_type == "DTR":
        from sklearn.tree import DecisionTreeClassifier
        clf = DecisionTreeClassifier(min_samples_split=40)
    elif alg_type == "KNN":
        from sklearn.neighbors import KNeighborsClassifier
        clf = KNeighborsClassifier(n_neighbors=3)
    elif alg_type == "ADA":
        from sklearn.ensemble import AdaBoostClassifier
        clf = AdaBoostClassifier(n_estimators=100)
    elif alg_type == "RDF":
        from sklearn.ensemble import RandomForestClassifier
        clf = RandomForestClassifier(n_estimators=10)
    else:
        print "Wrong Alg ", alg_type
        return None

    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time() - t0, 3), "s"

    return clf

def my_alg(features_train, labels_train, alg_type = "GNB"):
    clf = classify(features_train, labels_train, alg_type)

    t0 = time()
    pred = clf.predict(features_test)
    print "predict time:", round(time()-t0, 3), "s"

    #accuracy = clf.score(features_test, labels_test)
    accuracy = accuracy_score(labels_test, pred)
    print "accuracy: ", accuracy

    try:
        prettyPicture(clf, features_test, labels_test, alg_type)

    except NameError:
        pass

alg_list = ["GNB", "SVM", "DTR", "KNN", "RDF", "ADA"]
map(lambda alg: my_alg(features_train, labels_train, alg), alg_list)
#plt.show()

"""
Algorithm:  GNB
training time: 0.001 s
predict time: 0.0 s
accuracy:  0.884
Algorithm:  SVM
training time: 0.02 s
predict time: 0.001 s
accuracy:  0.932
Algorithm:  DTR
training time: 0.001 s
predict time: 0.0 s
accuracy:  0.912
Algorithm:  KNN
training time: 0.001 s
predict time: 0.001 s
accuracy:  0.936
Algorithm:  RDF
training time: 0.019 s
predict time: 0.004 s
accuracy:  0.924
Algorithm:  ADA
training time: 0.161 s
predict time: 0.007 s
accuracy:  0.924
"""