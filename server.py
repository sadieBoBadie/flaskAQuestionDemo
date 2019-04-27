from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():

    # Renders the index page (home page)

    return render_template('index.html')


@app.route('/about')
def about():
    
    # renders the about page

    return render_template('about.html')

@app.route('/process', methods=["POST"])
def process():

    # Do something with the form info

    return redirect('/confirmation')

@app.route('/confirmation')
def confirmation():
    # Do something with the form info

    return render_template('confirmation.html')

@app.route('/search')
def search():

    terms = request.args.get('search_terms')
    print(search)
    
    # Do something with the form info

    return render_template('results.html', display_search=terms)




if __name__ == "__main__":
    app.run(debug=True)