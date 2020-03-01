import uuid
from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, render_template, request, redirect, url_for, session, flash

from image_generator import serve_pil_image, make_pil_image

app = Flask(__name__, static_folder="/templates/static")
app.secret_key = uuid.uuid4().hex
app.debug = True
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
    return render_template('disappointment.html', person=session.get('person'))

@app.route('/details', methods=['GET', 'POST'])
def ask_for_details():
    if request.method == 'POST':
        session['plan'] = request.form['plan']
        session['date'] = request.form['date']
        session['time'] = request.form['time']
        session['location'] = request.form['location']
        return redirect(url_for('detail_confirmation'))
    return render_template('askfordetails.html', person=session.get('person'))

@app.route('/confirmation', methods=['GET', 'POST'])
def detail_confirmation():
    return render_template('confirmation.html')

@app.route('/image.jpeg')
def serve_img():
    if all(val is not "" for val in session.values()):
        img = make_pil_image(session.get('person'), session.get('plan'), session.get('date'), session.get('time'), session.get('location'))
        return serve_pil_image(img)
    else:
        flash("You haven't entered everything!")
        return redirect(url_for('ask_for_details'))

if __name__ == '__main__':
    app.run()
