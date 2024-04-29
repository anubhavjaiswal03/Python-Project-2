import tkinter.filedialog

from Book import Book
from Show import Show
import timeit
from tkinter import filedialog as fd
import os


class Recommender:
    def __init__(self):
        self.__books = {}  # Stores all the Book Objects with the book ID as the key and the value as the Book Object.
        self.__shows = {}  # Stores all the Show Objects with the show ID as the key and the value as the Show Object.
        self.__associations = {}  # Stores the relationships/associations.

    def __str__(self):
        pass

    def loadAssociations(self):
        # prompt for a file dialog
        associations_filename = ""
        while not os.path.exists(associations_filename):
            book_filename = fd.askopenfilename(initialdir=os.getcwd())
            if not os.path.exists(associations_filename):
                print('\033[91;1m%s\033[0m file does not exist!' % associations_filename)

        with (open(associations_filename, 'r') as file):
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
        book_filedialog = ""
        book_filename = ""
        while not os.path.exists(book_filename):
            book_filename = fd.askopenfilename(initialdir=os.getcwd())
            if not os.path.exists(book_filename):
                print('\033[91;1m%s\033[0m file does not exist!' % book_filename)

        with open(book_filename) as book_file:
            line = book_file.readline()
            while line:
                book_object = Book(*line.strip().split(','))
                self.__books[book_object.get_book_id()] = book_object
                line = book_file.readline()

        for book in self.__books.items():
            print(book[0], book[1])

    def loadShows(self):
        book_filedialog = ""
        show_filename = ""
        while not os.path.exists(show_filename):
            show_filename = fd.askopenfilename(initialdir=os.getcwd())
            if not os.path.exists(show_filename):
                print('\033[91;1m%s\033[0m file does not exist!' % show_filename)

        with open(show_filename) as show_file:
            line = show_file.readline()
            while line:
                show_object = Show(*line.strip().split(','))
                self.__shows[show_object.get_show_id()] = show_object
                line = show_file.readline()

        for show in self.__shows.items():
            print(show[0], show[1], sep=":")


if __name__ == '__main__':
    rec = Recommender()
    rec.loadBooks()
    rec.loadShows()
    rec.loadAssociations()
    print("test")
    # execution_time = timeit.timeit(rec.loadAssociations, number=1)
    # print("Execution time:", execution_time, "seconds")
