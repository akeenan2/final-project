# list of all urls
urls = {
    "wsj":"http://www.wsj.com/",
    "huffingtonpost":"http://www.huffingtonpost.com/",
    "washingtonpost":"https://www.washingtonpost.com/",
    "nytimes":"http://www.nytimes.com/",
    "theguardian":"https://www.theguardian.com/us/",
    "cnn":"http://www.cnn.com/",
    "usatoday":"http://www.usatoday.com/",
    "dailymail":"http://www.dailymail.co.uk/ushome/index.html/",
    "abcnews":"http://abcnews.go.com/",
    "google":"https://news.google.com/"
}

# map of url to xpath for the headline and the associated url
# headline and url seperated by a comma
# multiple headlines or urls seperated by semicolons
url_map = {
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