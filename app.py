import uuid
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, render_template, request, redirect, url_for, session
import telegram

app = Flask(__name__, static_folder="/templates/static")
app.secret_key = "AshleighAshleighAshleigh"
app.debug = False
toolbar = DebugToolbarExtension(app)

@app.route('/', methods=['GET', 'POST'])
def greetings():
    if request.method == 'POST': # if user has submitted their name
        person = request.form['name']
        session['person'] = person
        return redirect(url_for('express_disappointment')) # redirect them to the url to express disappointment
    else:
        return render_template('index.html') # else just return the main welcome message

@app.route('/test') # to test the base.html file
def test():
    return render_template("base.html")

@app.route('/disappointment')
def express_disappointment():
    return render_template('disappointment.html')

@app.route('/details', methods=['GET', 'POST'])
def ask_for_details():
    if request.method == 'POST':
        session['plan'] = request.form['plan']
        session['date'] = request.form['date']
        session['time'] = request.form['time']
        session['location'] = request.form['location']
        return redirect(url_for('success'))
    return render_template('askfordetails.html')

@app.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('success.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/send-message', methods=['GET'])
def send_message():
    with open ('bot_token', 'r') as f:
        bot_token = f.readline()
    with open ('chat_id', 'r') as f:
        chat_id = f.readline()
    bot = telegram.Bot(bot_token)
    bot.sendMessage(chat_id=chat_id, text=construct_message())
    return render_template('sendmessage.html')

def construct_message():
    return "Hey! New confirmation from " + session['person'] + ":" + "\nWe're going to " + session['plan'] + " \non " + session['date'] + " \nat " + session['time'] + " \nat " + session['location']

if __name__ == '__main__':
    app.run()
