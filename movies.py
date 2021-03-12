import imdb
import random

ia = imdb.IMDb()
search = ia.get_top250_movies()

def recommend():
    for i in range(0, 11):
        random_num = random.randrange(0, len(search))
        print(search[random_num])

recommend()