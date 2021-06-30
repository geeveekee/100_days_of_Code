from bs4 import BeautifulSoup
import requests
import sys
import codecs


res = requests.get("https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century")
website = res.content
soup = BeautifulSoup(website, 'html.parser', from_encoding="utf-8")
title = soup.find_all('strong')
movies = [t.get_text() for t in title]
#print(movies)

movie_list = []
j = 100
for i in range(1, 201, 2):
    movie = f"{j}) {movies[i-1]}"
    movie_list.append(movie)
    j -=1

mv = movie_list[::-1]
print(mv)

with open("movies.txt", mode="w") as file:
    for movie in mv:
        file.write(f"{movie}\n")



