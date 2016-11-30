import media
import fresh_tomatoes

# List of my favorite movies, including their plot, poster image, and Youtube trailer

song_of_the_sea = media.Movie("Song-of-the-sea", # Calling media.Movie for each item instantiates the objects from class Movie
                        "A boy saves his selkie sister's life by finding her enchanted coat.",
                        "https://cdn.traileraddict.com/content/gkids/song-of-the-sea.jpg",
                        "https://www.youtube.com/watch?v=HgbXWt8kM5Q")
    
wall_e = media.Movie("WallE",
                     "A sad robot finds a girlfriend.",
                     "http://www.impawards.com/2008/posters/wall_e.jpg",
                     "https://www.youtube.com/watch?v=ZisWjdjs-gM")

ratatouille = media.Movie("Ratatouille",
                       "A rat who loves to cook moves to Paris",
                       "https://s-media-cache-ak0.pinimg.com/736x/c6/b0/38/c6b038f42ea34a14434144f3ea55e0a0.jpg",
                       "https://www.youtube.com/watch?v=ALUmKa_mpik")

alien = media.Movie("Alien",
                       "An alien comes out of a guy's chest. Sigourney Weaver kills bad aliens on a ship",
                       "https://ae01.alicdn.com/kf/HTB1sfnNIpXXXXaGXXXXq6xXFXXXH/-font-b-Alien-b-font-Thriller-font-b-Movie-b-font-Classic-font-b-Poster.jpg",
                       "https://www.youtube.com/watch?v=XKSQmYUaIyE")

harry_potter = media.Movie("Harry",
                       "An alien comes out of a guy's chest. Sigourney Weaver kills bad aliens on a ship",
                       "http://www.impawards.com/2001/posters/harry_potter_and_the_sorcerers_stone_ver4.jpg",
                       "https://www.youtube.com/watch?v=K1KPcXRMMo4")

best_in_show = media.Movie("Best-in-Show",
                       "An alien comes out of a guy's chest. Sigourney Weaver kills bad aliens on a ship",
                       "http://www.impawards.com/2000/posters/best_in_show.jpg",
                       "https://www.youtube.com/watch?v=yeifMjqpsg0")

# List of movies for open_movies_page function in fresh_tomatoes.py
movies = [song_of_the_sea, wall_e, ratatouille, alien, harry_potter, best_in_show]

fresh_tomatoes.open_movies_page(movies)

