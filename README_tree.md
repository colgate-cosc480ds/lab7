# Decision Tree

Implement a decision tree classifier. You can assume all features will be discrete (binary/categorical).  Your implementation should be written in `decisionTree.py`.  

Note: you are *permitted* to copy/paste code from `decisionStump.py`.  Although this seems to violate the "DRY" principle, I am making an exception here because decision stump is a lab exercise and constitutes "throw away" code -- i.e., once you complete `decisionTree.py`, you no longer have use for a decision stump and it could be deleted.

## Stopping criteria

The stopping criteria determine when to stop building the tree.  Your implementation should stop when any of the following conditions have been met:

- `max_depth` has been reached.  The depth is the number of features on any path from leaf to root.  So a tree with `max_depth=1` is a decision stump. 
- every feature has been used along the path from the current node to the root of the tree
- all of the examples at the current node belong to the same class

You may include additional stopping criteria.

## Classification decision

When the stopping criterion is met, the value assigned to the leaf should be the most frequently occurring value among the training examples at that leaf.  

## Testing Correctness

The restaurant dataset is small enough that you can calculate the information gain for each feature by hand and make sure your code is correct. Examples of a correct tree includes the tree shown below.  There are multiple correct answers because after splitting on pat, several features are tied for maximum information gain.

You can run your tree by executing the command:

	$ python dataClassifier.py -d restaurant.arff -c dt

Be sure to also test it on datasets that have non-binary class label. For example, this command:

	$ python dataClassifier.py -d betterZoo.arff -c dt -t 90 -s 10

should produce a tree that gets 100% accuracy on the test dataset.

## Displaying the tree

The `printDiagnostics` method should print a nicely formatted version of the tree. It should be at least as nicely formatted as the tree shown below:

	Split on pat (info gain = 0.540852082973):
	pat=none ==>
	    Label = no
	pat=full ==>
	    Split on est (info gain = 0.251629167388):
	    est=10-30 ==>
	        Split on bar (info gain = 1.0):
	        bar=yes ==>
	            Label = no
	        bar=no ==>
	            Label = yes
	    est=30-60 ==>
	        Split on bar (info gain = 1.0):
	        bar=yes ==>
	            Label = yes
	        bar=no ==>
	            Label = no
	    est=60+ ==>
	        Label = no
	pat=some ==>
	    Label = yes

