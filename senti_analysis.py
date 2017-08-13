import nltk
#nltk.download()
from twython import Twython



def bagOfWords(tweets):
    wordsList = []
    for (words, sentiment) in tweets:
        wordsList.extend(words)
    return wordsList


def wordFeatures(wordList):
    wordList = nltk.FreqDist(wordList)
    wordFeatures = wordList.keys()
    return wordFeatures


def getFeatures(doc):
    docWords = set(doc)
    feat = {}
    for word in wordFeatures:
        feat['contains(%s)' % word] = (word in docWords)
    return feat


def read_tweets(fname, t_type):
    tweets = []
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        tweets.append([line, t_type])
        line = f.readline()
    f.close()
    return tweets


positiveTweets = read_tweets('happy.txt', 'positive')
negativeTweets = read_tweets('sad.txt', 'negative')

tweets = []
for (words, sentiment) in positiveTweets + negativeTweets:
    words_filtered = [e.lower() for e in nltk.word_tokenize(words) if len(e) >= 3]
    tweets.append((words_filtered, sentiment))

def classify_tweet(tweet):
    return \
        classifier.classify(getFeatures(nltk.word_tokenize(tweet)))


wordFeatures = wordFeatures(bagOfWords(tweets))

training_set = nltk.classify.apply_features(getFeatures, tweets)
##print training_set
classifier = nltk.NaiveBayesClassifier.train(training_set)

##print(classifier.show_most_informative_features(32))

ConsumerKey = "kaVYVy3MiVQlgmbjNY1c1tXgC"
ConsumerSecret = "U1SlMgkUEhX8fN2rxJNmhRkNL1wrlnYJKZzL6lOnRMMJSotiei"
AccessToken = "3571069213-0GF7pm4jGMA0xnITifvPdIvXYwfjZxc5OELnEBK"
AccessTokenSecret = "veTCGfvmIDfCRDNvDBfj8HGXqnaBBwYCvPxNsJTnvVK6G"

twitter = Twython(ConsumerKey,
                  ConsumerSecret,
                  AccessToken,
                  AccessTokenSecret)

queryText = ""
result = twitter.search(q=queryText)

for status in result["statuses"]:
    print("Tweet: {0} \n Sentiment: {1} \n".format(status["text"].encode('utf-8'),
                                                   classifier.classify(getFeatures(status["text"].split())).encode(
                                                       'utf-8')))
