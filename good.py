import feedparser
import random
from pysentimiento import SentimentAnalyzer

analyzer = SentimentAnalyzer(lang="es")

feed = feedparser.parse("https://www.bbc.com/mundo/temas/internacional/index.xml")

titles = list()

for entries in feed.entries:
    titles.append(entries.title)
    
titles = set(titles)

news = list()

for i in titles:
    result = analyzer.predict(i)
    if (result.output == "POS" or result.output == "NEU") and (result.probas["POS"] >= 0.98 or result.probas["NEU"] >= 0.98):
       news.append(i)

def chooseNew():
    global news
    n = random.randint(0, len(news))
    return news[n]

print(chooseNew())
    

