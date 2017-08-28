""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import numpy as np
import matplotlib.pyplot as plt

from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score

def prettyPicture(clf, X_test, y_test):
	x_min = 0.0; x_max = 1.0
	y_min = 0.0; y_max = 1.0

	# Plot the decision boundary. For that, we will assign a color to each
	# point in the mesh [x_min, m_max]x[y_min, y_max].
	h = .01  # step size in the mesh
	xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
	Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

	# Put the result into a color plot
	Z = Z.reshape(xx.shape)
	plt.xlim(xx.min(), xx.max())
	plt.ylim(yy.min(), yy.max())

	plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)

	# Plot also the test points
	grade_sig = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==0]
	bumpy_sig = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==0]
	grade_bkg = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==1]
	bumpy_bkg = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==1]

	plt.scatter(grade_sig, bumpy_sig, color = "b", label="fast")
	plt.scatter(grade_bkg, bumpy_bkg, color = "r", label="slow")
	plt.legend()
	plt.xlabel("bumpiness")
	plt.ylabel("grade")

	plt.savefig("test.png")

    
import base64
import json
import subprocess

def output_image(name, format, bytes):
	image_start = "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
	image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
	data = {}
	data['name'] = name
	data['format'] = format
	data['bytes'] = base64.encodestring(bytes)
	print image_start+json.dumps(data)+image_end

def classify(features_train, labels_train):   

	from sklearn import svm

	clf = svm.SVC(kernel="rbf", C=100000.0)    
	clf.fit(features_train, labels_train)

	return clf


features_train, features_test, labels_train, labels_test = preprocess()

clf = classify(features_train, labels_train)

pred = clf.predict(features_test)

accuracy = accuracy_score(pred, labels_test)
print(accuracy)


prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())