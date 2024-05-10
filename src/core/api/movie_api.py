import requests
import configparser
import json
from PIL import ImageTk, Image
from io import BytesIO


class Movie:
    def __init__(self, name, image):
        self.name = name
        self.image = image


class MovieAPI:
    # Python dictionary containing genres and their IDs
    genre_map = {"Action": 28, "Adventure": 12, "Animation": 16, "Comedy": 35, "Crime": 80, "Documentary": 99,
                 "Drama": 18, "Family": 10751, "Fantasy": 14, "History": 36, "Horror": 27, "Music": 10402,
                 "Mystery": 9648, "Romance": 10749, "Science Fiction": 878, "TV Movie": 10770, "Thriller": 53,
                 "War": 10752, "Western": 37}

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("secrets.ini")
        self.api_key = config["secrets"]["movie_api"]
        self.headers = {
            'User-Agent': 'movie recommender for games'
        }

    def genre_name_to_str_id(self, name):
        return str(self.genre_map[name])

    def get_movie_recommendations(self, genre_list):

        genre_ids = []
        for genre in genre_list:
            genre_ids.append(self.genre_name_to_str_id(genre))

        url = f"https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}&with_genres={','.join(genre_ids)}"

        response = requests.get(url, headers=self.headers)

        data = json.loads(response.text)
        movies = []
        for movie in data["results"]:
            if not movie["adult"]:
                movie_name = movie["title"]
                movie_img_path = movie["poster_path"]
                img_url = f"https://image.tmdb.org/t/p/w500/{movie_img_path}?api_key={self.api_key}"
                img_response = requests.get(img_url, headers=self.headers)
                try:
                    movie_img = Image.open(BytesIO(img_response.content))
                    movies.append(Movie(movie_name, movie_img))
                except:
                    x = 1 # do nothing

        return movies
