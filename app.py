import uuid

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, static_folder="/templates/static")
app.secret_key = uuid.uuid4().hex

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
    return render_template('disappointment.html', person=session.get('person'))

@app.route('/details', methods=['GET', 'POST'])
def ask_for_details():
    return render_template('askfordetails.html', person=session.get('person'))

if __name__ == '__main__':
    app.run()
