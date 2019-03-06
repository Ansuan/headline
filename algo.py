# -*- coding: utf-8 -*-
from flask import Flask
import feedparser
from flask import render_template
#from flask.views import MethodView
#import json

app= Flask(__name__)

#articles = {}
articles = dict()
articles['bbc'] = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml')['entries'][:5]
articles['elpais'] = feedparser.parse('https://elpais.com/rss/elpais/portada.xml')['entries'][:5]
journals = ['bbc','elpais'] 

@app.route("/")
def get_news():
  return render_template("algo.html", article=articles)

#@app.route("/test/<peri>")
#def get_news_journall(peri):
#if peri in journals:
#	if peri == 'bbc':
#		return render_template("algo2.html", article2=articles['bbc'])
#	if peri == 'elpais':
#		return render_template("algo2.html", article2=articles['elpais'])

@app.route("/elpais")
def get_news_journa():
    return render_template("algo2.html", article2=articles['elpais'])

@app.route("/bbc")
def get_news_journal():
    return render_template("algo2.html", article2=articles['bbc'])

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5300,debug=True)

