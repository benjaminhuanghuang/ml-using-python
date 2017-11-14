'''
  Gaussian Naive bayes
  Bayes was a religious man tring to prove the existence of God. 
'''

import numpy as numpy
X = np.array([-1, -1], [-2, 1], [-3, -2], [ 1,  1],[2, 1], [3, 2])
Y = np.array([1,1,1,2,2,2])

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X,Y)
print(clf.predict([[-0.8, -1]]))