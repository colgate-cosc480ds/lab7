# Lab 7

Welcome to the *seventh* COSC 480 Data Science Lab!  (Lab 6 was working on data acquisition for your project.)  You are encouraged to work with a partner for this lab.

The first part of this lab, building a decision stump, should be completed by the end of lab on Tuesday.  Please show me your implementation before you leave lab.

This lab is due **Thursday, April 13 2017 at 11:59pm**.  Submission instructions are similar to previous labs.  *When you finish, please be sure to write a commit message!*  

## Setup Instructions

You should not need to make any updates to your VM.  However, you do need to download the data.  This might take a minute or two.

	vagrant@ubuntu:~$ cd /vagrant/lab7
	vagrant@ubuntu:/vagrant/lab7$ curl -O http://cs.colgate.edu/~mhay/cosc480ds/ml_data.tgz
	vagrant@ubuntu:/vagrant/lab7$ tar xfz ml_data.tgz

This should create a data directory in your lab7 folder.

	vagrant@ubuntu:/vagrant/lab7$ ls data

Please do *not* commit this data folder to your repo.


## Overview

In this lab, you will design and implement several classifiers, applying them to a variety of datasets. Then, for some specific classification tasks, you are asked to perform some feature engineering (crafting features that are likely predictive of the target label), followed by some analysis.  The two tasks are spam detection and classifying hand-written digits.

## Getting Started

### Overview of files 

This lab contains several files.  Here's a brief orientation.  Note that the files for this lab take advantage of object-oriented features of Python, such as the ability to define *classes*, *inheritance*, etc.  If you have never seen these features before in Python, you **should review p.30-31 of DSFS**. 

Files you may edit:

- `decisionStump.py` 
- `decisionTree.py`	
- `perceptron.py`
- `naiveBayes.py`
- `featureExtractors.py` -- where you write your enhanced feature extractors
- `analysis_spam.txt`	-- where you will write an analysis of your feature engineering for the digits dataset.
- `analysis_digits.txt`	-- where you will write an analysis of your feature engineering for the spam dataset.


Files you should read but *not* edit:

- `classificationMethod.py`	-- Abstract super class for the classifiers you will write.  (You should read this file carefully to see the basic API of a classifier.)
- `mostFrequent.py`	-- A simple baseline classifier that just labels every instance as the most frequent class.  
- `featureExtractorsBasic.py` -- Abstract super class `FeatureExtractor` as well as implementations of simple feature extractors. You should look at these before implementing your enhanced feature extractors.
- `util.py`	-- Code defining some useful tools. These may save you a lot of time.

Supporting files you can probably ignore and should *not* edit:

- `dataClassifer.py` -- The main program for running your classifiers. 
- `porter2.py`	-- Code for performing word-stemming. See how it might be used inside the `EmailFeatureExtractor`.
- `samples.py`	-- I/O code to read in the classification data.


### Running a classifier

For this lab, you can work mostly from the VM command line.

	vagrant@ubuntu:~$ cd /vagrant/lab7

All interactions with the code will be through the "main" program `dataClassifer.py`.  You can see the available options, by calling it with the `--help` flag.

	vagrant@ubuntu:/vagrant/lab7$ python dataClassifier.py --help
	...

To get started, run the `MostFrequentClassifier` on the restaurant dataset, training on 10 examples and testing on 2.

	vagrant@ubuntu:/vagrant/lab7$ python dataClassifier.py -d restaurant.arff -c mostFrequent -t 10 -s 2

The `MostFrequentClassifier` is a simple baseline classifier that finds the most frequently occurring class label in the training data. To classify a test instance, it simply assigns it the most frequent label. You should see that it has accuracy of 0 on this simple example because the most frequent label is yes but the two test instances happen to have the label no.  Try a different train/test split.  Can you get an accuracy above 0%?

Browse the source code for `MostFrequentClassifier` to get a basic sense of how classifier training and testing works.

The restaurant dataset is encoded in [Attribute-Relation File Format (ARFF) format](http://www.cs.waikato.ac.nz/ml/weka/arff.html). The format is fairly self explanatory, but you can read the documentation for it here. Browse the restaurant dataset by opening the file `data/arffdata/restaurant.arff` in a text editor. It is also shown below.

	Restaurant dataset

	@relation Restaurant.symbolic
	@attribute Alternative {yes,no}
	@attribute Bar {yes,no}
	@attribute FridaySat {yes,no}
	@attribute Hunger {yes,no}
	@attribute Pat {some,full,none}
	@attribute price {$,$$,$$$}
	@attribute Rain {yes,no}
	@attribute Res {yes,no}
	@attribute Est {0-10,10-30,30-60,60+}
	@attribute Type {burger,french,italian,thai}
	@attribute wait {yes,no}

	@data
	yes,no,no,yes,some,$$$,no,yes,0-10,french,yes
	yes,no,no,yes,full,$,no,no,30-60,thai,no
	no,yes,no,no,some,$,no,no,0-10,burger,yes
	yes,no,yes,yes,full,$,no,no,10-30,thai,yes
	yes,no,yes,no,full,$$$,no,yes,60+,french,no
	no,yes,no,yes,some,$$,yes,yes,0-10,italian,yes
	no,yes,no,no,none,$,yes,no,0-10,burger,no
	no,no,no,yes,some,$$,yes,yes,0-10,thai,yes
	no,yes,yes,no,full,$,yes,no,60+,burger,no
	yes,yes,yes,yes,full,$$$,no,yes,10-30,italian,no
	no,no,no,no,none,$,no,no,0-10,thai,no
	yes,yes,yes,yes,full,$,no,no,30-60,burger,yes

**Running on other datasets** In the folder data/arffdata you will find other datasets which you can load by specifying the name of the ARFF file on the command line. For example, you can also run the `MostFrequentClassifier` on the spambase dataset and see it gets 57% accuracy on the test data.

	vagrant@ubuntu:/vagrant/lab7$ python dataClassifier.py -d spambase.arff


## Your Tasks

1. [Implement DecisionStump](README_stump.md) (in lab on Tuesday, April 4th)
2. [Implement DecisionTree](README_tree.md)
3. [Implement NaiveBayes](README_nbayes.md)
4. [Implement Perceptron](README_perceptron.md) -- *OPTIONAL* Completing the Perceptron is an optional challenge problem.
5. Complete one from the following two choices (or both as a challenge problem):
	* [Classify spam](README_spam.md).
	* [Classify digits](README_digits.md).


## Contest

The team that achieves highest combined accuracy on Spam and Digits will win a prize!



#### Acknowledgments

Some of the code for lab was adapted from the Berkeley AI course.