# Authors: Anubhav Jaiswal, Prayash Das
# Description: This program contains the Recommender class and imports Book and Show module. This program contains all
# the functionalities required to successfully run the working behind RecommenderGUI program

import tkinter.filedialog

from Book import Book
from Show import Show
import timeit
from tkinter import filedialog as fd
import os
import tkinter.messagebox as messagebox


class Recommender:
    def __init__(self, file_names=None):
        '''
        Constructor function taking in file_names as parameters
        '''
        self.__books = {}  # Stores all the Book Objects with the book ID as the key and the value as the Book Object.
        self.__shows = {}  # Stores all the Show Objects with the show ID as the key and the value as the Show Object.
        self.__associations = {}  # Stores the relationships/associations.
        self.__max_movie_title_width = 0
        self.__max_movie_runtime_width = 0
        self.__max_tv_title_width = 0
        self.__max_tv_season_width = 0
        self.__max_books_title_width = 0
        self.__max_books_authors_width = 0
        self.__spacing_between_columns = 2  # Adds space between 2 columns, Making thigs look pretty
        self.__default_filenames = file_names  # Purely for testing fast.

    def __str__(self):
        pass

    def loadAssociations(self):
        '''
        Function for loading all the data from an association file
        '''
        self.__associations = {}  # Resetting the association data member before loading new associations.
        # prompt for a file dialog
        associations_filename = "" if self.__default_filenames is None else self.__default_filenames[2]
        while not os.path.exists(associations_filename):
            associations_filename = fd.askopenfilename(initialdir=os.getcwd())
            if not os.path.exists(associations_filename):
                print('\033[91;1m%s\033[0m file does not exist!' % associations_filename)

        with (open(associations_filename, 'r') as file):
            line = file.readline()

            # Skip the first header line
            if "id" in line[0]:
                line = file.readline()

            while line:
                id_set = line.strip().split(',')
                # Adding Association of the first id:
                if id_set[0] in self.__associations.keys():
                    inner_dictionary = self.__associations[id_set[0]]
                    if id_set[1] in inner_dictionary.keys():
                        inner_dictionary[id_set[1]] += 1
                    else:
                        inner_dictionary.update({id_set[1]: 1})
                else:
                    self.__associations.update({id_set[0]: {id_set[1]: 1}})

                # Adding Association of the second id:
                if id_set[1] in self.__associations.keys():
                    inner_dictionary = self.__associations[id_set[1]]
                    if id_set[0] in inner_dictionary.keys():
                        inner_dictionary[id_set[0]] += 1
                    else:
                        inner_dictionary.update({id_set[0]: 1})
                else:
                    self.__associations.update({id_set[1]: {id_set[0]: 1}})
                line = file.readline()

        for (key, value) in self.__associations.items():
            print(f"{key} : {value}")

        # Counting all the associations, it should be 2x the number of lines in the associated****.csv class.
        count = 0
        for (o_keys, i_dict) in self.__associations.items():
            for (i_key, i_values) in i_dict.items():
                count += i_values
        print(count)

    def loadBooks(self):
        '''
        Function for loading all of the data from a book file
        '''
        self.__books = {}  # Resetting the books data member before loading books.
        book_filename = "" if self.__default_filenames is None else self.__default_filenames[0]
        while not os.path.exists(book_filename):
            book_filename = fd.askopenfilename(initialdir=os.getcwd())
            if not os.path.exists(book_filename):
                print('\033[91;1m%s\033[0m file does not exist!' % book_filename)

        with open(book_filename) as book_file:
            # Called to skip the header
            book_file.readline()

            line = book_file.readline()

            # Skip the first header line
            if "id" in line[0]:
                line = book_file.readline()

            while line:
                book_object = Book(*line.strip().split(','))

                title_width = len(book_object.get_title())
                author_width = len(book_object.get_book_author())

                if self.__max_books_title_width < title_width:
                    self.__max_books_title_width = title_width

                if self.__max_books_authors_width < author_width:
                    self.__max_books_authors_width = author_width

                self.__books[book_object.get_book_id()] = book_object
                line = book_file.readline()

        for book in self.__books.items():
            print(book[0], type(book[1]), book[1])
        print(self.__max_books_title_width, self.__max_books_authors_width)

    def loadShows(self):
        '''
        Function for loading all of the data from a show file
        '''
        self.__shows = {}  # Resetting the shows data member.
        show_filename = "" if self.__default_filenames is None else self.__default_filenames[1]
        while not os.path.exists(show_filename):
            show_filename = fd.askopenfilename(initialdir=os.getcwd())
            if not os.path.exists(show_filename):
                print('\033[91;1m%s\033[0m file does not exist!' % show_filename)

        with open(show_filename) as show_file:
            # Called to skip the header
            show_file.readline()
            line = show_file.readline()

            while line:
                show_object = Show(*line.strip().split(','))
                title_width = len(show_object.get_title())
                duration_width = len(show_object.get_show_duration_str())
                if show_object.get_show_type() == "TV Show":
                    if self.__max_tv_title_width < title_width:
                        self.__max_tv_title_width = title_width

                    if self.__max_tv_season_width < duration_width:
                        self.__max_tv_season_width = duration_width
                else:
                    if self.__max_movie_title_width < title_width:
                        self.__max_movie_title_width = title_width

                    if self.__max_movie_runtime_width < duration_width:
                        self.__max_movie_runtime_width = duration_width

                self.__shows[show_object.get_show_id()] = show_object
                line = show_file.readline()

        for show in self.__shows.items():
            print(show[0], show[1], sep=":")
        print("TV title width: ", self.__max_tv_title_width, ", TV seasons width: ", self.__max_tv_season_width)
        print("Movie title width: ", self.__max_movie_title_width, ", Movie duration width: ",
              self.__max_movie_runtime_width)

    def getMovieList(self):
        '''
        Function for returning the Title and Runtime for all of the stored movies
        '''
        if len(self.__shows) == 0:
            return "No File Selected, Please Select a Show file."
        movielist_header = ["Title", "Runtime"] # Aligning 'Title' and 'Runtime' columns with respect to their maximum widths and adds spacing between columns.
        formatted_movielist = f"{movielist_header[0]:<{self.__max_movie_title_width + self.__spacing_between_columns}}{movielist_header[1]:<{self.__max_movie_runtime_width + self.__spacing_between_columns}}\n"

        for show_id in self.__shows.keys():
            if self.__shows[show_id].get_show_type() == 'Movie': # Checking for Movie category
                show_object: Show = self.__shows[show_id]
                formatted_movielist = formatted_movielist + f"{show_object.get_title():<{self.__max_movie_title_width + self.__spacing_between_columns}}{show_object.get_show_duration_str():<{self.__max_movie_runtime_width + self.__spacing_between_columns}}\n"
                # Adding title and duration with formatted spacing between columns.
        return formatted_movielist

    def getTVList(self):
        '''
        Function for returning the Title and Number of Seasons for all of the stored tv shows
        '''
        if len(self.__shows) == 0:
            return "No File Selected, Please Select a Show file."
        tvlist_header = ["Title", "Seasons"] # Aligning 'Title' and 'Seasons' columns with respect to their maximum widths and adds spacing between columns.
        formatted_tvlist = f"{tvlist_header[0]:<{self.__max_tv_title_width + self.__spacing_between_columns}}{tvlist_header[1]:<{self.__max_tv_season_width + self.__spacing_between_columns}}\n"

        for show_id in self.__shows.keys():
            if self.__shows[show_id].get_show_type() == 'TV Show': # Checking for TV Show category
                show_object: Show = self.__shows[show_id]
                formatted_tvlist = formatted_tvlist + f"{show_object.get_title():<{self.__max_tv_title_width + self.__spacing_between_columns}}{show_object.get_show_duration_str():<{self.__max_tv_season_width + self.__spacing_between_columns}}\n"
                # Adding title and duration with formatted spacing between columns.
        return formatted_tvlist

    def getBookList(self):
        '''
        Function for returning Title and Author(s) for all of the stored books
        '''
        if len(self.__books) == 0:
            return "No File Selected, Please Select a Book file."
        booklist_header = ["Title", "Authors"] # Aligning 'Title' and 'Authors' columns with respect to their maximum widths and adds spacing between columns.
        formatted_booklist = f"{booklist_header[0]:<{self.__max_books_title_width + self.__spacing_between_columns}}{booklist_header[1]:<{self.__max_books_authors_width + self.__spacing_between_columns}}\n"

        for book_id in self.__books.keys():
            book_object: Book = self.__books[book_id]
            formatted_booklist = formatted_booklist + f"{book_object.get_title():<{self.__max_books_title_width + self.__spacing_between_columns}}{book_object.get_book_author():<{self.__max_books_authors_width + self.__spacing_between_columns}}\n"
            # Adding each book's title and authors with formatting spacing between columns
        return formatted_booklist

    def getMovieStats(self):
        '''
        Function for returning all the statistics regarding movies such as ratings, average movie duration, director
        with the most movies, actor with the most movies, most frequent movie genre
        '''
        movie_stats = {
            'movies': [],
            'ratings': {},
            'average_duration': 0,
            'directors': {},
            'actors': {},
            'genres': {},
            'most_frequent_genre': None,
            'most_frequent_director': None,
            'most_frequent_actor': None
        }

        total_movies = 0
        max_genre_count = 0
        max_director_count = 0
        max_actor_count = 0
        if len(self.__shows) > 0:
            for id, show in self.__shows.items():
                if show.get_show_type() == "Movie":
                    total_movies += 1
                    movie = show
                    title = movie.get_show_title()
                    rating = movie.get_show_content_rating()
                    duration_str = movie.get_show_duration_str()
                    duration_int = movie.get_show_duration()
                    directors = movie.get_show_director()
                    actors = movie.get_show_cast()
                    genres = movie.get_show_genre()

                    movie_stats['movies'].append([id, title, rating, duration_str])

                    # Ratings distribution
                    movie_stats['ratings'][rating] = movie_stats['ratings'].get(rating, {'count': 0})
                    movie_stats['ratings'][rating]['count'] += 1

                    # Average duration
                    movie_stats['average_duration'] += duration_int

                    # Directors
                    if directors:
                        for director in directors.split('\\'):
                            director = director.strip()
                            if director:
                                movie_stats['directors'][director] = movie_stats['directors'].get(director,
                                                                                                  {'count': 0})
                                movie_stats['directors'][director]['count'] += 1
                                if movie_stats['directors'][director]['count'] > max_director_count:
                                    max_director_count = movie_stats['directors'][director]['count']
                                    movie_stats['most_frequent_director'] = director

                    # Actors
                    if actors:
                        for actor in actors.split('\\'):
                            actor = actor.strip()
                            if actor:
                                movie_stats['actors'][actor] = movie_stats['actors'].get(actor, {'count': 0})
                                movie_stats['actors'][actor]['count'] += 1
                                if movie_stats['actors'][actor]['count'] > max_actor_count:
                                    max_actor_count = movie_stats['actors'][actor]['count']
                                    movie_stats['most_frequent_actor'] = actor

                    # Genre
                    if genres:
                        for genre in genres.split('\\'):
                            genre = genre.strip()
                            if genre:
                                movie_stats['genres'][genre] = movie_stats['genres'].get(genre, {'count': 0})
                                movie_stats['genres'][genre]['count'] += 1
                                if movie_stats['genres'][genre]['count'] > max_genre_count:
                                    max_genre_count = movie_stats['genres'][genre]['count']
                                    movie_stats['most_frequent_genre'] = genre

            # Calculate average duration
            if total_movies > 0:
                movie_stats['average_duration'] = f"{(movie_stats['average_duration'] / total_movies):.2f}"

            # Calculate ratings distribution using the total count of ratings
            for rating_info in movie_stats['ratings'].values():
                rating_info['distribution'] = f"{((rating_info['count'] / total_movies) * 100):.2f}"

        else:
            return "No shows found"

        for key in movie_stats.keys():
            print(key, movie_stats[key])
        return movie_stats

    def getTVStats(self):
        '''
        Function for returning statistics regarding TV Shows such as Ratings, average number of seasons, actor with the
        most number of TV Shows, and the most number of genres for a TV show
        '''
        tv_stats = {
            'shows': [],
            'ratings': {},
            'average_seasons': 0,
            'actors': {},
            'genres': {},
            'most_frequent_genre': None,
            'most_frequent_actor': None
        }

        total_shows = 0
        max_genre_count = 0
        max_actor_count = 0

        if len(self.__shows) > 0:
            for id, show in self.__shows.items():
                if show.get_show_type() == "TV Show":
                    total_shows += 1
                    tv_show = show
                    title = tv_show.get_show_title()
                    rating = tv_show.get_show_content_rating()
                    seasons_str = tv_show.get_show_duration_str()
                    actors = tv_show.get_show_cast()
                    genres = tv_show.get_show_genre()

                    tv_stats['shows'].append([id, title, rating, seasons_str])

                    # Ratings distribution
                    tv_stats['ratings'][rating] = tv_stats['ratings'].get(rating, {'count': 0})
                    tv_stats['ratings'][rating]['count'] += 1

                    # Average seasons
                    if seasons_str:
                        try:
                            seasons_value = int(seasons_str.split()[0])
                            tv_stats['average_seasons'] += seasons_value
                        except ValueError:
                            pass

                    # Actors
                    if actors:
                        for actor in actors.split('\\'):
                            actor = actor.strip()
                            if actor:
                                tv_stats['actors'][actor] = tv_stats['actors'].get(actor, {'count': 0})
                                tv_stats['actors'][actor]['count'] += 1
                                if tv_stats['actors'][actor]['count'] > max_actor_count:
                                    max_actor_count = tv_stats['actors'][actor]['count']
                                    tv_stats['most_frequent_actor'] = actor

                    # Genre
                    if genres:
                        for genre in genres.split('\\'):
                            genre = genre.strip()
                            if genre:
                                tv_stats['genres'][genre] = tv_stats['genres'].get(genre, {'count': 0})
                                tv_stats['genres'][genre]['count'] += 1
                                if tv_stats['genres'][genre]['count'] > max_genre_count:
                                    max_genre_count = tv_stats['genres'][genre]['count']
                                    tv_stats['most_frequent_genre'] = genre
            # Calculate average seasons
            if total_shows > 0:
                tv_stats['average_seasons'] = f"{(tv_stats['average_seasons'] / total_shows):.2f}"

                # Calculate ratings distribution using the total count of ratings
            for rating_info in tv_stats['ratings'].values():
                rating_info['distribution'] = f"{(rating_info['count'] / total_shows) * 100:.2f}"
        else:
            return "No shows found"

        for key in tv_stats.keys():
            print(key, tv_stats[key])
        return tv_stats

    def getBookStats(self):
        '''
        Function for returning statistics regarding books such as average page count, author with the most books,
        and the publisher with the most books.
        '''
        book_stats = {
            'books': [],
            'authors': {},
            'publishers': {},
            'most_frequent_author': None,
            'most_frequent_publisher': None,
            'average_page_count': 0
        }

        total_books = 0
        total_pages = 0
        max_author_count = 0
        max_publisher_count = 0

        if len(self.__books) > 0:
            for book_id, book_object in self.__books.items():
                total_books += 1
                book_title = book_object.get_book_title()
                author = book_object.get_book_author()
                publisher = book_object.get_book_publisher()
                pages = book_object.get_book_page_count()

                book_stats['books'].append([book_id, book_title])

                # Authors
                if author:
                    for author_name in author.split('\\'):
                        author_name = author_name.strip()
                        if author_name:
                            book_stats['authors'][author_name] = book_stats['authors'].get(author_name, {'count': 0})
                            book_stats['authors'][author_name]['count'] += 1
                            if book_stats['authors'][author_name]['count'] > max_author_count:
                                max_author_count = book_stats['authors'][author_name]['count']
                                book_stats['most_frequent_author'] = author_name

                # Publishers
                if publisher:
                    book_stats['publishers'][publisher] = book_stats['publishers'].get(publisher, {'count': 0})
                    book_stats['publishers'][publisher]['count'] += 1
                    if book_stats['publishers'][publisher]['count'] > max_publisher_count:
                        max_publisher_count = book_stats['publishers'][publisher]['count']
                        book_stats['most_frequent_publisher'] = publisher

                # Calculate total pages
                if pages:
                    try:
                        total_pages += int(pages)
                    except ValueError:
                        pass

            # Calculate average page count
            if total_books > 0:
                book_stats['average_page_count'] = f"{(total_pages / total_books):.2f}"

        else:
            return "No books found"

        for key in book_stats.keys():
            print(key, book_stats[key])
        return book_stats

    def searchTVMovies(self, key_type: str, key_title: str, key_director: str, key_actor: str, key_genre: str) -> str:
        result = ""
        show_types = ["TV Show", "Movie"]
        if key_type not in show_types:
            messagebox.showerror("Invalid Show Type", f"Please select either {show_types[0]} or {show_types[1]}")
            return "No Results"

        if len(key_title) + len(key_director) + len(key_actor) + len(key_genre) == 0:
            messagebox.showerror("Empty Fields Error",
                                 f"Please provide input for at least one of the following fields to search: Title, Director, Actor or Genre or any combination of them.")
            return "No Results"

        if not self.__shows:
            messagebox.showerror("File Not Loaded Error", "Please Load a Show File Before you can perform a search.")
            return "Please Load a Show file before you can perform a search with the \"Load Shows button\"."

        return result

    def searchBooks(self, key_title: str, key_author: str, key_publisher: str) -> str:
        pass

    def getRecommendations(self, key_type: str, key_title: str) -> str:
        pass


if __name__ == '__main__':
    file_paths = ["Input Files/books100.csv",
                  "Input Files/shows100.csv",
                  "Input Files/associated10.csv"]

    rec = Recommender(file_paths)

    print("Select a Book File")
    rec.loadBooks()
    print(rec.getBookList())

    print("Select a Show file")
    rec.loadShows()
    print(rec.getMovieList())
    print(rec.getTVList())

    rec.getMovieStats()
    rec.getTVStats()
    rec.getBookStats()

    rec.loadAssociations()
    # execution_time = timeit.timeit(rec.loadAssociations, number=1)
    # print("Execution time:", execution_time, "seconds")
