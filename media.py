import webbrowser

class Movie():
    """ This class provides a way to store relevant movie information """ 
    VALID_RATINGS = ["G","PG","PG-13","R"]

    # Allows instances can be created from the class
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        #  the self variable represents the instance of the object itself
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Opens youtube trailer in a web browser 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    # Opens link to poster image in a web browser 
    def show_image(self):
        webbrowser.open(self.poster_image_url)
