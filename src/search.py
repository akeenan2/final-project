#!/usr/bin/env python2.7
from lxml import html
import requests

def search(keywords):
    url = "https://news.google.com/#q="
    for word in keywords[:-1]:
        url = url + word + '+'
    url = url + word
    # fetch the website
    page = requests.get(url)
    tree = html.fromstring(page.content)

    headlines = []
    links = []

    headline = tree.xpath("//h2[contains(@class,'esc-lead-article-title')]/a/span/text()")
    link = tree.xpath("//h2[contains(@class,'esc-lead-article-title')]/a/@href")

    print headline[0]
    print link[0]
