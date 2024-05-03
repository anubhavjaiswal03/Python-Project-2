from Recommender import Recommender
import  Bonus

recommend=Recommender()
recommend.loadShows()

movie_ratings=recommend.getMovieStats()
tv_ratings=recommend.getTVStats()

Bonus.display_pie(movie_ratings,tv_ratings)
