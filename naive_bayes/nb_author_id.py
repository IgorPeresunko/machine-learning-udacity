""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

features_train, features_test, labels_train, labels_test = preprocess()

clf = GaussianNB()

# count the time to train model
t0 = time()
clf.fit(features_train, labels_train)

print("Training time: ", round(time() - t0, 3), "s")

prediction = clf.predict(features_test)
accuracy = accuracy_score(prediction, labels_test)

print(accuracy)