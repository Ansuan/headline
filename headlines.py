# -*- coding: utf-8 -*-
from flask import Flask
import feedparser
from flask import render_template
from flask.views import MethodView
from lxml import etree
from urllib import urlopen
import json

app= Flask(__name__)

RSS_FEED = { 'elp':'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
             'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
             'lav':'http://www.lavanguardia.com/mvc/feed/rss/politica',
             'cnn':'http://rss.cnn.com/rss/edition.rss',
             'abc':'http://sevilla.abc.es/rss/feeds/Sevilla_Sevilla.xml',
             'elm':'http://estaticos.elmundo.es/elmundo/rss/portada.xml'
}
Titles = {'elp':'El Pais: Ultimas noticas',
          'bbc':'BBC headlines',
          'lav':'La Vanguardia: Política',
          'cnn':'CNN headlines',
          'abc':'ABC: Sevilla',
          'elm':'El Mundo'
}

articles = {}
articles['elp'] = feedparser.parse(RSS_FEED['elp'])['entries'][:5]
articles['bbc'] = feedparser.parse(RSS_FEED['bbc'])['entries'][:5]
articles['lav'] = feedparser.parse(RSS_FEED['lav'])['entries'][:5]
articles['cnn'] = feedparser.parse(RSS_FEED['cnn'])['entries'][:5]
articles['abc'] = feedparser.parse(RSS_FEED['abc'])['entries'][:5]
articles['elm'] = feedparser.parse(RSS_FEED['elm'])['entries'][:5]


def getting_unres(article):
       dict1 = {
              'title':article.title,
              'link':article.link,
              'published':article.published
       }
       if hasattr(article, 'summary'):
         dict1['summary'] = article.summary
       else:
         dict1['summary'] = ''
       return dict1


@app.route("/")
def get_news():
  return render_template("home.html", articles=articles,titles=Titles)

@app.route("/news/<string(length=3):journal>")
def get_one_journal(journal):
  if(journal not in articles):
     journal='elp'
  dict_articles = {}
  dict_titles = {}
  dict_articles[journal] = articles[journal]
  dict_titles[journal] = Titles[journal]
  return render_template("home.html", articles=dict_articles,titles=dict_titles)

'''	@app.route("/elpais")
def get_newss():
  news = []
  url = 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml'
  news = feedparser.parse(url)['entries'][:5]
  return render_template("home.html", news=news, show_fotos=0, show_news=1)

  @app.route("/fotosMin")
def get_miniature():
  fotos = []
  ns={"Atom" : "http://www.w3.org/2005/Atom"}
  parser = etree.XMLParser()
  tree = etree.parse(urlopen('https://api.flickr.com/services/feeds/photos_public.gne?tags=sevilla'),parser)
  entries = tree.xpath('//Atom:entry', namespaces=ns) 
  for i in entries:
     unafoto = {}
     unafoto['link'] = i.getchildren()[1].attrib['href']
     unafoto['title'] = i.getchildren()[0].text
     unafoto['src'] = i.getchildren()[9].attrib['href']
     fotos.append(unafoto)
  return render_template("home21.html", fotos=fotos)

@app.route("/fotosSevilla")
def get_fotos():
  fotos = []
  ns={"Atom" : "http://www.w3.org/2005/Atom"}
  parser = etree.XMLParser()
  tree = etree.parse(urlopen('https://api.flickr.com/services/feeds/photos_public.gne?tags=sevilla'),parser)
  fotos = tree.xpath('//Atom:entry/Atom:title', namespaces=ns) 
  return render_template("home2.html", fotos=fotos, show_fotos=1, show_news=0)*/
'''
class NewView(MethodView) :
  def get(self, journal='elp', id=None):
     res = {}
     one_journal = []
     one_journal = articles[journal]
     res['journal']=journal
     if id is None:
        id=0;
        for article in one_journal:
            res[id] = getting_unres(article)
            id += 1
     else:
       article = one_journal[id]
       if not article:
         abort(404)
       res[id] = getting_unres(article)
     return json.dumps(res)

new_view = NewView.as_view('new_view')
app.add_url_rule('/api/news', view_func=new_view, methods=['GET'])
app.add_url_rule('/api/news/<string(length=3):journal>', view_func=new_view, methods=['GET'])
app.add_url_rule('/api/news/<string(minlength=3,maxlength=3):journal>/<int(min=0,max=4):id>', view_func=new_view, methods=['GET'])

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5300,debug=True)

