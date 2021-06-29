from flask import Flask, request, render_template
from intelli.Sentiment_Analyzer import Sentiment_Analyzer
from dotenv import load_dotenv
import os

load_dotenv()
PORT = os.getenv("PORT")
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/processSurvey', methods=['POST'])
def process_survey():
    sentimentAnalizer = Sentiment_Analyzer(request.form['openEndedQuestion'])
    data = sentimentAnalizer.get_sentiment()
    data['normalQuestions'].append({
        'firstQuestion': request.form['firstQuestion'],
        'secondQuestion': request.form['secondQuestion'],
        'thirdQuestion': request.form['thirdQuestion']
    })

    #return data
    return render_template('score.html', data = data)

if __name__ == '__main__':
    app.debug = True
    app.run(port=PORT)