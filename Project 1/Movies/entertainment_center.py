import media
import fresh_tomatoes

movie_title = "Toy Story"
movie_storyline = "A Story of a boy and his toys that come to life"
poster_image = "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
trailer_youtube = "https://www.youtube.com/watch?v=KYz2wyBy3kc"

toy_story = media.Movie(movie_title, movie_storyline, poster_image, trailer_youtube)
avatar = media.Movie("Avatar", "A marine on an alien planet", \
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", \
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
edge_of_tomorrow = media.Movie("Edge of Tomorrow", "A soldier repeat the day to save the Earth", \
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg", \
                               "https://www.youtube.com/watch?v=yUmSVcttXnI")
school_of_rock = media.Movie("School of Rock", "Using rock music to learn", \
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", \
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris", \
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", \
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors", \
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", \
                                "https://www.youtube.com/watch?v=dtiklALGz20")

hunger_games = media.Movie("Hunger Games", "A really real realith show", \
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", \
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, edge_of_tomorrow, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__module__)
# print(avatar.storyline)
# edge_of_tomorrow.show_trailer()