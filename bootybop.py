import tweepy
import datetime
import random 
from time import sleep
from good import goodNew


consumer_key = "9KoTqJIWrcCPthGTcNbXs1dEA"
consumer_secret = "pyg1GtiBMN8ZgpbRa8snLwZIUmfehiV8IoCXTfhX2Fon1be9jx"
acces_token = "860676362-M8olui8Qn6BAJYgFgbAVqiiWJH1ca5H5W1d6rGul"
acces_token_secret = "NspeJeAyD9qPQCi61mGOkieVwWOIVOniIZP1jOg8NquXk"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth)

def publicdate():
    if datetime.date.today().weekday() == 0:
        topublish = "Hoy es Lunes! Buen inicio de semana."
    if datetime.date.today().weekday() == 1:
        topublish = "Hoy es Martes."
    if datetime.date.today().weekday() == 2:
        topublish = "Feliz mitad de semana. Hoy es miercoles."
    if datetime.date.today().weekday == 3:
        topublish = "Hoy es Jueves!"
    if datetime.date.today().weekday() == 4:
        topublish = "Feliz fin de semana. Hoy es Viernes!"
    if datetime.date.today().weekday() == 5:
        topublish = "Feliz Sabado."
    if datetime.date.today().weekday() == 6:
         topublish = "Buen Domingo!"
    
    api.update_status(topublish)
    print(topublish) 

# publicdate()


"""trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"]) """

with open ("acertijos.txt") as file: 
    acertijos = file.read()
acertijos = acertijos.split('\n')
with open("respuestas.txt") as file:
    respuestas = file.read()
respuestas = respuestas.split('\n')


def acertijoRand():
    n = random.randint(0, len(acertijos))
    print(n)
    print(len(acertijos))
    return (acertijos[n], respuestas[n])

def publicaAcertijo():
    acer, res = acertijoRand()
    print(acer)
    print(res)
    api.update_status(acer)
    sleep(300)
    api.update_status(res)

publicaAcertijo()

# api.update_status(goodNew)
