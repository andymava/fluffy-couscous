import feedparser
import random
from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")

titles = list()
for entries in feed.entries:
    titles.append(entries.title)

titles = set(titles)
#print(titles)

positives = list()
for i in titles:
    result = sentiment_analysis(i)[0]
    if result["label"] == "POSITIVE" and result["score"] >= 0.98:
        positives.append(i)
       # print(i)
       # print(result["score"])

#for i in positives:
 #   print(i)
#def chooseNew():
#    global positives
n = random.randint(0, len(positives))
goodNew = positives[n]

#print(chooseNew())
    
