from flask import render_template
from app import app
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title ='Home'
    return render_template('index.html',title = title)


@app.route('/source/<int:source_id>')
def source(source_id):

    return render_template('news.html',id =source_id)