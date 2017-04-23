# Perceptron

**Important**: The perceptron is optional.  Completing it will earn you challenge problem credit. 

A skeleton implementation of a perceptron classifier is provided for you in `perceptron.py`. You will fill in the `train` function, the `classify` function, and the `printDiagnostics` function.

This perceptron is similar to what was described in class.  However, your implementation must support multi-class classification.

The way this is handled with a perceptron is by maintaining a separate weight vector for each possible value of the target attribute.  So, if the target attribute is binary (e.g., spam/ham), you would have two weight vectors (one for spam and one for ham).  

To perform classification, the perceptron computes the weighted combination for each weight vector and classifies the input as belonging to whichever class yields the highest weighted combination.

To fit a multi-class perceptron using training data, the procedure is pretty much as described in class.  The only difference is the weight vector update step.  Here, you should update each weight vector in turn.  For example, suppose the misclassified example was labeled spam but it really is a ham.  Then we should *subtract* from the spam vector and *add* to the ham vector.

Finally, your implementation should repeatedly loop through the data until convergence or until `max_iterations` is reached.  One iteration is one pass through the entire training dataset.

Run your code with:

	$ python dataClassifier.py -d spambase.arff -t 4000 -s 500 -c perceptron

Perceptrons expect features to be numbers. So when run on an ARFF dataset, which may have nominal features, all features are automatically converted to binary features that are either 1 or 0. For example, the pat feature in the restaurant dataset would be converted into three features: pat=full, pat=some, pat=none. On any particular instance only one of these features would be set to 1. This conversion is done for you in `featureExtractorsBasic.py`.

Implement the `printDiagnostics` to print out a nicely formatted list of of the top weighted features for each class label.

Hints and observations:

- The command above should yield test accuracy around 78% (with the default 5 iterations). This is only an approximate estimate because the perceptron is a lot more sensitive to the specific choice of tie-breaking than naive Bayes.

- One of the problems with the perceptron is that its performance is sensitive to several practical details, such as how many iterations you train it for, and the order you use for the training examples (in practice, using a randomized order works better than a fixed order). The current code uses a default value of 5 training iterations. You can change the number of iterations for the perceptron with the -a option, as in

  		$ python dataClassifier.py -d spambase.arff -t 4000 -s 601 -c perceptron -a iterations=3

    Try different numbers of iterations and see how it influences the performance. In practice, this experimentation should be done on a validiation set (a held-out portion of the training data) rather than on the test dataset but this is not required.
