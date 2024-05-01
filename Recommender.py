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

    def getMovieList(self):
        list=[]
        max_title=0
        max_runtime=0
        formatted='Title        | Runtime\n'
        for get_id in self.__shows.items():
            for object in get_id:
                if object.get_type()=='movie':
                    title=object.get_show_title()
                    duration=object.get_show_duration()
                    max_title=max(max_title,len(title))
                    max_runtime=max(max_runtime,len(str(duration)))

        formatted=formatted+f'{"Title" :<{max_title}} | {"Runtime" :<{max_runtime}}\n'
        for get_id in self.__shows.items():
            for object in get_id:
                if object.get_type()=='movie':
                    title=object.get_show_title()
                    duration=object.get_show_duration()
                    list.append((title,duration))
                    formatted=formatted+f'{"Title" :<{max_title}} | {"Runtime" :<{max_runtime}}\n'

        return formatted



        return formatted

    def getTVList(self):
        list=[]
        max_title=0
        max_season=0
        formatted='Title        | Seasons\n'
        for get_id in self.__shows.items():
            for object in get_id:
                if object.get_type()=='TV Show':
                    title=object.get_show_title()
                    duration=object.get_show_duration()
                    list.append((title,duration))
                    formatted = formatted + f'{"Title" :<{max_title}} | {"Runtime" :<{max_season}}\n'

        for get_id in self.__shows.items():
            for object in get_id:
                if object.get_type()=='TV Show':
                    title=object.get_show_title()
                    duration=object.get_show_duration()
                    max_title=max(max_title,len(title))
                    max_season=max(max_season,len(str(duration)))
                    formatted = formatted + f'{"Title" :<{max_title}} | {"Runtime" :<{max_season}}\n'

        return formatted

    def getBookList(self):
        list=[]
        maxtitle=0
        maxauthors=0
        formatted='Title        | Authors\n'
        for book in self.__books:
            title=book.get_book_title()
            authors=', '.join(book.get_book_author())
            list.append((title,authors))
            formatted=formatted+f'{title:<12} | {authors:>12}\n'
        return formatted


    def getMovieStats(self):
        ratings={}
        total_rating=0
        total_duration=0
        count_dir={}
        count_actor={}
        count_genre={}

        for show in self.__shows.values():
            rating=show.get_rating()
            if rating in ratings:
                ratings[rating]=ratings[rating]+1
            else:
                ratings[rating]=1
            total_duration=total_duration+show.get_show_duration()

            director=show.get_show_director()
            if director in count_dir:
                count_dir[director]=count_dir[director]+1
            else:
                count_dir[director]=1

            actors=show.get_show_cast()
            actors.split('\\')
            for i in actors:
                i=i.strip()
                if i in count_actor:
                    count_actor[i]=count_actor[i]+1
                else:
                    count_actor[i]=count_actor[i]+1

            genre=show.get_show_genre()
            genre.split('\\')
            for i in genre:
                if i in count_genre:
                    count_genre[genre]=count_genre[genre]+1
                else:
                    count_genre[genre]=1


        shows=len(self.__shows)
        if shows>0:
            duration_av=total_duration/shows
        else:
            duration_av=0

        freq_dir=None
        count1=0
        for director,count in count_dir.items():
            if count>count1:
                freq_dir=director
                count1=count

        freq_actor=None
        count2=0
        for actors,count in count_actor.items():
            if count>count2:
                freq_actor=actors
                count2=count

        freq_genre=None
        count3=0
        for genre,count in count_genre.items():
            if count>count3:
                freq_genre=genre
                count3=count

        return {'Ratings: ':ratings,'Average Duration: ':round(duration_av,2),'Most Frequent Director: ':freq_dir,'Most frequent Actor: ':freq_actor,'Most Frequent Genre: ':freq_genre}

    def getTVStats(self):
        ratings={}
        seasons=0
        shows=0
        actor={}
        genre={}

        for show in self.__shows.values():
            if show.get_show_type()=='TV Show':
                rating=show.get_rating()
                if rating in ratings:
                    ratings[rating]=ratings[rating]+1
                else:
                    ratings[rating]=1

                shows=shows+1
                seasons=seasons+show.get_show_duration()

                actors=show.get_show_cast()
                actors.split('\\')
                for i in actors:
                    if i in actor:
                        actor[i]=actor[i]+1
                    else:
                        actor[i]=1

                genres=show.get_show_genre()
                genres.split('\\')
                for i in genres:
                    if i in genre:
                        genre[i]=genre[i]+1
                    else:
                        genre[i]=1
        percentage={}
        for rating,count in ratings.items():
            if shows>0:
                percentage[rating]=(count/shows)*100
            else:
                percentage[rating]=0

        actor_freq=None
        actor_count=0
        for i,j in actor.items():
            if j>actor_count:
                actor_freq=i
                actor_count=j

        genre_freq=None
        genre_count=0
        for i,j in genre.items():
            if j>genre_count:
                genre_freq=i
                genre_count=j

        return {'Ratings: ':ratings,'Percentage: ':percentage,'Seasons: ':seasons,'Shows: ':shows,'Most Frequent Actor: ':actor_freq,'Most Frequent Genre: ':genre_freq}


    def getBookStats(self):
        total_pages=0
        for book in self.__books.values():
            count=book.get_book_page_count()
            total_pages=total_pages+count
        num_books=len(self.__books)
        if num_books>0:
            avg_page=total_pages/num_books
        else:
            avg_page=0

        author_count={}
        for book in self.__books.values():
            authors=book.get_book_author()
            for i in authors:
                if i in author_count:
                    author_count[i]=author_count+1
                else:
                    author_count[i]=1
        book_author=None
        book_count=0

        for i,j in author_count.items():
            if j>book_count:
                book_author=i
                book_count=j

        publisher_count={}
        for book in self.__books.values():
            publisher=book.get_book_publisher()
            if publisher in publisher_count:
                publisher_count[publisher]=publisher_count[publisher]+1
            else:
                publisher_count[publisher]=1

        most_publisher=None
        publish_count=0

        for i,j in publisher_count.items():
            if j>publish_count:
                most_publisher=i
                publish_count=j

        return {'Average Page Count: ': round(avg_page,2),'Most Books Author: ': book_author,'Most Published Publisher: ':most_publisher}














if __name__ == '__main__':
    rec = Recommender()
    rec.loadBooks()
    rec.loadShows()
    rec.loadAssociations()
    print("test")
    # execution_time = timeit.timeit(rec.loadAssociations, number=1)
    # print("Execution time:", execution_time, "seconds")
