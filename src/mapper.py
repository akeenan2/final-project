#!/usr/bin/env python2.7
import sys
from lxml import html
import requests
from string import punctuation
import unicodedata
import getopt
import re
import db

# store the headlines/url for each news url
HEADLINES = dict()

# url - url of website being scraped
# headline_paths - a list of xpaths to scrape all the headlines
# link_paths - a list of associated xpaths to scrape all urls to those headlines
# article - a dictionary of headlines mapped to their urls
def scraper(url,headline_paths,link_paths):
    # fetch the website
    page = requests.get(url)
    tree = html.fromstring(page.content)

    headlines = []
    links = []

    # select all linked headers
    for path in headline_paths:
        headlines = headlines + tree.xpath(path)
    for link in link_paths:
        links = links + tree.xpath(link)

    # create a map of headlines to links
    articles = dict()
    for headline,link in zip(headlines,links):
        articles[headline.lower().strip()] = link.lower()

    # return the dictionary
    return articles

# headline - the headline of the article being sanitized
# words - the cleaned and useful words of the headline
def sanitize(headline):
    global common_words
    words = []
    for word in headline.split(' '):
        # ignore unicode characters
        word = word.encode('ascii','ignore')
        # clean off leading and trailing punctuation
        word = word.strip(punctuation)
        # ignore common words
        if word not in db.common_words:
            words.append(word)
    # return a listt of words
    return words

# url - url of website being scraped
# keywords - map of key words to their frequency
def mapper(url):
    global HEADLINES
    headline_paths = db.url_map[url].split(';')[0].split('|')
    url_paths = db.url_map[url].split(';')[1].split('|')
    articles = scraper(url,headline_paths,url_paths)
    HEADLINES[url] = articles
    # store the key words mapped to a count of the number of times repeated
    keywords = dict()
    # iterate through the headlines
    for headline,url in articles.iteritems():
        # if url is not valid, ignore
        if url == "javascript:void(0);":
            continue
        words = sanitize(headline)
        for word in words:
            if word in keywords:
                keywords[word] += 1
            else:
                keywords[word] = 1
    return keywords

# url - search for headlines
# keywords - tuple list of keywords with their count
def lookup(search_url,keywords):
    global HEADLINES
#    headline_paths = db.url_map[search_url].split(';')[0].split('|')
#    url_paths = db.url_map[search_url].split(';')[1].split('|')
#    articles = scraper(search_url,headline_paths,url_paths)
    # store the list of headlines that have at least one match
    headlines = []
    for headline,url in HEADLINES[search_url].iteritems():
        # if url is not valid, ignore
        if url == "javascript:void(0);":
            continue
        words = sanitize(headline)
        weight = 0 # weight of the matches
        matches = 0 # number of word matches
        for word in words:
            for key_word in keywords:
                # check for substrings
                if word in key_word[0] or key_word[0] in word:
                    weight += key_word[1]
                    matches += 1
        # only append if there was a match and the url is not null
        if matches > 0:
            if not re.match("^https?://.*",url):
                # append the url to the search url if a relative path
                url = search_url[:-1] + url
            headlines.append((matches,weight,headline,url))
    return headlines
