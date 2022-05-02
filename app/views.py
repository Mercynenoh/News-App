from flask import render_template, request
from app import app
from .request import get_sources, get_articles

@app.route('/')
def index():
    title = 'Welcome to the best news site'
    sources = get_sources()
    return render_template('index.html', title=title, sources= sources)

@app.route('/home')
def home():
    articles = get_articles('popular')
    return render_template('news.html',articles= articles)


 