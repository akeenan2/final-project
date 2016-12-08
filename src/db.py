#!/usr/bin/env python2.7
# list of all urls (ordered by general size)
urls = [
    "http://www.forbes.com/",
    "https://www.washingtonpost.com/",
    "http://www.usatoday.com/",
    "https://news.google.com/",
    "https://www.theguardian.com/us/",
    "http://www.nytimes.com/",
    "http://www.huffingtonpost.com/",
    "http://abcnews.go.com/",
    "http://www.wsj.com/",
    "http://www.dailymail.co.uk/ushome/index.html/"
]

# map of url to xpath for the headline and the associated url
# headline and url seperated by a comma
# multiple headlines or urls seperated by semicolons
url_map = {
    "http://michaelsills.com/sample_links.html":"//a/text();//a/@href",
    "http://michaelsills.com/sample_links_2.html":"//a/text();//a/@href",
    "http://www.wsj.com/":"//a[contains(@class,'wsj-headline-link')]/text();//a[contains(@class,'wsj-headline-link')]/@href",
    "http://www.huffingtonpost.com/":"//h2[contains(@class,'card__headline')]/a[contains(@class,'card__link')]/text();//h2[contains(@class,'card__headline')]/a[contains(@class,'card__link')]/@href",
    "https://www.washingtonpost.com/":"//div[contains(@class,'headline')]/a/text();//div[contains(@class,'headline')]/a/@href",
    "http://www.nytimes.com/":"//h2[contains(@class,'story-heading')]/a/text();//h2[contains(@class,'story-heading')]/a/@href",
    "https://www.theguardian.com/us/":"//h2[contains(@class,'fc-item__title')]/a/span/span[contains(@class,'js-headline-text')]/text();//h2[contains(@class,'fc-item__title')]/a[contains(@class,'fc-item__link')]/@href",
    "http://www.usatoday.com/":"//a[contains(@class,'js-asset-link')]/div/p[contains(@class,'js-asset-headline')]/text()|//a[contains(@class,'js-asset-link')]/span[contains(@class,'js-asset-headline')]/text();//a[contains(@class,'js-asset-link')]/@href|//a[contains(@class,'js-asset-link')]/span[contains(@class,'js-asset-headline')]/text()",
    "http://www.dailymail.co.uk/ushome/index.html/":"//h2[contains(@class,'linkro-darkred')]/a/text();//h2[contains(@class,'linkro-darkred')]/a/@href",
    "http://abcnews.go.com/":"//div[contains(@class,'headlines-li-div')]/h1/a/text()|//div[contains(@class,'caption-wrapper')]/h1/a/text();//div[contains(@class,'headlines-li-div')]/h1/a/@href|//div[contains(@class,'caption-wrapper')]/h1/a/@href",
    "https://news.google.com/":"//h2[contains(@class,'esc-lead-article-title')]/a/span/text();//h2[contains(@class,'esc-lead-article-title')]/a/@href",
    "http://www.forbes.com/":"//h4[contains(@class,'editable-hed')]/a/text()|//li[contains(@class,'edittools-contentitem')]/h3/a/text();//h4[contains(@class,'editable-hed')]/a/@href|//li[contains(@class,'edittools-contentitem')]/h3/a/@href",
}

# common words to ignore
common_words = [
    "","about","above","across","after","along","amid","around","above","at","atop","before",
    "behind","below","beneath","besides","between","beyond","but","by","concerning","down",
    "during","except","for","from","in","into","like","near","of","off","on","onto","out",
    "outside","over","past","regarding","since","through","throughout","to","toward","towards",
    "upon","until","with","within","the","a","an","as","and","are","is","be","being","were",
    "was","his","her","us","up","we","who","what","where","when","why","how","or","and","it","its",
    "it's","you","your","this","that","there","their","i","do","don't","he's","she's","he","she",
    "says","will","won't","can","can't","could","couldn't","they","they're","make","not","no",
    "nor","all","only","than","then","been","very","my","mine","me","may","new","one","two","has","him",
]