from core.api.game_api import *
from core.api.movie_api import *
import random


class GameParser:
    movie_genres = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy",
                    "Historical", "Horror", "Musical", "Mystery", "Romance", "Science Fiction", "Thriller", "War",
                    "Western"]

    movie_mapper = {
        "Action": ["Action"],
        "Action-Adventure": ["Action", "Adventure"],
        "Adventure": ["Adventure", "Action"],
        "Baseball": ["Action", "Documentary"],
        "Basketball": ["Action", "Documentary"],
        "Billiards": ["Drama", "Sport"],
        "Block-Breaking": ["Western"],
        "Bowling": ["Action", "Documentary"],
        "Boxing": ["Action", "Drama", "Crime"],
        "Brawler": ["Action", "Drama"],
        "Card Game": ["Mystery", "Documentary"],
        "Cricket": ["Documentary"],
        "Driving/Racing": ["Action", "Thriller", "Romance"],
        "Educational": ["Documentary", "History", "Romance"],
        "Fighting": ["Action", "Drama", "Thriller"],
        "First-Person Shooter": ["Action", "War", "Western", "Thriller", "History"],
        "Fishing": ["Comedy"],
        "Fitness": ["Romance", "Drama"],
        "Flight Simulator": ["Romance", "Drama", "Documentary"],
        "Football": ["Documentary"],
        "Gambling": ["Crime", "Comedy", "Drama"],
        "Golf": ["Family", "Drama"],
        "Hockey": ["Family", "Action"],
        "Light-Gun Shooter": ["Action", "Crime", "War", "Thriller", "Western"],
        "MMORPG": ["Fantasy", "Romance", "Mystery", "Music"],
        "MOBA": ["Family", "Action", "Adventure", "Fantasy", "War", "Thriller"],
        "Music/Rhythm": ["Music", "Action"],
        "Pinball": ["Documentary"],
        "Platformer": ["Adventure", "Action"],
        "Puzzle": ["Mystery", "Mystery", "Mystery"],
        "Real-Time Strategy": ["War"],
        "Role-Playing": ["Adventure", "Fantasy"],
        "Shoot ‘Em Up": ["Action", "Crime", "War", "Thriller", "Western"],
        "Shooter": ["Action", "Crime", "War", "Thriller", "Western"],
        "Simulation": ["Romance", "Science Fiction"],
        "Skateboarding": ["Documentary", "Western", "Action"],
        "Snowboarding/Skiing": ["Adventure", "Thriller"],
        "Soccer": ["Drama", "Comedy"],
        "Sports": ["Documentary", "Drama", "Family"],
        "Strategy": ["Documentary", "Science Fiction", "War", "Family"],
        "Tennis": ["Thriller", "Family", "Adventure"],
        "Text Adventure": ["Horror", "Fantasy", "Family", "Science Fiction", "Thriller"],
        "Track & Field": ["Action", "Family", "Drama"],
        "Trivia/Board Game": ["Mystery", "Family"],
        "Vehicular Combat": ["Action", "War", "Crime", "Drama"],
        "Wrestling": ["Action", "War", "Drama"],
        "Abstract": ["Fiction"],
        "Adult": ["Romance", "Drama", "Family"],
        "Alternative Historical": ["War", "Documentary"],
        "Anime": ["Animation", "Animation", "Animation", "Animation"],
        "Aquatic": ["Music"],
        "Civil War": ["War"],
        "Comedy": ["Comedy"],
        "Comic Book": ["Action", "Adventure"],
        "Crime": ["Crime", "Thriller"],
        "Cyberpunk": ["Science Fiction", "Science Fiction", "Science Fiction"],
        "Dating": ["Romance", "Comedy", "Family", "Romance", "Romance", "Romance"],
        "Egyptian": ["History", "Mystery", "Documentary"],
        "Espionage": ["Mystery", "Thriller"],
        "Fantasy": ["Fantasy", "Fantasy"],
        "Game Show": ["Family", "Comedy"],
        "Horror": ["Horror", "Horror"],
        "Management": ["Western"],
        "Martial Arts": ["Action", "Thriller"],
        "Mayan": ["History", "Mystery", "Documentary"],
        "Medieval": ["War", "History", "Thriller", "Documentary"],
        "Modern Military": ["War", "History", "Action", "Thriller"],
        "Motorsports": ["Action", "Drama", "Action", "Western"],
        "Post-Apocalyptic": ["Action", "Horror", "Thriller"],
        "Prehistoric": ["History", "Documentary"],
        "Sci-Fi": ["Science Fiction", "Science Fiction"],
        "Steampunk": ["Science Fiction, Adventure"],
        "Superhero": ["Action", "Mystery", "Drama"],
        "Vietnam": ["History", "Documentary"],
        "Western": ["Western"],
        "World War II": ["War", "Action", "Thriller", "Horror"]
    }

    def __init__(self):
        self.gameAPI = GameAPI()
        self.games = []
        self.movieAPI = MovieAPI()

    def add_game(self, name):
        self.games.append(self.gameAPI.get_game_by_name(name))

    def get_games(self):
        return self.games

    def remove_game(self, name):
        for i in range(len(self.games)):
            if self.games[i]["name"] == name:
                del self.games[i]
                return
        print("Game not found.")

    def update_game(self, name, new_name=None, new_genres=None):
        for i in range(len(self.games)):
            if self.games[i]["name"] == name:
                if new_name:
                    self.games[i]["name"] = new_name
                if new_genres:
                    self.games[i]["genres"] = new_genres
                return
        print("Game not found.")

    def get_movie_recommendations(self):
        movie_genres = []
        if len(self.games) == 0:
            raise Exception("no games supplied")
        for game in self.games:
            if game:
                if len(game.genres) == 0:
                    raise Exception("no games supplied")
                for genre in game.genres:
                    g_list = self.movie_mapper.get(genre)
                    for g in g_list:
                        movie_genres.append(g)
        unique_genres = list(set(movie_genres))
        if len(unique_genres) == 0:
            raise Exception("No real games provided. Could not get recommendations")
        if len(unique_genres) < 4:
            return self.movieAPI.get_movie_recommendations(unique_genres)
        else:
            return self.movieAPI.get_movie_recommendations(random.sample(unique_genres, 3))


g = GameParser()
# for i in range(1):
#     game = input("Find movies like this type of video game:")
#     g.add_game(game)

try:
    x = g.get_movie_recommendations()
    for a in x:
        print(a.name)
except:
    print("No real games provided. Could not get recommendations")
