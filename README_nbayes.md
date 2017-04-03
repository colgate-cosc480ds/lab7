# Naive Bayes

A skeleton implementation of a naive Bayes classifier is provided for you in `naiveBayes.py`. You will fill in the functions `train`, `calculateLogJointProbabilities`, `classify`, and `printDiagnostics`.

The Naive Bayes classifier was described in class and in the reading.  In several respects, your implementation should follow the approach described in class:

- Assume all predictor atributes attributes are categorical (thus it will not be applicable to all provided datasets, only the ones with categorical features).
- Use simple counting to estimate the probabilities needed in the Naive Bayes calculations
- Smooth those counts using Laplace smoothing.  The `k` parameter in the implementation controls the amount of smoothing -- i.e., k is the number of additional pseudo training examples we see for each combination of feature value and class label.  If k=0, then no smoothing occurs.
- You should *not* smooth the estimates of P(Y = y)

In two important respects, your implementation **differs** from what is described in class:

- You must support *multi-class* classification.   In other words, the target attribute can take on more than two possible values. For example, in digit classification, the target attribute takes on ten possible values: 0, 1, 2, ..., 9.  Check out [naiveBayes.pdf](naiveBayes.pdf) for clarification on the differences from what was described in class.
- To avoid underflow, you should compute log probabilities.  This is mentioned in the reading.  See [naiveBayes.pdf](naiveBayes.pdf) for more details.

Implement `train` and `calculateLogJointProbabilities` and `classify` in `naiveBayes.py`. Test your classifier with:

	$ python dataClassifier.py -d spambase.arff -t 4000 -s 500 -c naiveBayes

(The dataset `spambase.arff` is a dataset of pre-processed email messages -- i.e., each email has already been converted into a feature of vectors.  A feature like `word_freq_money` is the frequency of the word money in the emails.  The frequency has been discretized into intervals.  The interval `(-inf-0.01]` is from minus infinity to 0.01.)

You can try different settings of `k` by passing it in as a command line argument, as in

	$ python dataClassifier.py -d spambase.arff -t 4000 -s 500 -c naiveBayes -a k=5

In addition, implement the `printDiagnostics` function to print some useful information about what features are most predictive. See details below.


## Print Diagnostics: Odds Ratios

One tool for understanding the parameters is to look at maximum odds ratios.  Check out [naiveBayes.pdf](naiveBayes.pdf) for the mathematical description.

Use odds ratios in `printDiagnostics` to compare two different class labels.  Print the top 5 features according to odds ratio.  For multi-class classification, do this for all pairs of labels.

For example, when run on the spambase data, like this:

	$ python dataClassifier.py -d spambase.arff -t 4000 -s 500 -c naiveBayes

Your print diagnostics function should print something like this:

	For label 1 vs. 0
	The top 5 features according to max odds ratio are:
	   word_freq_000 = (0.26-inf) has odds 30.785046196
	   capital_run_length_longest = (251.5-inf) has odds 29.6781681305
	   word_freq_remove = (0.01-inf) has odds 21.7283696842
	   word_freq_money = (0.01-inf) has odds 18.2933303811
	   char_freq_$ = (0.1475-inf) has odds 17.6434313862
