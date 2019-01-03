from flask import render_template
from flask import request
from app import app
from app.models import jumbler

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Michael'}
    return render_template('index.html', title='Home', user=user)

@app.route('/posts')
def posts():
    user = {'username': 'Michael'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('posts.html', title='Home', user=user, posts=posts)

@app.route('/results', methods=['GET', 'POST'])
def results():
    userdata = dict(request.form)
    if request.method == 'GET':
        return render_template('404.html')
    else:
        name = jumbler.shout(userdata['name'])
        breakfast = jumbler.shout(userdata['breakfast'])
        return render_template('shoutpage.html', name=name, mybreakfast=breakfast)
