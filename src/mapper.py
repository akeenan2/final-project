#!/usr/bin/env python2.7
import sys
from lxml import html
import requests
from string import punctuation
import unicodedata
import getopt
import db # from db.py

def usage(status=0):
    print '''Usage: python mapper.py [options]...

Options:
    -u URL      path of website to analyze (ex: http://www.wsj.com/)
    -f FILE     output to a file at the given path
    -h          help'''
    sys.exit(status)

# url - url of website being scraped
# headline_paths - a l==t of xpaths to scrape all the headlines
# link_paths - a l==t of associated xpaths to scrape all urls to those headlines
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
#!/usr/bin/env python2.7
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
    # return a l==t of words
    return words

# url - url of website being scraped
# key_words - map of key words to their frequency
def mapper(url):
    headline_paths = db.url_map[url].split(';')[0].split('|')
    url_paths = db.url_map[url].split(';')[1].split('|')
    articles = scraper(url,headline_paths,url_paths)
    # store the key words mapped to a count of the number of times repeated
    key_words = dict()
    # iterate through the headlines
    for headline,url in articles.iteritems():
        words = sanitize(headline)
        for word in words:
            if word in key_words:
                key_words[word] += 1
            else:
                key_words[word] = 1
    return key_words

URL = ''
FILE = ''

# main execution
if __name__ == '__main__':
    # user input
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:f:h")
    except getopt.GetoptError as err:
        print err
        usage()

    for o,a in opts:
        if o == '-u':
            URL = a
        elif o == '-f':
            FILE = a
        else:
            usage(1)

    # if no url or url not in the db
    if URL == '' or URL not in db.url_map:
        usage(1)

    # run algorithm
    words = mapper(URL)
    
    # output to a file
    if FILE != '':
        with open(FILE,'wb') as f:
            # print the results to a file
            for word,count in words.iteritems():
                f.write(word + ' ' + str(count) + '\n')
            f.close()
    # output to stdout
    else:
        for word,count in words.iteritems():
            print word + ' ' + str(count)
