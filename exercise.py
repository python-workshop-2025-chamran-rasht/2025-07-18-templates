from flask import Flask, render_template

app = Flask(__name__)

title = 'Whatever Social'

@app.route('/')
def index():
    user = {'username': 'johndoe'}
    posts = [
        {
            'author': {'username': 'johndoe'},
            'content': 'lorem ipsum',
        },
        {
            'author': {'username': 'johndoe'},
            'content': 'something something',
        },
    ]

    return render_template('index.html', user=user, posts=posts)
