# Python Movie Website Project Overview
The project submission shows a simple movie trailer website that lists some of my favorite movies, and includes links to their poster images and trailers. This is my submission for the first project in the Udacity full stack web developer nanodegree program. 

# Recreate this Python Mobie Website Project
To create your own python movie website, 
1. Download Python (at least 2.7) here: https://www.python.org/download/releases/2.7/
2. Create a file named media.py containing class movie with properties that most movies share (such as title) and functions (actions) that the class will take
```
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    def show_image(self):
        webbrowser.open(self.poster_image_url
 ```
3. Create file named entertainment_center.py with the list of movies containing the properties created in class Movie.. Example:
```
    song_of_the_sea = media.Movie("Song-of-the-sea",
                        "A boy saves his selkie sister's life by finding her enchanted coat.",
                        "https://cdn.traileraddict.com/content/gkids/song-of-the-sea.jpg",
                        "https://www.youtube.com/watch?v=HgbXWt8kM5Q")
```
4. Include an array of movies in the entertainment_center.py 
```
    movies = [song_of_the_sea, wall_e, ratatouille, alien, harry_potter, best_in_show]
```
5. Create a file named fresh_tomatoes.py that takes the list of movies and creates a website displaying their details. This file contains HTML info needed to style the page output relatively nicely.
6. Make sure to import all necessary python modules to all files (example: webbrowser), and save all files in the same folder
7. Also, import media and fresh_tomatoes to the entertainment_center.py file
8. Run entertainment_center.py to open the movie website 
9. That's it!
