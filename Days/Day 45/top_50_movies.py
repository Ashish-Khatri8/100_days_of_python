# Day 45 project - Top 50 movies of all time.

from bs4 import BeautifulSoup
import requests

# Scrape the data from IMDB website.
URL = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
response = requests.get(url=URL)

# Create an empty list to store movies names.
top_50_movies = []

soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select(selector="h3 a")
# Get each movie's name from the corresponding anchor tag.
for movie in movies:
    top_50_movies.append(movie.getText())

# Write the movie names in the text file.
with open("top_50_movies.txt", mode="w") as file:
    movie_no = 1
    for movie in top_50_movies:
        file.write(f"{movie_no}. {movie}\n")
        movie_no += 1
