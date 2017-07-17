import webbrowser

class Movie():

    """This class allows users to store information about movies"""

    def __init__(   self, movie_title, movie_storyline,
                    poster_image, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

# launches the trailer for the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
