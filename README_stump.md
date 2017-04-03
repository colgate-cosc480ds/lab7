# Decision Stump

The in-lab exercise is to build a decision stump. A decision stump is a depth-limited decision tree: it splits on a single feature and then classifies the instances according to the value of that feature. Completing this lab exercise should put you in good shape for writing a full-blown decision tree classifier.

**Important:**  You are expected to complete your decision stump classifier by the end of lab. Please show me your code before you leave.  Please commit + push your work as well.

The key challenge in building a decision stump is finding the best feature on which to split the data. The best feature is the one that maximizes information gain as described in lecture.  Recall from lecture that maximizing information gain is equivalent to minimizing segmentEntropy.  Note: the book, DSFS, uses slightly different terminology: the segmentEntropy from class is equivalent to the partitionEntropy described in the book.

In your implementation, you can assume all attributes are categorical.

A skeleton implementation of a decision stump is provided for you in `decisionStump.py`.  The current implementation is "hard coded" to work on the restaurant data.  Run it once so you see how it works:

	$ python dataClassifier.py -d restaurant.arff -c stump

The methods `classify` and `printDiagnostics` are already implemented.  You need only revise `train`.	

## Testing correctness

On the restaurant dataset, the feature with the highest information gain is *pat* which describes the number of patrons in the restaurant and takes on three values (none, some, full). Its information gain is around 0.541 bits.

You can run your stump by executing the command:

	$ python dataClassifier.py -d restaurant.arff -c stump

If you run it on the weather data, it should split on outlook with a gain of 0.247 bits:

	$ python dataClassifier.py -d weather.arff -c stump

Be sure to test on a dataset with a non-binary class label. On the `betterZoo.arff` dataset, the feature with the highest information gain is legs with a gain of around 1.37 bits.

	$ python dataClassifier.py -d betterZoo.arff -c stump