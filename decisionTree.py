import classificationMethod
import math
import util

class DecisionTreeClassifer(classificationMethod.ClassificationMethod):
    '''
    Decision tree classifer.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to raw data such as that produced by the loadXXX functions in samples.py).
    '''

    def __init__(self, legalLabels, max_depth=5):  # feel free to change default max_depth
        self.legalLabels = legalLabels
        self.max_depth = max_depth 
        self.root = None       # training should replace this with root of decision tree!

        "*** YOUR CODE HERE ***"
        # initialize any data structures here

    def train(self, trainingData, trainingLabels):
        '''
        Train the decision tree on training data.
        '''
        # might be useful in your code later...
        # this is a list of all features in the training set.
        features = list(set([ f for datum in trainingData for f in datum.keys() ]))
        "*** YOUR CODE HERE ***"

        util.raiseNotDefined()

    def classify(self, data):
        """
        Classifies each datum by passing it through the decision tree.  

        Expects data to be a list.  Each datum in list is a feature vector (i.e., a dictionary)
        """
        "*** YOUR CODE HERE ***"

        util.raiseNotDefined()


    def printDiagnostics(self):
        """
        This function is called after the classifier has been trained.  

        It should print the first five levels of the decision tree in a nicely 
        formatted way.  
        """
        "*** YOUR CODE HERE ***"

        util.raiseNotDefined()


"*** YOUR CODE HERE ***"
"""
You may find it helpful to create additional classes/functions
such as making a DecisionNode class that represents a single 
node in the decision tree.
"""

