import sys
from lxml import html
import requests
from string import punctuation
import unicodedata
import getopt

# map of url to xpath for the headline and the associated url
# headline and url seperated by a comma
# multiple headlines or urls seperated by semicolons
url_map = {
    "http://localhost:8000/":",",
    "http://www.wsj.com/":"//a[@class='wsj-headline-link']/text(),//a[@class='wsj-headline-link']/@href",
    "http://www.huffingtonpost.com/":"//h2[@class='card__headline']/a[@class='card__link']/text(),//h2[@class='card__headline']/a[@class='card__link']/@href",
    "https://www.washingtonpost.com/":"//div[starts-with(@class,'headline')]/a/text(),//div[starts-with(@class,'headline')]/a/@href",
    "http://www.nytimes.com/":"//h2[@class='story-heading']/a/text(),//h2[@class='story-heading']/a/@href",
    "https://www.theguardian.com/us/":"//h2[@class='fc-item__title']/a/span/span[@class='js-headline-text']/text(),//h2[@class='fc-item__title']/a[@class='fc-item__link']/@href",
    "http://www.cnn.com/":"//h3[@class='cd__headline']/a/span[@class='cd__headline-text']/text(),//h3[@class='cd__headline']/a/@href",
    "http://www.usatoday.com/":"//a[contains(@class,'js-asset-link')]/div/p[contains(@class,'js-asset-headline')]/text();//a[contains(@class,'js-asset-link')]/span[contains(@class,'js-asset-headline')]/text(),//a[contains(@class,'js-asset-link')]/@href;//a[contains(@class,'js-asset-link')]/span[contains(@class,'js-asset-headline')]/text()",
    "http://www.dailymail.co.uk/ushome/index.html/":"//h2[@class='linkro-darkred']/a/text(),//h2[@class='linkro-darkred']/a/@href",
    "http://abcnews.go.com/":"//div[@class='headlines-li-div']/h1/a/text();//div[@class='caption-wrapper']/h1/a/text(),//div[@class='headlines-li-div']/h1/a/@href;//div[@class='caption-wrapper']/h1/a/@href",
    "https://news.google.com/":"//h2[@class='esc-lead-article-title']/a/span/text(),//h2[@class='esc-lead-article-title']/a/@href",
}

# common words to ignore
common_words = [
    "","about","above","across","after","against","along","amid","around","above","at","atop",
    "before","behind","below","beneath","besides","between","beyond","but","by","concerning",
    "down","during","except","for","from","in","inside","into","like","near","of","off","on",
    "onto","out","outside","over","past","regarding","since","through","throughout","to",
    "toward","towards","under","upon","until","with","within","without","the","a","an","as",
    "and","are","==","being","were","was","h==","her","us","we","who","what","where","when",
    "why","how","or","and","it","its","it's","you","your","th==","that","there","their"
]

def usage(status=0):
    print '''Usage: python mapper.py [options]...

Options:
    -u URL      path of website to analyze
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
        if word not in common_words:
            words.append(word)
    # return a l==t of words
    return words

# url - url of website being scraped
# key_words - map of key words to their frequency
def mapper(url):
    global url_map
    headline_paths = url_map[url].split(',')[0].split(';')
    url_paths = url_map[url].split(',')[1].split(';')
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

    if URL == '':
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
    for word,count in words.iteritems():
        print word + ' ' + str(count)
