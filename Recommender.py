import tkinter.filedialog

from Book import Book
from Show import Show
import timeit
from tkinter import filedialog as fd
import os
import tkinter.messagebox as messagebox


class Recommender:
    def __init__(self, file_names=None):
        self.__books: dict[
            str, Book] = {}  # Stores all the Book Objects with the book ID as the key and the value as the Book Object.
        self.__shows: dict[
            str, Show] = {}  # Stores all the Show Objects with the show ID as the key and the value as the Show Object.
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
        #
        # # Counting all the associations, it should be 2x the number of lines in the associated****.csv class.
        # count = 0
        # for (o_keys, i_dict) in self.__associations.items():
        #     for (i_key, i_values) in i_dict.items():
        #         count += i_values
        # print(count)

    def loadBooks(self):
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

                self.__books[book_object.get_id()] = book_object
                line = book_file.readline()

        for book in self.__books.items():
            print(book[0], type(book[1]), book[1])
        print(self.__max_books_title_width, self.__max_books_authors_width)

    def loadShows(self):
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
        if len(self.__shows) == 0:
            return "No File Selected, Please Select a Show file."
        movielist_header = ["Title", "Runtime"]
        formatted_movielist = f"{movielist_header[0]:<{self.__max_movie_title_width + self.__spacing_between_columns}}{movielist_header[1]:<{self.__max_movie_runtime_width + self.__spacing_between_columns}}\n"

        for show_id in self.__shows.keys():
            if self.__shows[show_id].get_show_type() == 'Movie':
                show_object: Show = self.__shows[show_id]
                formatted_movielist = formatted_movielist + f"{show_object.get_title():<{self.__max_movie_title_width + self.__spacing_between_columns}}{show_object.get_show_duration_str():<{self.__max_movie_runtime_width + self.__spacing_between_columns}}\n"

        return formatted_movielist

    def getTVList(self):
        if len(self.__shows) == 0:
            return "No File Selected, Please Select a Show file."
        tvlist_header = ["Title", "Seasons"]
        formatted_tvlist = f"{tvlist_header[0]:<{self.__max_tv_title_width + self.__spacing_between_columns}}{tvlist_header[1]:<{self.__max_tv_season_width + self.__spacing_between_columns}}\n"

        for show_id in self.__shows.keys():
            if self.__shows[show_id].get_show_type() == 'TV Show':
                show_object: Show = self.__shows[show_id]
                formatted_tvlist = formatted_tvlist + f"{show_object.get_title():<{self.__max_tv_title_width + self.__spacing_between_columns}}{show_object.get_show_duration_str():<{self.__max_tv_season_width + self.__spacing_between_columns}}\n"

        return formatted_tvlist

    def getBookList(self):
        if len(self.__books) == 0:
            return "No File Selected, Please Select a Book file."
        booklist_header = ["Title", "Authors"]
        formatted_booklist = f"{booklist_header[0]:<{self.__max_books_title_width + self.__spacing_between_columns}}{booklist_header[1]:<{self.__max_books_authors_width + self.__spacing_between_columns}}\n"

        for book_id in self.__books.keys():
            book_object: Book = self.__books[book_id]
            formatted_booklist = formatted_booklist + f"{book_object.get_title():<{self.__max_books_title_width + self.__spacing_between_columns}}{book_object.get_book_author():<{self.__max_books_authors_width + self.__spacing_between_columns}}\n"

        return formatted_booklist

    def getMovieStats(self):
        movie_dict = {}

        # Rating
        rating_count = {}
        total_movies = 0
        # print(rating_count)
        for show_id, show_object in self.__shows.items():
            if show_object.get_show_type() == 'Movie':
                rating = show_object.get_show_content_rating()
                total_movies = total_movies + 1
                if rating:
                    if rating not in rating_count.keys():
                        rating_count[rating] = 1
                    else:
                        rating_count[rating] = rating_count[rating] + 1
                else:
                    rating_count['None'] = rating_count.get('None', 0) + 1

        rating_distribution = {}
        for rating, count in rating_count.items():
            percentage = round(count / total_movies * 100)
            rating_distribution[rating] = percentage

        distribution = ', '.join([f"{rating}: {percentage:.2f}%" for rating, percentage in rating_distribution.items()])

        movie_dict['rating_distribution'] = distribution

        # Average Movie Duration
        total_duration = 0
        movie_count = 0
        for show_id, show_object in self.__shows.items():
            if show_object.get_show_type() == 'Movie':
                duration = show_object.get_show_duration_str()
                if duration:
                    try:
                        duration_value = int(duration.split()[0])
                        total_duration = total_duration + duration_value
                        movie_count = movie_count + 1
                    except ValueError:
                        pass

        # Average Duration
        if movie_count > 0:
            average_duration = total_duration / movie_count
        else:
            average_duration = 0
        movie_dict['average_duration'] = f'{average_duration:.2f} minutes'

        # Director most frequency
        director_count = {}
        for show_id, show_object in self.__shows.items():
            if show_object.get_show_type() == 'Movie':
                director = show_object.get_show_director()
                if director not in director_count.keys():
                    director_count[director] = 1
                else:
                    director_count[director] = director_count[director] + 1

        freq_dir = max(director_count, key=director_count.get) if director_count else None
        movie_dict['most_movies_director'] = freq_dir if freq_dir else 'No director data found'

        # Actor with Most Movies
        actor_count = {}
        for show_id, show_object in self.__shows.items():
            if show_object.get_show_type() == 'Movie':
                actors = show_object.get_show_cast()
                if actors:
                    for actor in actors.split('\\'):
                        if actor:
                            if actor not in actor_count.keys():
                                actor_count[actor] = 0
                            actor_count[actor] = actor_count[actor] + 1

        # Actor most frequency
        freq_actor = max(actor_count, key=actor_count.get) if actor_count else None
        movie_dict['most_movies_actor'] = freq_actor if freq_actor else 'No actor data found'

        # Genre most frequency
        genre_count = {}
        for show_id, show_object in self.__shows.items():
            if show_object.get_show_type() == 'Movie':
                genres = show_object.get_show_genre()
                if genres:
                    for genre in genres.split('\\'):
                        if genre:
                            if genre not in genre_count.keys():
                                genre_count[genre] = 0
                            else:
                                genre_count[genre] = genre_count[genre] + 1

        freq_genre = max(genre_count, key=genre_count.get) if genre_count else None
        movie_dict['most_movies_genre'] = freq_genre if freq_genre else 'No genre data found'
        print("\n")
        for key in movie_dict.keys():
            print(key, movie_dict[key])

        return movie_dict

    def getTVStats(self):
        tv_dict = {}

        # Rating
        rating_count = {}
        total_shows = 0
        for show_id, show_object in self.__shows.items():
            if show_object.get_show_type() == 'TV Show':
                rating = show_object.get_show_content_rating()
                if rating:
                    total_shows = total_shows + 1
                    if rating not in rating_count.keys():
                        rating_count[rating] = 1
                    else:
                        rating_count[rating] = rating_count[rating] + 1

        rating_distribution = {}
        for rating, count in rating_count.items():
            percentage = round(count / total_shows * 100)
            rating_distribution[rating] = percentage

        distribution = ', '.join([f"{rating}: {percentage:.2f}%" for rating, percentage in rating_distribution.items()])

        tv_dict['rating_distribution'] = distribution

        # Average Seasons
        total_seasons = 0
        show_count = 0
        for show_id, show_object in self.__shows.items():
            if show_object.get_show_type() == 'TV Show':
                seasons = show_object.get_show_duration_str()
                if seasons:
                    try:
                        duration_value = int(seasons.split()[0])
                        total_seasons = total_seasons + duration_value
                        show_count = show_count + 1
                    except ValueError:
                        pass

        # Average Season duration
        if show_count > 0:
            average_duration = total_seasons / show_count
        else:
            average_duration = 0

        tv_dict['average seasons'] = f'{average_duration:.2f} seasons'

        # Actor with most TV shows
        actor_count = {}
        for show_id, show_object in self.__shows.items():
            if show_object.get_show_type() == 'TV Show':
                actors = show_object.get_show_cast()
                if actors:
                    for actor in actors.split('\\'):
                        if actor:
                            if actor not in actor_count.keys():
                                actor_count[actor] = 0
                            else:
                                actor_count[actor] = actor_count[actor] + 1

        # Actor most frequency
        freq_actor = max(actor_count, key=actor_count.get) if actor_count else None
        tv_dict['most_tvshows_actor'] = freq_actor if freq_actor else 'No actor data found'

        # Genre Most Frequency
        genre_count = {}
        for show_id, show_object in self.__shows.items():
            if show_object.get_show_type() == 'TV Show':
                genres = show_object.get_show_genre()
                if genres:
                    for genre in genres.split('\\'):
                        if genre:
                            if genre not in genre_count.keys():
                                genre_count[genre] = 0
                            else:
                                genre_count[genre] = genre_count[genre] + 1

        freq_genre = max(genre_count, key=genre_count.get) if genre_count else None
        tv_dict['most_tvshows_genre'] = freq_genre if freq_genre else 'No genre data found'
        print('\n')
        for key in tv_dict.keys():
            print(key, tv_dict[key])

        return tv_dict

    def getBookStats(self):
        book_dict = {}
        # Average Page Count
        total_pages = 0
        page_count = 0
        for book_id, book_object in self.__books.items():
            try:
                pages = book_object.get_book_page_count()
                page_value = int(pages)
                total_pages = total_pages + page_value
                page_count = page_count + 1
            except:
                pass

        # Average Page
        if page_count > 0:
            average_page = total_pages / page_count
        else:
            average_page = 0

        book_dict['average page'] = f'{average_page:.2f} pages'

        # Author most books
        author_count = {}
        for book_id, book_object in self.__books.items():
            authors = book_object.get_book_author()
            if authors:
                for author in authors.split('\\'):
                    if author:
                        if author not in author_count.keys():
                            author_count[author] = 0
                        else:
                            author_count[author] = author_count[author] + 1

        # Author Most Frequency
        freq_author = max(author_count, key=author_count.get) if author_count else None
        book_dict['most_book_author'] = freq_author if freq_author else 'No author data found'

        # Publisher most books
        publisher_count = {}
        for book_id, book_object in self.__books.items():
            publishers = book_object.get_book_publisher()
            if publishers:
                if publishers not in publisher_count.keys():
                    publisher_count[publishers] = 0
                else:
                    publisher_count[publishers] = publisher_count[publishers] + 1

        # Publisher Most Frequency
        freq_publisher = max(publisher_count, key=publisher_count.get) if publisher_count else None
        book_dict['Most_book_publisher'] = freq_publisher if freq_publisher else 'No publisher data found'
        print('\n')
        for key in book_dict.keys():
            print(key, book_dict[key])

        return book_dict

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

        # for key in self.__shows.keys():
        #     if self.__shows[key].get_show_type() == key_type:
        #         filtered_show_objects.append(self.__shows[key])

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
            result = "No Results"
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
                result = ""
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
        results = ""
        if len(key_title) + len(key_title) + len(key_author) + len(key_publisher) == 0:
            messagebox.showerror("Empty Fields Error",
                                 f"Please provide input for at least one of the following fields to search: Title, Author or Publisher or any combinations of them.")
            return "No Result"

        if not self.__books:
            messagebox.showerror("File Not Loaded Error", "Please load a Book File first.")
            return "Please load a Book file before you can perform a search with the \"Load Books\" button."

        filter_books_objects: list[Book] = [book_object for book_object in self.__books.values()]

        if not len(key_title) == 0:
            filter_books_objects: list[Book] = [book_object for book_object in filter_books_objects if book_object.get_title() == key_title]

        if not len(key_author) == 0:
            filter_books_objects: list[Book] = [book_object for book_object in filter_books_objects if key_author in book_object.get_book_author().split('\\')]

        if not len(key_publisher) == 0:
            filter_books_objects: list[Book] = [book_object for book_object in filter_books_objects if book_object.get_book_publisher() == key_publisher]

        max_title_width: int = 0
        max_author_width: int = 0
        max_publisher_width: int = 0

        if not filter_books_objects:
            results = "No Results"
            print(f"\nInput:"
                  f"\n\tTitle\t\t: '{key_title}'"
                  f"\n\tAuthor\t\t: '{key_author}'"
                  f"\n\tPublisher\t: '{key_publisher}'"
                  f"\nNo Results")
        else:
            print(f"\nInput:"
                  f"\n\tTitle\t\t: '{key_title}'"
                  f"\n\tAuthor\t\t: '{key_author}'"
                  f"\n\tPublisher\t: '{key_publisher}'"
                  f"\nResults:")

            # Finding the Maximum length of all the fields.
            for book in filter_books_objects:
                results = ""
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
        pass


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

    rec.searchTVMovies("Movie", "Standby", "", "", "Comedy")
    rec.searchBooks("Twelfth Night", "William Shakespeare", "")
    rec.searchBooks("", "John Sandford", "")

    # execution_time = timeit.timeit(rec.loadAssociations, number=1)
    # print("Execution time:", execution_time, "seconds")
