# Reading feelings (RF Project)

## Description
Artificial Intelligence project in conjunction with the Flask framework. Focused on open-ended questions in surveys, RF Project analyzes if the questions that the user fills out contain a positive, negative or neutral connotation.

## Get started
To start the flask application, it just needs to execute the app.py in the root dir with the command below.

`$ python3 app.py`

> App running in the port 5050

Note: The first time you execute the app install vader_lexicon and punkt. You can do it directly in the code (Sentiment_Analyzer.py/Sentiment_Analyzer_Demo.py)

```python
#nltk.download('vader_lexicon')
#nltk.download('punkt')
```

## Technologies
                    
Name  | Version
------------- | -------------
Python  | 3.9.6
Flask  | 2.0.1
Nltk library  | 3.6.2

## Testing only the AI
In the demo directory, execute the following command:

`$ python3 Sentiment_Analyzer_Demo.py`