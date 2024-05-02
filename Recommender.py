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
        self.__spacing_between_columns = 4
        self.__default_filenames = file_names  # Purely for testing fast.

    def __str__(self):
        pass

    def loadAssociations(self):
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

        movielist_header = ["Title", "Runtime"]
        formatted_movielist = f"\033[1m{movielist_header[0]:<{self.__max_movie_title_width + self.__spacing_between_columns}}{movielist_header[1]:<{self.__max_movie_runtime_width + self.__spacing_between_columns}}\033[0m\n"

        for show_id in self.__shows.keys():
            if self.__shows[show_id].get_show_type() == 'Movie':
                show_object: Show = self.__shows[show_id]
                formatted_movielist = formatted_movielist + f"{show_object.get_title():<{self.__max_movie_title_width + self.__spacing_between_columns}}{show_object.get_show_duration_str():<{self.__max_movie_runtime_width + self.__spacing_between_columns}}\n"

        return formatted_movielist

    def getTVList(self):

        tvlist_header = ["Title", "Seasons"]
        formatted_tvlist = f"\033[1m{tvlist_header[0]:<{self.__max_tv_title_width + self.__spacing_between_columns}}{tvlist_header[1]:<{self.__max_tv_season_width + self.__spacing_between_columns}}\033[0m\n"

        for show_id in self.__shows.keys():
            if self.__shows[show_id].get_show_type() == 'TV Show':
                show_object: Show = self.__shows[show_id]
                formatted_tvlist = formatted_tvlist + f"{show_object.get_title():<{self.__max_tv_title_width + self.__spacing_between_columns}}{show_object.get_show_duration_str():<{self.__max_tv_season_width + self.__spacing_between_columns}}\n"

        return formatted_tvlist

    def getBookList(self):

        booklist_header = ["Title", "Authors"]
        formatted_booklist = f"\033[1m{booklist_header[0]:<{self.__max_books_title_width + self.__spacing_between_columns}}{booklist_header[1]:<{self.__max_books_authors_width + self.__spacing_between_columns}}\033[0m\n"

        for book_id in self.__books.keys():
            book_object: Book = self.__books[book_id]
            formatted_booklist = formatted_booklist + f"{book_object.get_title():<{self.__max_books_title_width + self.__spacing_between_columns}}{book_object.get_book_author():<{self.__max_books_authors_width + self.__spacing_between_columns}}\n"

        return formatted_booklist

    def getMovieStats(self):
        movie_dict={}

        #Rating
        rating_count={}
        total_movies=0
        for show_id,show_object in self.__shows.items():
            if show_object.get_show_type()=='Movie':
                rating=show_object.get_show_content_rating()
                if rating:
                    total_movies=total_movies+1
                    if rating not in rating_count.keys():
                        rating_count[rating]=1
                    else:
                        rating_count[rating]+=1

        rating_distribution={}
        for rating,count in rating_count.items():
                percentage=round(count/total_movies*100)
                rating_distribution[rating]=percentage

        movie_dict['rating_distribution']=rating_distribution

        #Average Movie Duration
        total_duration=0
        movie_count=0
        for show_id,show_object in self.__shows.items():
            if show_object.get_show_type()=='Movie':
                duration=show_object.get_show_duration_str()
                if duration:
                    try:
                        duration_value=int(duration.split()[0])
                        total_duration=total_duration+duration_value
                        movie_count=movie_count+1
                    except ValueError:
                        pass

        #Average Duration
        if movie_count>0:
            average_duration=total_duration/movie_count
        else:
            average_duration=0
        movie_dict['average_duration']=f'{average_duration:.2f} minutes'

        #Director most frequency
        director_count={}
        for show_id,show_object in self.__shows.items():
            if show_object.get_show_type()=='Movie':
                director=show_object.get_show_director()
                if director not in director_count.keys():
                    director_count[director]=1
                else:
                    director_count[director]=director_count[director]+1

        freq_dir=max(director_count,key=director_count.get) if director_count else None
        movie_dict['most_movies_director']=freq_dir if freq_dir else 'No director data found'

        #Actor with Most Movies
        actor_count={}
        for show_id,show_object in self.__shows.items():
            if show_object.get_show_type()=='Movie':
                actors=show_object.get_show_cast()
                if actors:
                    for actor in actors.split('\\'):
                        if actor:
                            if actor not in actor_count.keys():
                                actor_count[actor]=0
                            actor_count[actor]=actor_count[actor]+1

        #Actor most frequency
        freq_actor=max(actor_count,key=actor_count.get) if actor_count else None
        movie_dict['most_movies_actor']=freq_actor if freq_actor else 'No actor data found'

        #Genre most frequency
        genre_count={}
        for show_id,show_object in self.__shows.items():
            if show_object.get_show_type()=='Movie':
                genres=show_object.get_show_genre()
                if genres:
                    for genre in genres.split('\\'):
                        if genre:
                            if genre not in genre_count.keys():
                                genre_count[genre]=0
                            else:
                                genre_count[genre]=genre_count[genre]+1

        freq_genre=max(genre_count,key=genre_count.get) if genre_count else None
        movie_dict['most_movies_genre']=freq_genre if freq_genre else 'No genre data found'
        print("\n")
        for key in movie_dict.keys():
            print(key,movie_dict[key])

        return movie_dict



    def getTVStats(self):
        tv_dict={}

        #Rating
        rating_count={}
        total_shows=0
        for show_id,show_object in self.__shows.items():
            if show_object.get_show_type()=='TV Show':
                rating=show_object.get_show_content_rating()
                if rating:
                    total_shows=total_shows+1
                    if rating not in rating_count.keys():
                        rating_count[rating]=1
                    else:
                        rating_count[rating]=rating_count[rating]+1

        rating_distribution={}
        for rating,count in rating_count.items():
            percentage=round(count/total_shows*100)
            rating_distribution[rating]=percentage

        distribution=', '.join([f"{rating}: {percentage:.2f}%" for rating,percentage in rating_distribution.items()])

        tv_dict['rating_distribution']=distribution

        #Average Seasons
        total_seasons=0
        show_count=0
        for show_id,show_object in self.__shows.items():
            if show_object.get_show_type()=='TV Show':
                seasons=show_object.get_show_duration_str()
                if seasons:
                    try:
                        duration_value=int(seasons.split()[0])
                        total_seasons=total_seasons+duration_value
                        show_count=show_count+1
                    except ValueError:
                        pass

        # Average Season duration
        if show_count>0:
            average_duration=total_seasons/show_count
        else:
            average_duration=0

        tv_dict['average seasons']=f'{average_duration:.2f} seasons'

        #Actor with most TV shows
        actor_count={}
        for show_id,show_object in self.__shows.items():
            if show_object.get_show_type()=='TV Show':
                actors=show_object.get_show_cast()
                if actors:
                    for actor in actors.split('\\'):
                        if actor:
                            if actor not in actor_count.keys():
                                actor_count[actor]=0
                            else:
                                actor_count[actor]=actor_count[actor]+1

        #Actor most frequency
        freq_actor=max(actor_count,key=actor_count.get) if actor_count else None
        tv_dict['most_tvshows_actor']=freq_actor if freq_actor else 'No actor data found'

        #Genre Most Frequency
        genre_count={}
        for show_id,show_object in self.__shows.items():
            if show_object.get_show_type()=='TV Show':
                genres=show_object.get_show_genre()
                if genres:
                    for genre in genres.split('\\'):
                        if genre:
                            if genre not in genre_count.keys():
                                genre_count[genre]=0
                            else:
                                genre_count[genre]=genre_count[genre]+1

        freq_genre=max(genre_count,key=genre_count.get) if genre_count else None
        tv_dict['most_tvshows_genre']=freq_genre if freq_genre else 'No genre data found'
        print('\n')
        for key in tv_dict.keys():
            print(key,tv_dict[key])

        return tv_dict


    def getBookStats(self):
        book_dict={}
        # Average Page Count
        total_pages=0
        page_count=0
        for book_id,book_object in self.__books.items():
            pages=book_object.get_book_page_count()
            page_value=int(pages.split()[0])
            total_pages=total_pages+page_value





if __name__ == '__main__':
    file_paths = ["Input Files/books10.csv",
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

    rec.loadAssociations()
    # execution_time = timeit.timeit(rec.loadAssociations, number=1)
    # print("Execution time:", execution_time, "seconds")
