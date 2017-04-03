import util

class PerceptronClassifier:
    """
    Perceptron classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to raw data such as that produced by the loadXXX functions in samples.py).
    """
    def __init__(self, legalLabels, max_iterations=5):
        self.legalLabels = legalLabels
        self.max_iterations = max_iterations

    def train(self, trainingData, trainingLabels):
        """
        Train the percptron.

        The training loop for the perceptron passes through the training data several
        times and updates the weight vector for each label based on classification errors.
        """

        self.features = list(set([ f for datum in trainingData for f in datum.keys() ]))
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def classify(self, data):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  
        """

        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def printDiagnostics(self):
        """
        For each label, print the 20 features with the greatest weight for that label
        """
        "*** YOUR CODE HERE ***"

        util.raiseNotDefined()











# perceptron.py
# -------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# Note: this is a modified version of the code available from
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
