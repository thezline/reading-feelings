from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def home_post():
    firstQuestion = request.form['firstQuestion']
    secondQuestion = request.form['secondQuestion']
    thirdQuestion = request.form['thirdQuestion']
    thirdQuestion = request.form['thirdQuestion']
    openEndedQuestion = request.form['openEndedQuestion']

    return openEndedQuestion

if __name__ == '__main__':
    app.debug = True
    app.run()

app.run(port=5000)