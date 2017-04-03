# Digit Classification

The classification task is to take an image (i.e. pixel values) of a single handwritten digit and determine whether it is 0, 1, 2, ..., or 9.

Try running your classifiers on the digit dataset. This command runs the perceptron classifier. It may take a while. You may wish to choose smaller values for the size of the training and test sets (the `-t` and `-s` parameters respectively). If running a decision tree, you almost certainly want to limit the depth as there are a lot of features.

	$ python dataClassifier.py -d digits -t 5000 -s 1000 -c naiveBayes

The basic feature set for the digits dataset is simply the pixel values: there is a feature for each possible pixel and its value is either 0 or 1. Using the basic feature set, the perceptron obtains approximately 70.8% accuracy on the test set.

## Feature Design for Digits dataset

Building classifiers is only a small part of getting a good system working for a task. Indeed, the main difference between a good classification system and a bad one is usually not the classifier itself (e.g. perceptron vs. naive Bayes), but rather the quality of the features used. So far, we have used the simplest possible features: the identity of each pixel (being on/off).

To increase your classifier's accuracy further, you will need to extract more useful features from the data. The `EnhancedDigitFeatureExtractor` in `featureExtractors.py` is your new playground. When analyzing your classifiers' results, you should look at some of your errors and look for characteristics of the input that would give the classifier useful information about the label. If you wish, you can add code to the end of the `runClassifier` function in `dataClassifier.py` to inspect what your classifier is doing.

There are number of possible features you could add. Here is one that should work well. Consider the number of separate, connected regions of "off" pixels, which varies by digit type. 1, 2, 3, 5, 7 tend to have a single contiguous region of "off" pixels while the loops in 6, 8, 9 create more. The number of "off" regions in a 4 depends on the writer. This is an example of a feature that is not directly available to the classifier from the per-pixel information. If your feature extractor adds new features that encode these properties, the classifier will be able exploit them. Note that some features may require non-trivial computation to extract, so write efficient and correct code.

**Important**: even though your classifiers may be able to handle a variety of features, you are strongly encouraged to only create binary features (0 or 1). Perceptrons, for instance, can have trouble converging when features have wildly different numerical values.

## Task

Add new binary features for the digit dataset in the `EnhancedDigitFeatureExtractor`. Note that you can encode a feature which takes 3 values [1,2,3] by using 3 binary features, of which only one is on at the time, to indicate which of the three possibilities you have. In theory, features aren't conditionally independent as naive Bayes requires, but your classifier can still work well in practice.

You can run your enhanced features by passing the `-f` flag, as in

	$ python dataClassifier.py -d digits -t 5000 -s 1000 -c naiveBayes -f

Your features should increase the accuracy of your classifiers. For full credit, you should see a significant improvement in accuracy (5% or more) and/or demonstrate that you tried a number of thoughtful features.

After you have finished, fill in `analysis_digits.txt`.

