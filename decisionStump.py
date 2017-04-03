import classificationMethod
import collections
import math
import util

class DecisionStumpClassifer(classificationMethod.ClassificationMethod):
    '''
    Decision Stump classifer.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to raw data such as that produced by the loadXXX functions in samples.py).
    '''

    def __init__(self, legalLabels):
        self.legalLabels = legalLabels
        self.splitFeature = None         # the feature this stump uses to classify
        self.valueToLabel = {}           # for each value of splitFeature, the class 
                                         # label that will be assigned
        "*** YOUR CODE HERE ***"
        # initialize any data structures here

    def train(self, trainingData, trainingLabels):
        '''
        Train the decision stump on training data.  Find the one
        feature with highest information gain.

        Split the training data based on this feature and calculate
        the distribution over labels within each split.  
        '''
        # might be useful in your code later...
        # this is a list of all features in the training set.
        features = list(set([ f for datum in trainingData for f in datum.keys() ]))
        "*** YOUR CODE HERE ***"

        # find the feature to split on and set self.splitFeature
        # split the trainingData based on the value of this feature
        # for each split, assign the plurality label

        # PLEASE DELETE THIS LINE AND THE NEXT FOUR LINES 
        # illustrative example of a decision stump hard-coded for restaurant.arff
        # this stump ignores the data and splits on price
        self.splitFeature = 'price'    
        self.valueToLabel = {'$': 'yes', '$$': 'yes', '$$$': 'no'}

    def classify(self, data):
        """
        Classifies each datum.

        Expects data to be a list.  Each datum in list is a feature vector (i.e., a dictionary)
        """
        guesses = []
        for datum in data:
            value = datum[self.splitFeature]
            guess = self.valueToLabel[value]
            guesses.append(guess)
        return guesses
        

    def printDiagnostics(self):
        """
        This function is called after the classifier has been trained.  

        It should print the first five levels of the decision Stump in a nicely 
        formatted way.  
        """
        print 'Decision Stump'
        print 'Classify based on feature: {0}'.format(self.splitFeature)
        for value in self.valueToLabel:
            label = self.valueToLabel[value]
            print '\tif {0}={1}, classify as {2}'.format(self.splitFeature, value, label)


"*** YOUR CODE HERE ***"
"""
You may find it helpful to create additional classes/functions
here
"""
