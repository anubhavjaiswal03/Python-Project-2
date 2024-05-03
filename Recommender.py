import tkinter.filedialog

from Book import Book
from Show import Show
import timeit
from tkinter import filedialog as fd
import os


class Recommender:
    def __init__(self, file_names=None):
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
        pass

    def getTVStats(self):
        pass

    def getBookStats(self):
        pass

    def searchTVMovies(self, key_type: str, key_title: str, key_director: str, key_actor: str, key_genre: str) -> str:
        pass

    def searchBooks(self, key_title: str, key_author: str, key_publisher: str) -> str:
        pass

    def getRecommendations(self, key_type: str, key_title: str) -> str:
        pass


if __name__ == '__main__':
    file_paths = ["Input Files/books10.csv",
                  "Input Files/shows10.csv",
                  "Input Files/associated10.csv"]

    rec = Recommender(file_paths)

    print("Select a Book File")
    rec.loadBooks()
    print(rec.getBookList())

    print("Select a Show file")
    rec.loadShows()
    print(rec.getMovieList())
    print(rec.getTVList())

    # print(rec.getMovieStats())

    rec.loadAssociations()
    # execution_time = timeit.timeit(rec.loadAssociations, number=1)
    # print("Execution time:", execution_time, "seconds")
