import media
import fresh_tomatoes

# Information for various movies
deadpool = media.Movie("Deadpool", "Adventure of a comic book anti-hero",
                        "http://www.impawards.com/2016/posters/deadpool_ver5.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=gtTfd6tISfw")

thor = media.Movie("Thor: Ragnarok", "I'm not entirely sure",
                    "http://pre08.deviantart.net/6e83/th/pre/i/2016/255/6/1/thor__ragnarok_poster_by_bakikayaa-daheka0.jpg",  # NOQA
                    "https://youtu.be/v7MGUNV8MxU")

hunger_games = media.Movie("Hunger Games", "24 contestants, one winner",
                            "https://2982-presscdn-29-70-pagely.netdna-ssl.com/wp-content/uploads/2015/11/Hunger-Games-Teaser-Poster-Large.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=mfmrPu43DF8")

logan = media.Movie("Logan", "Old Man Logan",
                    "http://logan-touch.foxfilm.com/backgrounds_logan_outer.jpg",  # NOQA
                    "https://youtu.be/Div0iP65aZo")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar_ver2_xlg.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

spider_man = media.Movie("Spider-Man: Homecoming", "Spider-Man reboot",
                            "http://cdn2-www.comingsoon.net/assets/uploads/gallery/spider-man-homecoming/c7thfxlwsaapuf.jpg",  # NOQA
                            "https://youtu.be/39udgGPyYMg")

# List of movies
movies = [deadpool, thor, hunger_games, logan, avatar, spider_man]

# Launches website
fresh_tomatoes.open_movies_page(movies)
