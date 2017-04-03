import collections
import featureExtractorsBasic
import porter2
import re
import samples
import util


'''
-----------------------------
FEATURE EXTRACTORS FOR SPAM
-----------------------------
'''
def numCaps(s):
    '''
    Counts the number of capital letters in s.
    '''
    all_caps = 0
    for ch in s:
        if ch == ch.upper():
            all_caps += 1
    return all_caps

class EmailFeatureExtractor(featureExtractorsBasic.FeatureExtractor):
    def __init__(self):
        self.capCounts = []
        self.n = 0

    def preProcess(self, datum):
        '''
        Counts number of capitalized letters
        '''
        assert isinstance(datum, str), 'Expects datum to be a string!'
        count = numCaps(datum)
        self.capCounts.append(count)
        self.n += 1

    def finalizeFeatures(self):
        '''
        Analyzes distributions of caps and records the 25%, 50% and 75% percentiles.
        '''
        self.capCounts.sort()
        
        self.capThresholds = (self.capCounts[self.n/4], self.capCounts[self.n/2], self.capCounts[3*self.n/4])
        print 'The 25%, 50%, and 75% percentile number of capitalized letters is', self.capThresholds

    def extractFeatures(self, datum):
        '''
        Assigns a feature based on the number of capitalized letters in the email.

        All features are binary.
        '''
        assert isinstance(datum, str), 'Expects datum to be a string!'
        features = collections.Counter()

        count = numCaps(datum)
        p25, p50, p75 = self.capThresholds
        if count <= p25:
            features['fewCaps'] = 1.0
        elif count <= p50:
            features['someCaps'] = 1.0
        elif count <= p75:
            features['manyCaps'] = 1.0
        else:
            features['allCaps'] = 1.0

        return features


class EnhancedEmailFeatureExtractor(featureExtractorsBasic.FeatureExtractor):
    '''
    Your enhanced email extractor here.

    extractFeatures should return a dictionary or a util.Counter() of features
    for this datum (datum is of type string, representing the body of the email).


    Hint: you might find it handy to use functions regular expressions and porter2.stem.
    '''

    def __init__(self):
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def preProcess(self, datum):

        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def finalizeFeatures(self):

        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def extractFeatures(self, datum):

        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


'''
-----------------------------
FEATURE EXTRACTORS FOR DIGITS
-----------------------------
'''

class DigitFeatureExtractor(featureExtractorsBasic.FeatureExtractor):
    '''
    Handles digit data.  Expects datum to be of type samples.DigitDatum
    '''
    def extractFeatures(self, datum):
        """
        Returns a set of pixel features indicating whether
        each pixel in the provided datum is white (0) or gray/black (1)
        """
        assert isinstance(datum, samples.DigitDatum), 'Expects datum to be a digit!'
        a = datum.getPixels()

        features = collections.Counter()
        for x in range(datum.width):
            for y in range(datum.height):
                if datum.getPixel(x, y) > 0:
                    features[(x,y)] = 1
                else:
                    features[(x,y)] = 0
        return features

class EnhancedDigitFeatureExtractor(DigitFeatureExtractor):

    def extractFeatures(self, datum):
        """
        Your feature extraction playground.

        You should return a dictionary or a util.Counter() of features
        for this datum (datum is of type samples.Datum).
        """
        features =  DigitFeatureExtractor.extractFeatures(self, datum)
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

        "*** [END] YOUR CODE HERE ***"
        return features
