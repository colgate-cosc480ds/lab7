# Spam Classification

The classification task is to take the text of an email and predict whether or not it is spam. The dataset `spambase.arff` is a dataset of pre-processed email messages -- i.e., each email has already been converted into a feature of vectors.  Where did those features come from? Well, for this problem, you will take raw email text and generate your own set of features.

An example of a bare bones feature extractor for spam is given in `EmailFeatureExtractor` in `featureExtractors.py`. It is based on the number of capitalized letters in the email. It creates four binary features: `fewCaps`, `someCaps`, `manyCaps`, and `allCaps`.  In any given email, exactly one of those features will be set to 1 and the others will be set to zero (by default).  

If you run the decision tree on the spam dataset, like this:

	$ python dataClassifier.py -d spam -c dt -t 5000 -s 1000

You should get an accuracy of around 72%, up slightly from the mostFrequent classifier which gets accuracy of 69.4% on the test data.

While this is a simple feature, if you examine the code, it illustrates how feature engineering may require three phases: 

1. pre process the data to gather some statistics, 
2. finalize the feature set based on those statistics, 
3. actually extract features. 

When you design your features, you will almost certainly want to employ three phases like this.

## Feature Design for Spam dataset

Building classifiers is only a small part of getting a good system working for a task. Indeed, the main difference between a good classification system and a bad one is usually not the classifier itself (e.g. perceptron vs. naive Bayes), but rather the quality of the features used. So far, we have used the simplest possible features.

To increase your classifier's accuracy further, you will need to extract more useful features from the data. The `EnhancedEmailFeatureExtractor` in `featureExtractors.py` is your new playground. When analyzing your classifiers' results, you should look at some of your errors and look for characteristics of the input that would give the classifier useful information about the label. If you wish, you can add code to the end of the `runClassifier` function in `dataClassifier.py` to inspect what your classifier is doing.

Here are some features you might try:

- Look at the features in the `spambase.arff` for inspiration.
- Consider creating a feature for every word. Of course, that's a lot of features! In fact, you will almost certainly want to prune the set of words to include only those that occur frequently (say, at least 100 times). This is where the three-phase approach to feature construction really helps. In preprocessing, simply count every word; then finalize the features to be those words that occur frequently; when extracting features, ignore any words not in your approved list.
- You should probably do additional processing to get a decent word set. For example, you might want to do some or all of the following:
	+ Convert all words to lower case (though you might also have features related to the frequency/length of capitalized words)
	+ Strip HTML (e.g., remove anything matching this regular expression '<[^<>]+>')
	+ Replace any specific URL with "httpaddr"
	+ Replace any specific email with "emailaddr"
	+ Replace any specific number with "number"
	+ Replace the dollar sign with "dollar"
	+ Removal of non-words: discard any non-alpha numeric characters and split on whitespace to get words.
	+ Employ word stemming. For example, 'discount', 'discounts', 'discounted' and 'discounting' are all forms of the word 'discount'. A stemmer has been provided for you. To use it, suppose that variable word represents some string you want to stem, you can simply do porter2.stem(word) to get the stemmed version of the word. (Warning: this code slows things down a bit.) Sometimes the stemmer actually strips off additional characters from the end, so 'include', 'includes', 'included', and 'including' are all replaced with 'includ'.

**Important**: even though your classifiers may be able to handle a variety of features, you are strongly encouraged to only create binary features (0 or 1). Perceptrons, for instance, can have trouble converging when features have wildly different numerical values.

## Task

Add new *binary* features for the spam dataset in the `EnhancedEmailFeatureExtractor`. Note that you can encode a feature which takes 3 values [1,2,3] by using 3 binary features, of which only one is on at the time, to indicate which of the three possibilities you have. In theory, features aren't conditionally independent as naive Bayes assumes, but your classifier can still work well in practice.

You can run your enhanced features by passing the `-f` flag, as in

	$ python dataClassifier.py -d spam -c dt -t 5500 -s 500 -f

Your features should increase the accuracy of your classifiers. For full credit, you should see a significant improvement in accuracy and/or demonstrate that you tried a number of thoughtful features. On the spam dataset, it is possible to get above 95% accuracy!

After you have finished, fill in `analysis_spam.txt`.