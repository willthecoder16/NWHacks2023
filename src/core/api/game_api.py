import requests
import configparser
import os


class Game:
    name = ""
    genres = []

    def __init__(self, name, genres):
        self.name = name
        self.genres = genres


class GameAPI:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.abspath("../parse/secrets.ini"))
        self.api_key = config["secrets"]["game_api"]
        self.headers = {
            'User-Agent': 'movie recommender for games'
        }

    def get_game_by_name(self, name):
        url = f'https://www.giantbomb.com/api/search/?api_key={self.api_key}&format=json&query={name}&resources=game'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            json_response = response.json()
            if json_response['number_of_total_results'] > 0:
                game_id = json_response['results'][0]['id']
                found_game_name = json_response['results'][0]['name']
                genres = self.get_genres(game_id)
                game = Game(found_game_name, genres)
                return game
            else:
                print("No games found with that name.")
        else:
            print(f"Error searching game: {response.status_code} - {response.reason}")

    def get_genres(self, game_id):
        url = f'https://www.giantbomb.com/api/game/{game_id}/?api_key={self.api_key}&format=json&field_list=genres,themes'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            json_response = response.json()
            genres_json = json_response['results']['genres']
            themes_json = json_response['results']['themes']
            genres = []
            for genre_json in genres_json:
                genres.append(genre_json['name'])
            for theme_json in themes_json:
                genres.append(theme_json['name'])  # treated same as genres

            return genres
        else:
            print(f"Error getting genres: {response.status_code} - {response.reason}")