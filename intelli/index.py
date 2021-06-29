import nltk
import json
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

        for sentence in sentences:
            scores = analizer.polarity_scores(sentence)
            scorePerSentence = {}
            for key in scores:
                if scores[key] == scores['compound']:
                    self.average += scores['compound']
                    self.count += 1
                scorePerSentence = { key: scores[key] }

            # Adds all the sentences with score in json format
            data["sentimentalScore"].append({
                "sentence": sentence,
                "score": scorePerSentence
            })

        # Adds de total average
        data["sentimentalScore"].append({
            "average": float("{0:.3f}".format(self.average / self.count)),
        })
        
        return data