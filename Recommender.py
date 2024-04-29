from Book import Book
from Show import Show
import timeit
import tkinter


class Recommender:
    def __init__(self):
        self.__books = []  # Stores all the Book Objects in a List
        self.__shows = []  # Stores all the Show Objects in a List
        self.__associations = {}  # Stores the relationships/associations.

    def __str__(self):
        pass


    def loadAssociations(self):
        # prompt for a file dialog
        filename = "Input Files/associated10.csv"
        with (open(filename, 'r') as file):
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


if __name__ == '__main__':
    rec = Recommender()
    execution_time = timeit.timeit(rec.loadAssociations, number=1)
    print("Execution time:", execution_time, "seconds")
