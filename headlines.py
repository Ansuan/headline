# -*- coding: utf-8 -*-
from flask import Flask
import feedparser
from flask import render_template
from flask.views import MethodView
from lxml import etree
from urllib import urlopen
import json

app= Flask(__name__)

	@app.route("/")
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

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5300,debug=True)

