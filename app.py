from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder="/templates/static")


@app.route('/', methods=['GET', 'POST'])
def greetings():
    if request.method == 'POST':
        pesteree = request.form['name']
        return redirect(url_for('pester'), vars=pesteree)
    return render_template("index.html")

@app.route('/test') # to test the base.html file
def test():
    return render_template("base.html")

@app.route('/<pesteree>', methods=['GET', 'POST'])
def main_pestering(pesteree):
    return render_template("pester.html", pesteree=pesteree)

if __name__ == '__main__':
    app.run()
