import tweepy
import datetime
import random 
from time import sleep
from good import good_new


consumer_key = "XXX"
consumer_secret = "XXX"
acces_token = "XXX"
acces_token_secret = "XXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth)

def publicdate():
    dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
    hoy = datetime.date.today().weekday()
    to_publish = "Hoy es " + dias[hoy]
    api.update_status(to_publish)
    sleep(3600)
    # print(to_publish) 
    # print(datetime.date.today().weekday())

def acertijos():
    with open ("acertijos.txt") as file: 
        acertijos = file.read()
    acertijos = acertijos.split('\n')
    with open("respuestas.txt") as file:
        respuestas = file.read()
    respuestas = respuestas.split('\n')
    n = random.randint(0, len(acertijos))
    api.update_status(str(acertijos[n]) + "\n\n\n" + str(respuestas[n]))
    sleep(3600)
    

def chistes():
    with open ("chistes.txt", encoding="utf-8") as file:
        c = file.read()
    chiste = c.split("\n")
    n = random.randint(0, len(chistes))
    api.status_update(chiste[n])
    sleep(3600)


publicdate()
acertijos()
publicaAcertijo()
chistes()
api.update_status(news)
