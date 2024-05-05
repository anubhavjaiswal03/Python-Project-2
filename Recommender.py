# Authors: Anubhav Jaiswal, Prayash Das
# Date: 04/25/24
# Description: This program contains the Recommender class and imports Book and Show module. This program contains all
# the functionalities required to successfully run the working behind RecommenderGUI program

import tkinter.filedialog

from Book import Book
from Show import Show
from tkinter import filedialog as fd
import os
import tkinter.messagebox as messagebox


class Recommender:
    def __init__(self, file_names=None):
        self.__books: dict[
            str, Book] = {}  # Stores all the Book Objects with the book ID as the key and the value as the Book Object.
        self.__shows: dict[
            str, Show] = {}  # Stores all the Show Objects with the show ID as the key and the value as the Show Object.
        self.__associations: dict[str, dict[str, int]] = {}  # Stores the relationships/associations.
        self.__max_movie_title_width = 0
        self.__max_movie_runtime_width = 0
        self.__max_tv_title_width = 0
        self.__max_tv_season_width = 0
        self.__max_books_title_width = 0
        self.__max_books_authors_width = 0
        self.__spacing_between_columns = 2  # Adds space between 2 columns, Making things look pretty
        self.__default_filenames = file_names  # Purely for testing fast.

    def __str__(self):
        pass

    def loadAssociations(self):
        """
        Function for loading all the data from an association file
        """
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

    def loadBooks(self):
        """
        Function for loading all the data from a book file
        """
        self.__books = {}  # Resetting the books data member before loading books.
        book_filename = "" if self.__default_filenames is None else self.__default_filenames[0]
        while not os.path.exists(book_filename):
            book_filename = fd.askopenfilename(initialdir=os.getcwd())
            if not os.path.exists(book_filename):
                print('\033[91;1m%s\033[0m file does not exist!' % book_filename)

        with open(book_filename) as book_file:
            book_file.readline()  # Skip the first header line
            line = book_file.readline()
            # if "id" in line[0]:
            #     line = book_file.readline()

            while line:
                book_object = Book(*line.strip().split(','))

                title_width = len(book_object.get_title())
                author_width = len(book_object.get_book_author())

                if self.__max_books_title_width < title_width:
                    self.__max_books_title_width = title_width

                if self.__max_books_authors_width < author_width:
                    self.__max_books_authors_width = author_width

                self.__books[book_object.get_id()] = book_object
                line = book_file.readline()

        for book in self.__books.items():
            print(book[0], type(book[1]), book[1])
        print(self.__max_books_title_width, self.__max_books_authors_width)

    def loadShows(self):
        """
        Function for loading all the data from a show file
        """
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

                self.__shows[show_object.get_id()] = show_object
                line = show_file.readline()

        print("TV title width: ", self.__max_tv_title_width, ", TV seasons width: ", self.__max_tv_season_width)
        print("Movie title width: ", self.__max_movie_title_width, ", Movie duration width: ",
              self.__max_movie_runtime_width)

    def getMovieList(self):
        """
        Function for returning the Title and Runtime for all the stored movies
        """
        if len(self.__shows) == 0:
            return "No File Selected, Please Select a Show file."
        movielist_header = ["Title",
                            "Runtime"]  # Aligning 'Title' and 'Runtime' columns with respect to their maximum widths and adds spacing between columns.
        formatted_movielist = f"{movielist_header[0]:<{self.__max_movie_title_width + self.__spacing_between_columns}}{movielist_header[1]:<{self.__max_movie_runtime_width + self.__spacing_between_columns}}\n"

        # Building the formatted string
        for show_id in self.__shows.keys():
            if self.__shows[show_id].get_show_type() == 'Movie':  # Checking for Movie category
                show_object: Show = self.__shows[show_id]
                formatted_movielist = formatted_movielist + f"{show_object.get_title():<{self.__max_movie_title_width + self.__spacing_between_columns}}{show_object.get_show_duration_str():<{self.__max_movie_runtime_width + self.__spacing_between_columns}}\n"
                # Adding title and duration with formatted spacing between columns.
        return formatted_movielist

    def getTVList(self):
        """
        Function for returning the Title and Number of Seasons for all the stored tv shows
        """
        if len(self.__shows) == 0:
            return "No File Selected, Please Select a Show file."
        tvlist_header = ["Title",
                         "Seasons"]  # Aligning 'Title' and 'Seasons' columns with respect to their maximum widths and adds spacing between columns.
        formatted_tvlist = f"{tvlist_header[0]:<{self.__max_tv_title_width + self.__spacing_between_columns}}{tvlist_header[1]:<{self.__max_tv_season_width + self.__spacing_between_columns}}\n"

        for show_id in self.__shows.keys():
            if self.__shows[show_id].get_show_type() == 'TV Show':  # Checking for TV Show category
                show_object: Show = self.__shows[show_id]
                formatted_tvlist = formatted_tvlist + f"{show_object.get_title():<{self.__max_tv_title_width + self.__spacing_between_columns}}{show_object.get_show_duration_str():<{self.__max_tv_season_width + self.__spacing_between_columns}}\n"
                # Adding title and duration with formatted spacing between columns.
        return formatted_tvlist

    def getBookList(self):
        """
        Function for returning Title and Author(s) for all the stored books
        """
        if len(self.__books) == 0:
            return "No File Selected, Please Select a Book file."
        booklist_header = ["Title",
                           "Authors"]  # Aligning 'Title' and 'Authors' columns with respect to their maximum widths and adds spacing between columns.
        formatted_booklist = f"{booklist_header[0]:<{self.__max_books_title_width + self.__spacing_between_columns}}{booklist_header[1]:<{self.__max_books_authors_width + self.__spacing_between_columns}}\n"

        for book_id in self.__books.keys():
            book_object: Book = self.__books[book_id]
            formatted_booklist = formatted_booklist + f"{book_object.get_title():<{self.__max_books_title_width + self.__spacing_between_columns}}{book_object.get_book_author():<{self.__max_books_authors_width + self.__spacing_between_columns}}\n"
            # Adding each book's title and authors with formatting spacing between columns
        return formatted_booklist

    def getMovieStats(self):
        """
        Function for returning all the statistics regarding movies such as ratings, average movie duration, director
        with the most movies, actor with the most movies, most frequent movie genre
        """
        # Initializing a new dictionary
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
            for show_id, show in self.__shows.items():
                if show.get_show_type() == "Movie":
                    total_movies += 1
                    movie = show
                    title = movie.get_title()
                    rating = movie.get_show_content_rating()
                    duration_str = movie.get_show_duration_str()
                    duration_int = movie.get_show_duration()
                    directors = movie.get_show_director()
                    actors = movie.get_show_cast()
                    genres = movie.get_show_genre()

                    movie_stats['movies'].append([show_id, title, rating, duration_str])

                    # Ratings distribution
                    if rating is not None:
                        movie_stats['ratings'][rating] = movie_stats['ratings'].get(rating, {'count': 0})
                        movie_stats['ratings'][rating]['count'] += 1
                    else:
                        movie_stats['ratings']['None'] = movie_stats['ratings'].get('None', {'count': 0})
                        movie_stats['ratings']['None']['count'] += 1  # Checking if there are empty spaces in the Rating
                        # distribution and considering them as 'None'

                    # Average duration
                    movie_stats['average_duration'] += duration_int

                    # Directors
                    if directors:
                        for director in directors.split('\\'):  # Splitting the director's name
                            director = director.strip()
                            if director:
                                movie_stats['directors'][director] = movie_stats['directors'].get(director,
                                                                                                  {'count': 0})
                                movie_stats['directors'][director]['count'] += 1
                                if movie_stats['directors'][director]['count'] > max_director_count:
                                    max_director_count = movie_stats['directors'][director]['count']
                                    movie_stats[
                                        'most_frequent_director'] = director  # Calculating for the most frequent
                                    # director

                    # Actors
                    if actors:
                        for actor in actors.split('\\'):  # Splitting the actor's name
                            actor = actor.strip()
                            if actor:
                                movie_stats['actors'][actor] = movie_stats['actors'].get(actor, {'count': 0})
                                movie_stats['actors'][actor]['count'] += 1
                                if movie_stats['actors'][actor]['count'] > max_actor_count:
                                    max_actor_count = movie_stats['actors'][actor]['count']
                                    movie_stats[
                                        'most_frequent_actor'] = actor  # Calculating for the most frequent actor
                                    # in Movies

                    # Genre
                    if genres:
                        for genre in genres.split('\\'):  # Splitting the genre
                            genre = genre.strip()
                            if genre:
                                movie_stats['genres'][genre] = movie_stats['genres'].get(genre, {'count': 0})
                                movie_stats['genres'][genre]['count'] += 1
                                if movie_stats['genres'][genre]['count'] > max_genre_count:
                                    max_genre_count = movie_stats['genres'][genre]['count']
                                    movie_stats[
                                        'most_frequent_genre'] = genre  # Calculating for the most frequent genre

            # Calculate average duration
            if total_movies > 0:
                movie_stats['average_duration'] = f"{(movie_stats['average_duration'] / total_movies):.2f}"

            # Calculate ratings distribution using the total count of ratings

            for rating_info in movie_stats['ratings'].values():
                rating_info['distribution'] = f"{((rating_info['count'] / total_movies) * 100):.2f}"

        else:
            return "No shows found"
        # Edge Test Case
        # Getting the desired stats in a new dictionary
        desired_stats = {
            'rating_distribution': {key if key != '' else 'None': float(value['distribution']) for key, value in
                                    movie_stats['ratings'].items()},
            'average_movie_duration': f"{movie_stats['average_duration']} minutes",
            'most_prolific_director': movie_stats['most_frequent_director'],
            'most_prolific_actor': movie_stats['most_frequent_actor'],
            'most_frequent_genre': movie_stats['most_frequent_genre']
        }
        for key in desired_stats.keys():
            print(key, desired_stats[key])
        return desired_stats

    def getTVStats(self):
        """
        Function for returning statistics regarding TV Shows such as Ratings, average number of seasons, actor with the
        number of TV Shows, and the most number of genres for a TV show
        """
        # Initializing a new dictionary
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
            for show_id, show in self.__shows.items():
                if show.get_show_type() == "TV Show":
                    total_shows += 1
                    tv_show = show
                    title = tv_show.get_title()
                    rating = tv_show.get_show_content_rating()
                    seasons_str = tv_show.get_show_duration_str()
                    actors = tv_show.get_show_cast()
                    genres = tv_show.get_show_genre()

                    tv_stats['shows'].append([show_id, title, rating, seasons_str])

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
                        for actor in actors.split('\\'):  # Splitting the actor's name
                            actor = actor.strip()
                            if actor:
                                tv_stats['actors'][actor] = tv_stats['actors'].get(actor, {'count': 0})
                                tv_stats['actors'][actor]['count'] += 1
                                if tv_stats['actors'][actor]['count'] > max_actor_count:
                                    max_actor_count = tv_stats['actors'][actor]['count']
                                    tv_stats['most_frequent_actor'] = actor  # Calculating for the most frequent actor

                    # Genre
                    if genres:
                        for genre in genres.split('\\'):  # Splitting the genre
                            genre = genre.strip()
                            if genre:
                                tv_stats['genres'][genre] = tv_stats['genres'].get(genre, {'count': 0})
                                tv_stats['genres'][genre]['count'] += 1
                                if tv_stats['genres'][genre]['count'] > max_genre_count:
                                    max_genre_count = tv_stats['genres'][genre]['count']
                                    tv_stats['most_frequent_genre'] = genre  # Calculating for the most frequent TV show
                                    # genre
            # Calculate average seasons
            if total_shows > 0:
                tv_stats['average_seasons'] = f"{(tv_stats['average_seasons'] / total_shows):.2f} seasons"

                # Calculate ratings distribution using the total count of ratings
            for rating_info in tv_stats['ratings'].values():
                rating_info['distribution'] = f"{(rating_info['count'] / total_shows) * 100:.2f}"
        else:
            return "No shows found"
        # Edge Test Case
        # Getting the desired stats in a new dictionary
        desired_stats = {
            'rating_distribution': {key: float(value['distribution']) for key, value in tv_stats['ratings'].items()},
            'average_number_of_seasons': tv_stats['average_seasons'],
            'most_prolific_actor': tv_stats['most_frequent_actor'],
            'most_frequent_genre': tv_stats['most_frequent_genre']}
        for key in desired_stats.keys():
            print(key, desired_stats[key])
        return desired_stats

    def getBookStats(self):
        """
        Function for returning statistics regarding books such as average page count, author with the most books,
        and the publisher with the most books.
        """
        # Initializing a new dictionary
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
                book_title = book_object.get_title()
                author = book_object.get_book_author()
                publisher = book_object.get_book_publisher()
                pages = book_object.get_book_page_count()

                book_stats['books'].append([book_id, book_title])

                # Authors
                if author:
                    for author_name in author.split('\\'):  # Splitting the Author's name
                        author_name = author_name.strip()
                        if author_name:
                            book_stats['authors'][author_name] = book_stats['authors'].get(author_name, {'count': 0})
                            book_stats['authors'][author_name]['count'] += 1
                            if book_stats['authors'][author_name]['count'] > max_author_count:
                                max_author_count = book_stats['authors'][author_name]['count']
                                book_stats[
                                    'most_frequent_author'] = author_name  # Calculating for the most frequent author

                # Publishers
                if publisher:
                    book_stats['publishers'][publisher] = book_stats['publishers'].get(publisher, {'count': 0})
                    book_stats['publishers'][publisher]['count'] += 1
                    if book_stats['publishers'][publisher]['count'] > max_publisher_count:
                        max_publisher_count = book_stats['publishers'][publisher]['count']
                        book_stats['most_frequent_publisher'] = publisher  # Calculating for the most frequent publisher

                # Calculate total pages
                if pages:
                    try:
                        total_pages += int(pages)
                    except ValueError:
                        pass

            # Calculate average page count
            if total_books > 0:
                book_stats['average_page_count'] = f"{(total_pages / total_books):.2f} pages"

        else:
            return "No books found"
        # Edge Test Case, Getting the desired stats in a new dictionary
        desired_stats = {'average_page_count': book_stats['average_page_count'],
                         'most_prolific_author': book_stats['most_frequent_author'],
                         'most_prolific_publisher': book_stats['most_frequent_publisher']}
        for key in desired_stats.keys():
            print(key, desired_stats[key])
        return desired_stats

    def searchTVMovies(self, key_type: str, key_title: str, key_director: str, key_actor: str, key_genre: str) -> str:
        """
        Function for searching TV shows and movies based on user-defined criteria and returns a formatted result string
        or error message
        """
        result = "No Results"
        show_types = ["TV Show", "Movie"]
        if key_type not in show_types:
            messagebox.showerror("Invalid Show Type", f"Please select either {show_types[0]} or {show_types[1]}")
            return result

        if len(key_title) + len(key_director) + len(key_actor) + len(key_genre) == 0:
            messagebox.showerror("Empty Fields Error",
                                 f"Please provide input for at least one of the following fields to search: Title, "
                                 f"Director, Actor or Genre or any combination of them.")
            return result

        if not self.__shows:
            messagebox.showwarning("File Not Loaded Error", "Please Load a Show File before you can perform a search.")
            return "Please Load a Show file before you can perform a search with the \"Load Shows\" button."

        # Filter for key_type
        filtered_show_objects: list[Show] = [self.__shows[key] for key in self.__shows.keys() if
                                             self.__shows[key].get_show_type() == key_type]

        # Filtering for key_title
        if not len(key_title) == 0:
            filtered_show_objects: list[Show] = [show_object for show_object in filtered_show_objects if
                                                 show_object.get_title() == key_title]

        # Filtering for key_actor
        if not len(key_actor) == 0:
            filtered_show_objects: list[Show] = [show_object for show_object in filtered_show_objects if
                                                 key_actor in show_object.get_show_cast().split('\\')]

        # Filtering for key_director
        if not len(key_director) == 0:
            filtered_show_objects: list[Show] = [show_object for show_object in filtered_show_objects if
                                                 key_director in show_object.get_show_director().split('\\')]

        # Filtering for key_genre
        if not len(key_genre) == 0:
            filtered_show_objects: list[Show] = [show_object for show_object in filtered_show_objects if
                                                 key_genre in show_object.get_show_genre().split('\\')]

        max_title_width: int = 0
        max_director_width: int = 0
        max_cast_width: int = 0
        max_genre_width: int = 0

        if not filtered_show_objects:
            print(f"\nInput:"
                  f"\n\tType\t\t: '{key_type}'"
                  f"\n\tTitle\t\t: '{key_title}'"
                  f"\n\tDirector\t: '{key_director}'"
                  f"\n\tActor\t\t: '{key_actor}'"
                  f"\n\tGenre\t\t: '{key_genre}'"
                  f"\nNo Results")
        else:
            print(f"\nInput:"
                  f"\n\tType\t\t: '{key_type}'"
                  f"\n\tTitle\t\t: '{key_title}'"
                  f"\n\tDirector\t: '{key_director}'"
                  f"\n\tActor\t\t: '{key_actor}'"
                  f"\n\tGenre\t\t: '{key_genre}'"
                  f"\nResults:")

            # Finding the Maximum length of all the fields.
            for show in filtered_show_objects:
                max_title_width = len(show.get_title()) if max_title_width < len(show.get_title()) else max_title_width
                max_director_width = len(show.get_show_director()) if max_director_width < len(
                    show.get_show_director()) else max_director_width
                max_cast_width = len(show.get_show_cast()) if max_cast_width < len(
                    show.get_show_cast()) else max_cast_width
                max_genre_width = len(show.get_show_genre()) if max_genre_width < len(
                    show.get_show_genre()) else max_genre_width

            # Building the Result String with correct spacing.
            result_header = ["Title", "Director", "Actor", "Genre"]
            result = f"{result_header[0]:<{max_title_width + self.__spacing_between_columns}}{result_header[1]:<{max_director_width + self.__spacing_between_columns}}{result_header[2]:<{max_cast_width + self.__spacing_between_columns}}{result_header[3]:<{max_genre_width + self.__spacing_between_columns}}\n"
            for show in filtered_show_objects:
                result += f"{show.get_title():<{max_title_width + self.__spacing_between_columns}}{show.get_show_director():<{max_director_width + self.__spacing_between_columns}}{show.get_show_cast():<{max_cast_width + self.__spacing_between_columns}}{show.get_show_genre():<{max_genre_width + self.__spacing_between_columns}}\n"

            print(result)

        return result

    def searchBooks(self, key_title: str, key_author: str, key_publisher: str) -> str:
        """
        Function for taking in strings, representing a title, an author,and a publisher, and returns information
        regarding books
        """
        results = "No Result"
        if len(key_title) + len(key_title) + len(key_author) + len(key_publisher) == 0:
            messagebox.showerror("Empty Fields Error",
                                 f"Please provide input for at least one of the following fields to search: Title, Author or Publisher or any combinations of them.")
            return results

        if not self.__books:
            messagebox.showerror("File Not Loaded Error", "Please load a Book File first.")
            return "Please load a Book file before you can perform a search with the \"Load Books\" button."

        filter_books_objects: list[Book] = [book_object for book_object in self.__books.values()]

        # Filter for Book Titles
        if not len(key_title) == 0:
            filter_books_objects: list[Book] = [book_object for book_object in filter_books_objects if
                                                book_object.get_title() == key_title]

        # Filter for Book Authors
        if not len(key_author) == 0:
            filter_books_objects: list[Book] = [book_object for book_object in filter_books_objects if
                                                key_author in book_object.get_book_author().split('\\')]

        # Filter for Book Publishers
        if not len(key_publisher) == 0:
            filter_books_objects: list[Book] = [book_object for book_object in filter_books_objects if
                                                book_object.get_book_publisher() == key_publisher]

        # Declaring default max field widths.
        max_title_width: int = 0
        max_author_width: int = 0
        max_publisher_width: int = 0

        if not filter_books_objects:
            print(f"\nInput:"
                  f"\n\tTitle\t\t: '{key_title}'"
                  f"\n\tAuthor\t\t: '{key_author}'"
                  f"\n\tPublisher\t: '{key_publisher}'"
                  f"\n{results}")
        else:
            print(f"\nInput:"
                  f"\n\tTitle\t\t: '{key_title}'"
                  f"\n\tAuthor\t\t: '{key_author}'"
                  f"\n\tPublisher\t: '{key_publisher}'"
                  f"\nResults:")

            # Finding the Maximum length of the required fields.
            for book in filter_books_objects:
                max_title_width = len(book.get_title()) if max_title_width < len(book.get_title()) else max_title_width
                max_author_width = len(book.get_book_author()) if max_author_width < len(
                    book.get_book_author()) else max_author_width
                max_publisher_width = len(book.get_book_publisher()) if max_publisher_width < len(
                    book.get_book_publisher()) else max_publisher_width

            # Building the Result String with correct spacing.
            result_header = ["Title", "Author", "Publisher"]
            results = f"{result_header[0]:<{max_title_width + self.__spacing_between_columns}}{result_header[1]:<{max_author_width + self.__spacing_between_columns}}{result_header[2]:<{max_publisher_width + self.__spacing_between_columns}}\n"
            for book in filter_books_objects:
                results += f"{book.get_title():<{max_title_width + self.__spacing_between_columns}}{book.get_book_author():<{max_author_width + self.__spacing_between_columns}}{book.get_book_publisher():<{max_publisher_width + self.__spacing_between_columns}}\n"

            print(results)

        return results

    def getRecommendations(self, key_type: str, key_title: str) -> str:
        """
        Function for retrieving recommendations based on the specified type(Movie, TV Show, Book) and title, utilizing
        data from associated objects and displaying the results accordingly.
        """
        results = "No Result"
        media_types = ["Movie", "TV Show", "Book"]

        if not self.__associations:
            messagebox.showerror("No Associations Loaded",
                                 "Please load the recommendation file first using, the 'Load Recommendations' button.")
            return "Please load the recommendation file first using, the 'Load Recommendations' button."

        if key_type not in media_types:
            messagebox.showerror(
                f"Invalid Type: {key_type}",
                "Please ensure to select the correct type from the drop down list."
            )
            return results
        elif key_type in media_types[0:2]:
            filtered_show_object = [show_object for show_object in list(self.__shows.values()) if
                                    show_object.get_show_type() == key_type]  # Filtering Movies and TV Show
            key_id_from_title = [show_object.get_id() for show_object in filtered_show_object if
                                 show_object.get_title() == key_title]  # Using List Comprehension to search through all the show titles and getting the show object id of the correct show.
            if key_id_from_title:
                # print(self.__associations[key_id_from_title.pop()])
                recommendations_dict: dict = self.__associations[
                    key_id_from_title.pop()]  # We assume that the titles are all unique so the list key_id_from_title only contains 1 item. We can safely pop it out.
                results = ""  # Reset the results Value
                for recommendation in recommendations_dict.keys():
                    try:
                        results += self.__books[recommendation].get_details()
                        results += "\n" + "-" * self.__max_books_title_width + "\n"  # Since we know the max title width we can use that as a measure of the length of the separating character.
                    except KeyError:
                        messagebox.showwarning("Some Books not found",
                                               "Some books are not found! Please load the correct Book file too.")
                        results += "Information Mismatch, Load the Correct Files."
                        return results
                print(results)
                return results
            else:
                messagebox.showwarning(f"0 Recommendations found",
                                       f"No recommendations found for {key_type} titled '{key_title}'.")
                return results
        elif key_type == media_types[2]:
            key_id_from_title = [book_object.get_id() for book_object in list(self.__books.values()) if
                                 book_object.get_title() == key_title]  # Using List Comprehension to search through all the show titles and getting the show object id of the correct show.
            if key_id_from_title:
                recommendations_dict: dict = self.__associations[
                    key_id_from_title.pop()]  # We assume that the titles are all unique so the list key_id_from_title only contains 1 item. We can safely pop it out.
                results = ""  # Reset the results Value
                for recommendation in recommendations_dict.keys():
                    try:
                        results += self.__shows[recommendation].get_details()
                        results += "\n" + "-" * 50 + "\n"  # Just multiplying the seperator with a fixed number.
                    except KeyError:
                        messagebox.showwarning("Some Shows not found",
                                               "Some shows are not found! Please load the correct Show file.")
                        results += "Information Mismatch, Load the Correct Files."  # Edge CAse TEst if there are associations which are coross
                        return results
                print(results)
                return results
            else:
                messagebox.showwarning(f"0 Recommendations found",
                                       f"No recommendations found for {key_type} titled '{key_title}'.")
                return results


if __name__ == '__main__':
    file_paths = ["Input Files/books100.csv",
                  "Input Files/shows100.csv",
                  "Input Files/associated100.csv"]

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

    # rec.searchTVMovies("Movie", "Standby", "", "", "Comedy")
    # rec.searchBooks("", "William Shakespeare", "")
    # rec.searchBooks("", "John Sandford", "")

    # rec.getRecommendations("", "")
    # rec.getRecommendations("Movie", "Stolen")
    # rec.getRecommendations("Movie", "It Might Be You")
    # rec.getRecommendations("TV Show", "")
    # rec.getRecommendations("Book", "")

    # execution_time = timeit.timeit(rec.loadAssociations, number=1)
    # print("Execution time:", execution_time, "seconds")
