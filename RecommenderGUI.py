# Authors: Anubhav Jaiswal, Prayash Das
# Date: 04/26/24
# Description: Driver Program which display the User Interface and import all the required functionalities from the
# other files and display as per the user's choice


import tkinter
from tkinter import ttk
from Recommender import Recommender
import tkinter.messagebox as messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class RecommenderGUI:
    def __init__(self):
        """
        Constructor function containing all the Notebook tabs, Buttons for User Interaction and Quitting the Program
        """
        self.credit_info_messagebox = None
        self.__recommender_object = Recommender()
        self.__main_window = tkinter.Tk()
        self.__main_window.title('Media Recommender')
        self.__main_window.geometry('1200x800')
        self.__main_window.minsize(800, 750)
        self.__button_frame = tkinter.Frame(self.__main_window)
        self.__notebook = ttk.Notebook(self.__main_window)
        self.__notebook.pack(side=tkinter.TOP, expand=1, fill=tkinter.BOTH)
        self.__button_frame.pack(side=tkinter.TOP, fill=tkinter.X)

        # Movies Tab
        self.__movies_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__movies_tab, text="Movies")
        self.__movies_list_text = tkinter.Text(self.__movies_tab, wrap=tkinter.WORD)
        self.__movies_stats_text = tkinter.Text(self.__movies_tab, wrap=tkinter.WORD)
        self.__movies_scrollbar = tkinter.Scrollbar(self.__movies_tab, orient=tkinter.VERTICAL,
                                                    command=self.__movies_list_text.yview)
        self.__movies_list_text.config(yscrollcommand=self.__movies_scrollbar.set)
        self.__movies_list_text.grid(column=0, row=0, sticky=tkinter.NSEW)
        self.__movies_scrollbar.grid(row=0, column=1, sticky=tkinter.NS)
        self.__movies_stats_text.grid(column=0, row=1, columnspan=2, sticky=tkinter.NSEW)
        self.__movies_tab.grid_rowconfigure(0, weight=1)
        self.__movies_tab.grid_columnconfigure(0, weight=1)
        self.__movies_tab.grid_rowconfigure(1, weight=1)
        self.__mutate_Text_GUI(self.__movies_list_text, "Nothing to Display Please Load a Shows file.")
        self.__mutate_Text_GUI(self.__movies_stats_text,
                               "Oops There are no numbers to Crunch Here!\nPlease Load a Shows file.")

        # TV Shows Tab
        self.__tv_shows_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__tv_shows_tab, text="TV Shows")
        self.__tv_shows_list_text = tkinter.Text(self.__tv_shows_tab, wrap=tkinter.WORD)
        self.__tv_shows_stats_text = tkinter.Text(self.__tv_shows_tab, wrap=tkinter.WORD)
        self.__tv_shows_scrollbar = tkinter.Scrollbar(self.__tv_shows_tab, orient=tkinter.VERTICAL,
                                                      command=self.__tv_shows_list_text.yview)
        self.__tv_shows_list_text.config(yscrollcommand=self.__tv_shows_scrollbar.set)
        self.__tv_shows_list_text.grid(column=0, row=0, sticky=tkinter.NSEW)
        self.__tv_shows_scrollbar.grid(row=0, column=1, sticky=tkinter.NS)
        self.__tv_shows_stats_text.grid(column=0, row=1, columnspan=2, sticky=tkinter.NSEW)
        self.__tv_shows_tab.grid_rowconfigure(0, weight=1)
        self.__tv_shows_tab.grid_columnconfigure(0, weight=1)
        self.__tv_shows_tab.grid_rowconfigure(1, weight=1)
        self.__mutate_Text_GUI(self.__tv_shows_list_text, "Nothing to Display Please Load a Shows file.")
        self.__mutate_Text_GUI(self.__tv_shows_stats_text,
                               "Oops There are no numbers to Crunch Here!\nPlease Load a Shows file.")

        # Books Tab
        self.__books_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__books_tab, text="Books")
        self.__books_list_text = tkinter.Text(self.__books_tab, wrap=tkinter.WORD)
        self.__books_stats_text = tkinter.Text(self.__books_tab, wrap=tkinter.WORD)
        self.__books_scrollbar = tkinter.Scrollbar(self.__books_tab, orient=tkinter.VERTICAL,
                                                   command=self.__books_list_text.yview)
        self.__books_list_text.config(yscrollcommand=self.__books_scrollbar.set)
        self.__books_scrollbar.grid(row=0, column=1, sticky=tkinter.NS)
        self.__books_list_text.grid(column=0, row=0, sticky=tkinter.NSEW)
        self.__books_stats_text.grid(column=0, row=1, columnspan=2, sticky=tkinter.NSEW)
        self.__books_tab.grid_rowconfigure(0, weight=1)
        self.__books_tab.grid_columnconfigure(0, weight=1)
        self.__books_tab.grid_rowconfigure(1, weight=1)
        self.__mutate_Text_GUI(self.__books_list_text, "Nothing to Display Please Load a Shows file.")
        self.__mutate_Text_GUI(self.__books_stats_text,
                               "Oops There are no numbers to Crunch Here!\nPlease Load a Shows file.")

        # Search Movies/TV Tab
        self.__shows_type_str = tkinter.StringVar()
        self.__shows_title_str = tkinter.StringVar()
        self.__shows_director_str = tkinter.StringVar()
        self.__shows_actor_str = tkinter.StringVar()
        self.__shows_genre_str = tkinter.StringVar()

        self.__search_shows_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__search_shows_tab, text="Search Movies/TV")
        self.__shows_type_label = tkinter.Label(self.__search_shows_tab, text="Type :")
        self.__shows_title_label = tkinter.Label(self.__search_shows_tab, text="Title :")
        self.__shows_director_label = tkinter.Label(self.__search_shows_tab, text="Director :")
        self.__shows_actor_label = tkinter.Label(self.__search_shows_tab, text="Actor :")
        self.__shows_genre_label = tkinter.Label(self.__search_shows_tab, text="Genre :")
        self.__shows_type_combo = ttk.Combobox(self.__search_shows_tab,
                                               textvariable=self.__shows_type_str)
        self.__shows_results_text = tkinter.Text(self.__search_shows_tab)

        self.__shows_type_combo['values'] = ('TV Show', 'Movie')
        self.__shows_title_entry = tkinter.Entry(self.__search_shows_tab, textvariable=self.__shows_title_str, width=40)
        self.__shows_director_entry = tkinter.Entry(self.__search_shows_tab, textvariable=self.__shows_director_str,
                                                    width=40)
        self.__shows_actor_entry = tkinter.Entry(self.__search_shows_tab, textvariable=self.__shows_actor_str, width=40)
        self.__shows_genre_entry = tkinter.Entry(self.__search_shows_tab, textvariable=self.__shows_genre_str, width=40)
        self.__search_show_button = tkinter.Button(self.__search_shows_tab, text="Search", command=self.searchShows)

        self.__shows_scrollbar_y = tkinter.Scrollbar(self.__search_shows_tab, orient=tkinter.VERTICAL,
                                                     command=self.__shows_results_text.yview)
        self.__shows_scrollbar_y.grid(row=6, column=3, sticky=tkinter.NS)
        self.__shows_results_text.config(yscrollcommand=self.__shows_scrollbar_y.set)

        self.__shows_type_label.grid(row=0, column=0, sticky=tkinter.W)
        self.__shows_title_label.grid(row=1, column=0, sticky=tkinter.W)
        self.__shows_director_label.grid(row=2, column=0, sticky=tkinter.W)
        self.__shows_actor_label.grid(row=3, column=0, sticky=tkinter.W)
        self.__shows_genre_label.grid(row=4, column=0, sticky=tkinter.W)
        self.__shows_type_combo.grid(row=0, column=1, sticky=tkinter.W)
        self.__shows_title_entry.grid(row=1, column=1, sticky=tkinter.W)
        self.__shows_director_entry.grid(row=2, column=1, sticky=tkinter.W)
        self.__shows_actor_entry.grid(row=3, column=1, sticky=tkinter.W)
        self.__shows_genre_entry.grid(row=4, column=1, sticky=tkinter.W)
        self.__search_show_button.grid(row=5, column=0, sticky=tkinter.EW)
        self.__shows_results_text.grid(row=6, column=0, columnspan=3, sticky=tkinter.NSEW)

        self.__search_shows_tab.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.__search_shows_tab.grid_columnconfigure(0, weight=1)
        self.__search_shows_tab.grid_columnconfigure(1, weight=50)
        self.__search_shows_tab.grid_rowconfigure(6, weight=50)
        self.__mutate_Text_GUI(self.__shows_results_text, "Please Search Something to Populate Information here.")

        # Search Books
        self.__search_books_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__search_books_tab, text="Search Books")
        self.__books_title_str = tkinter.StringVar()
        self.__books_author_str = tkinter.StringVar()
        self.__books_publisher_str = tkinter.StringVar()

        self.__books_title_label = tkinter.Label(self.__search_books_tab, text="Title :")
        self.__books_author_label = tkinter.Label(self.__search_books_tab, text="Author :")
        self.__books_publisher_label = tkinter.Label(self.__search_books_tab, text="Publisher :")
        self.__books_results_text = tkinter.Text(self.__search_books_tab)

        self.__books_title_entry = tkinter.Entry(self.__search_books_tab, textvariable=self.__books_title_str, width=40)
        self.__books_author_entry = tkinter.Entry(self.__search_books_tab, textvariable=self.__books_author_str,
                                                  width=40)
        self.__books_publisher_entry = tkinter.Entry(self.__search_books_tab, textvariable=self.__books_publisher_str,
                                                     width=40)
        self.__books_search_button = tkinter.Button(self.__search_books_tab, text="Search", command=self.searchBooks)
        self.__books_scrollbar_y = tkinter.Scrollbar(self.__search_books_tab, orient=tkinter.VERTICAL,
                                                     command=self.__books_results_text.yview)
        self.__books_scrollbar_y.grid(row=4, column=3, sticky=tkinter.NS)
        self.__books_results_text.config(yscrollcommand=self.__books_scrollbar_y.set)

        self.__books_title_label.grid(row=0, column=0, sticky=tkinter.W)
        self.__books_author_label.grid(row=1, column=0, sticky=tkinter.W)
        self.__books_publisher_label.grid(row=2, column=0, sticky=tkinter.W)
        self.__books_search_button.grid(row=3, column=0, sticky=tkinter.W)
        self.__books_results_text.grid(row=4, column=0, columnspan=3, sticky=tkinter.NSEW)

        self.__books_title_entry.grid(row=0, column=1, sticky=tkinter.W)
        self.__books_author_entry.grid(row=1, column=1, sticky=tkinter.W)
        self.__books_publisher_entry.grid(row=2, column=1, sticky=tkinter.W)

        self.__search_books_tab.grid_rowconfigure(0, weight=1)
        self.__search_books_tab.grid_columnconfigure(0, weight=1)
        self.__search_books_tab.grid_columnconfigure(1, weight=50)
        self.__search_books_tab.grid_rowconfigure(4, weight=50)
        self.__mutate_Text_GUI(self.__books_results_text, "Please Search Something to Populate Information here.")

        # Recommendations Tab
        self.__recommendations_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__recommendations_tab, text="Recommendations")
        self.__recommendations_title_str = tkinter.StringVar()
        self.__recommendations_type_str = tkinter.StringVar()

        self.__recommendations_type_label = tkinter.Label(self.__recommendations_tab, text="Type :")
        self.__recommendations_title_label = tkinter.Label(self.__recommendations_tab, text="Title :")
        self.__recommendations_get_button = tkinter.Button(self.__recommendations_tab, text="Get Recommendations",
                                                           command=self.getRecommendations)
        self.__recommendations_type_combo = ttk.Combobox(self.__recommendations_tab,
                                                         textvariable=self.__recommendations_type_str)
        self.__recommendations_title_entry = tkinter.Entry(self.__recommendations_tab,
                                                           textvariable=self.__recommendations_title_str, width=40)
        self.__recommendations_results_text = tkinter.Text(self.__recommendations_tab, wrap=tkinter.WORD)
        self.__recommendations_scrollbar_y = tkinter.Scrollbar(self.__recommendations_tab, orient=tkinter.VERTICAL,
                                                               command=self.__recommendations_results_text.yview)
        self.__recommendations_scrollbar_y.grid(row=3, column=2, sticky=tkinter.NS)
        self.__recommendations_results_text.config(yscrollcommand=self.__recommendations_scrollbar_y.set)
        self.__recommendations_type_combo['values'] = ('Movie', 'TV Show', 'Book')
        self.__mutate_Text_GUI(self.__recommendations_results_text, "Please Load the Recommendations.")
        self.__recommendations_type_label.grid(row=0, column=0, sticky=tkinter.W)
        self.__recommendations_title_label.grid(row=1, column=0, sticky=tkinter.W)
        self.__recommendations_get_button.grid(row=2, column=0, columnspan=2, sticky=tkinter.W)
        self.__recommendations_type_combo.grid(row=0, column=1, sticky=tkinter.W)
        self.__recommendations_title_entry.grid(row=1, column=1, sticky=tkinter.W)
        self.__recommendations_results_text.grid(row=3, column=0, columnspan=2, sticky=tkinter.NSEW)

        self.__recommendations_tab.grid_rowconfigure((0, 1, 2), weight=1)
        self.__recommendations_tab.grid_columnconfigure(0, weight=1)
        self.__recommendations_tab.grid_columnconfigure(1, weight=50)
        self.__recommendations_tab.grid_rowconfigure(3, weight=50)

        # Ratings Tab
        self.__ratings_tab = ttk.Frame(self.__notebook)
        self.__notebook.add(self.__ratings_tab, text="Ratings")
        self.__rating_shows_canvas = tkinter.Canvas(self.__ratings_tab, width=600)
        self.__rating_movies_canvas = tkinter.Canvas(self.__ratings_tab, width=600)

        self.__rating_shows_label = tkinter.Label(self.__rating_shows_canvas,
                                                  text="Please Load a Show File to Populate the Shows Pie-Chart")
        self.__rating_movies_label = tkinter.Label(self.__rating_movies_canvas,
                                                   text="Please Load a Show File to Populate the Movie Pie-Chart")

        self.__rating_movies_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.__rating_shows_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.__rating_shows_label.pack(side=tkinter.TOP, fill=tkinter.X)
        self.__rating_movies_label.pack(side=tkinter.TOP, fill=tkinter.X)
        self.__rating_shows_label.configure(font=("Ariel", 20))
        self.__rating_movies_label.configure(font=("Ariel", 20))
        # self.__fig_movie = None
        # self.__fig_tv = None
        # self.__ax_movie = None
        # self.__ax_tv = None

        # Bottom Button Configurations
        self.__load_shows_button = tkinter.Button(self.__button_frame, text='Load Shows', command=self.loadShows)
        self.__load_books_button = tkinter.Button(self.__button_frame, text='Load Books', command=self.loadBooks)
        self.__load_recommendations_button = tkinter.Button(self.__button_frame, text='Load Recommendations',
                                                            command=self.loadAssociations)
        self.__info_button = tkinter.Button(self.__button_frame, text='Info', command=self.creditInfoBox)
        self.__quit_button = tkinter.Button(self.__button_frame, text='Quit',
                                            command=self.__main_window.destroy)

        self.__load_shows_button.grid(row=0, column=0, pady=(0, 15))
        self.__load_books_button.grid(row=0, column=1, pady=(0, 15))
        self.__load_recommendations_button.grid(row=0, column=2, pady=(0, 15))
        self.__info_button.grid(row=0, column=3, pady=(0, 15))
        self.__quit_button.grid(row=0, column=4, pady=(0, 15))
        self.__button_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

    @staticmethod
    def __mutate_Text_GUI(text_GUI: tkinter.Text, text: str):
        """
        Static method used to mutate/change Text GUI elements.
        """
        text_GUI.configure(state=tkinter.NORMAL)
        text_GUI.delete(0.0, tkinter.END)
        text_GUI.insert(tkinter.INSERT, text)
        text_GUI.configure(state=tkinter.DISABLED)

    def loadShows(self):
        """
        Function for loading of show data, updating GUI elements with show lists and statistics,
        and calling the displayPie function
        """
        print("Select a Show file")
        self.__recommender_object.loadShows()
        self.__mutate_Text_GUI(self.__movies_list_text, self.__recommender_object.getMovieList())
        self.__mutate_Text_GUI(self.__tv_shows_list_text, self.__recommender_object.getTVList())
        self.__rating_shows_label['text'] = "Show Ratings"
        self.__rating_movies_label['text'] = "Movie Ratings"

        temp: str = self.__describeRatings(self.__recommender_object.getMovieStats())
        self.__mutate_Text_GUI(self.__movies_stats_text, temp)

        temp: str = self.__describeRatings(self.__recommender_object.getTVStats())
        self.__mutate_Text_GUI(self.__tv_shows_stats_text, temp)
        self.__displayPie()

        print("Shows loaded and GUI updated")

    def loadBooks(self):
        """
        Function for initiating the process of loading book into the application, updating GUI elements with book
        statistics
        """
        print("Select a Book file")
        self.__recommender_object.loadBooks()
        self.__mutate_Text_GUI(self.__books_list_text, self.__recommender_object.getBookList())
        temp: str = self.__describeRatings(self.__recommender_object.getBookStats())
        self.__mutate_Text_GUI(self.__books_stats_text, temp)

    def loadAssociations(self):
        print("Select an Association file")
        """
        Function for initiating the process of loading associations into the application
        """
        self.__recommender_object.loadAssociations()

    def creditInfoBox(self):
        """
        Function for displaying messagebox with project information such as Team name, Team members, and project
        completion date
        """
        title: str = "Project Information"
        message: str = "Team: Code Crusaders\nAnubhav Jaiswal\nPrayash Das"
        project_completion: str = "Project Completion: 05-May-2024"
        self.credit_info_messagebox = messagebox.showinfo(title, message, detail=project_completion)

    def searchShows(self):
        """
        Function to search for TV Shows or Movies based on User Input criteria such as type, title, director, actor, and
        genre. Updates the GUI with the search results
        """
        temp: str = self.__recommender_object.searchTVMovies(self.__shows_type_str.get(), self.__shows_title_str.get(),
                                                             self.__shows_director_str.get(),
                                                             self.__shows_actor_str.get(),
                                                             self.__shows_genre_str.get())
        self.__mutate_Text_GUI(self.__shows_results_text, temp)

    def searchBooks(self):
        """
        Function to search for Books based on User Input Criteria such as book title, book author, and the book
        publisher. Updates the GUI with the search results
        """
        temp: str = self.__recommender_object.searchBooks(self.__books_title_str.get(), self.__books_author_str.get(),
                                                          self.__books_publisher_str.get())
        self.__mutate_Text_GUI(self.__books_results_text, temp)

    def getRecommendations(self):
        """
        Function to fetch recommendations based on user-provided criteria like type and title. Updates the GUI by
        displaying the fetched recommendations in '__recommendations_results_text'
        """
        temp: str = self.__recommender_object.getRecommendations(self.__recommendations_type_str.get(),
                                                                 self.__recommendations_title_str.get())
        self.__mutate_Text_GUI(self.__recommendations_results_text, temp)

    def __displayPie(self):
        """
        Function for creating and displaying pie charts visualising the ratings distribution for movies and
        TV shows in the GUI
        """
        movie_ratings = self.__recommender_object.getMovieStats()['rating_distribution']
        tv_ratings = self.__recommender_object.getTVStats()['rating_distribution']

        fig, ax = plt.subplots(figsize=(6, 6))

        plt.figure(figsize=(6, 6))
        plt.pie(movie_ratings.values(), labels=movie_ratings.keys(), autopct='%1.1f%%', )
        plt.axis('equal')
        plt.savefig('pie_chart_movie.png', transparent=True)

        self.__movie_image = tkinter.PhotoImage(file="pie_chart_movie.png")
        x = (self.__rating_movies_canvas.winfo_width() - self.__movie_image.width())//2
        y = (self.__rating_movies_canvas.winfo_height() - self.__movie_image.height())//2
        self.__rating_movies_canvas.create_image(0, 0, anchor=tkinter.NW, image=self.__movie_image)

        plt.figure(figsize=(6, 6))
        plt.pie(tv_ratings.values(), labels=tv_ratings.keys(), autopct='%1.1f%%')
        plt.axis('equal')
        plt.savefig('pie_chart_tv.png', transparent=True)

        self.__tv_image = tkinter.PhotoImage(file="pie_chart_tv.png")
        x = (self.__rating_shows_canvas.winfo_width() - self.__tv_image.width())//2
        y = (self.__rating_shows_canvas.winfo_height() - self.__tv_image.height())//2
        self.__rating_shows_canvas.create_image(0, 0, anchor=tkinter.NW, image=self.__tv_image)

    @staticmethod
    def __describeRatings(ratings: dict) -> str:
        """
        Function for generating a formatted string with statistics related to ratings, including rating distribution
        and other relevant stats, based on input dictionary
        """
        result = ""  # The string we will build that will populate the respective tv or movie stats tab.
        for (key, value) in ratings.items():
            # Building the Ratings Stats in the String
            if key == "rating_distribution":
                result = "Ratings:\n"
                for (rating, num) in ratings[key].items():
                    result += f"{rating:>8} : {num:0.2f}%\n"
                continue
            # Building the other Stats in the String
            result += f"\n{' '.join([key_word.capitalize() for key_word in key.split('_')]):<25} : {value}\n"
        return result


def main():
    recGUI = RecommenderGUI()
    tkinter.mainloop()
    # abs = "asdf asdf sada"
    # print(" ".join([k.capitalize() for k in abs.split()]))


if __name__ == '__main__':
    main()
