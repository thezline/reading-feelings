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

            # Adds all the sentences with score in json format
            data["sentimentalScore"].append({
                "sentence": sentence,
                "score": scorePerSentence
            })

        # Adds de total average with color 
        average = float("{0:.3f}".format(self.average / self.count))
        color = self.get_color(average)

        data["totalAverage"].append({
            "average": average,
            "color": color,
        })
        
        return data

    def get_color(self, average):
        color = "#"

        if (average >= -1 and average >= -0.75):
            color = "#AB0404"
        if (average >= -0.75 and average >= -0.50):
            color = "#E20C0C"
        if (average >= -0.50 and average >= -0.25):
            color = "#EA5555"
        if (average >= -0.25 and average >=  -0.10):
            color = "#E89494"
        if (average >= -0.10 and average >=  0.10):
            color = "#B9B9B9"
        if (average >= 0.10 and average >=  0.25):
            color = "#98E894"
        if (average >= 0.25 and average >=  0.50):
            color = "#55EA55"
        if (average >= 0.50 and average >=  0.75):
            color = "#06CD0F"
        if (average >= 0.75 and average >=  1):
            color = "#009006"
        
        return color
