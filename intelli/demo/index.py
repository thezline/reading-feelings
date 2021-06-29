import nltk
#nltk.download('vader_lexicon')
#nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize

#f = open("../demo/text.txt", "r")
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