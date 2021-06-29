import nltk
#Lines to uncomment
#nltk.download('vader_lexicon')
#nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize

class Sentiment_Analyzer_Demo:
    """ Demo class """

    def get_sentiment(self):
        f = open("text.txt", "r")
        analizer = SentimentIntensityAnalyzer()
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = tokenizer.tokenize(f.read())

        for sentence in sentences:
            print(sentence)
            scores = analizer.polarity_scores(sentence)
            for key in scores:
                print(key, ':', scores[key])
            print()

sentimentAnalizerDemo = Sentiment_Analyzer_Demo()
print(sentimentAnalizerDemo.get_sentiment())