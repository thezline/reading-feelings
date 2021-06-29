import nltk
import json
#Lines to uncomment
#nltk.download('vader_lexicon')
#nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize

class Sentiment_Analyzer:
    """ Main class to analyze the feelings in text """

    def __init__(self, txt):
        self.text = txt
        self.average = 0.0
        self.count = 0
    
    def get_sentiment(self):
        """ 
        @Desc 
        Returns a JSON with the punctuation of each sentence in the text 
        """
        
        analizer = SentimentIntensityAnalyzer()
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = tokenizer.tokenize(self.text)

        data = {}
        data['sentimentalScore'] = []
        data['normalQuestions'] = []
        data["totalAverage"] = []
        
        for sentence in sentences:
            scores = analizer.polarity_scores(sentence)
            scorePerSentence = 0
            for key in scores:
                if scores[key] == scores['compound']:
                    self.average += scores['compound']
                    self.count += 1
                scorePerSentence = scores[key]
                
            color = self.get_color(scorePerSentence)
            # Adds all the sentences with score in json format
            data["sentimentalScore"].append({
                "sentence": sentence,
                "score": scorePerSentence,
                "color": color
            })

        # Adds de total average with color 
        average = float("{0:.3f}".format(self.average / self.count))
        color = self.get_color(average)

        data["totalAverage"].append({
            "average": average,
            "color": color,
        })
        
        return data

    def get_color(self, value):
        color = "#"

        if (value >= -1 and value >= -0.75):
            color = "#B70505"
        if (value >= -0.75 and value >= -0.50):
            color = "#E61010"
        if (value >= -0.50 and value >= -0.25):
            color = "#EA5555"
        if (value >= -0.25 and value >= -0.10):
            color = "#E89494"
        if (value >= -0.10 and value <= 0.10):
            color = "#C6C6C6"
        if (value >= 0.10 and value <= 0.25):
            color = "#8FE494"
        if (value >= 0.25 and value <= 0.50):
            color = "#6BDE6B"
        if (value >= 0.50 and value <= 0.75):
            color = "#10E62A"
        if (value >= 0.75 and value <= 1):
            color = "#05B710"
        
        return color
