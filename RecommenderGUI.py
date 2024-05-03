import tkinter
from tkinter import ttk
from Recommender import Recommender
import tkinter.messagebox as messagebox


class RecommenderGUI:
    def __init__(self):
        self.credit_info_messagebox = None
        self.__recommender = Recommender()
        self.__main_window = tkinter.Tk()
        self.__main_window.title('Media Recommender')
        self.__main_window.geometry('1200x800')
        self.__main_window.minsize(800, 750)
        self.__button_frame = tkinter.Frame(self.__main_window)
        self.__notebook = ttk.Notebook(self.__main_window)
        self.__notebook.pack(expand=1, fill=tkinter.BOTH)
        self.__button_frame.pack(side=tkinter.BOTTOM, fill=tkinter.X)

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

        self.__shows_scrollbar_x = tkinter.Scrollbar(self.__search_shows_tab, orient=tkinter.HORIZONTAL,
                                                     command=self.__shows_results_text.xview)
        self.__shows_scrollbar_x.grid(row=7, column=0, columnspan=3, sticky=tkinter.EW)
        self.__shows_results_text.config(xscrollcommand=self.__shows_scrollbar_x.set)

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
        self.__books_scrollbar_x = tkinter.Scrollbar(self.__search_books_tab, orient=tkinter.HORIZONTAL,
                                                     command=self.__books_results_text.xview)
        self.__books_scrollbar_x.grid(row=5, column=0, columnspan=3, sticky=tkinter.EW)
        self.__books_results_text.config(xscrollcommand=self.__books_scrollbar_x.set)

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
        self.__recommendations_get_button = tkinter.Button(self.__recommendations_tab, text="Get Recommendations")
        self.__recommendations_type_combo = ttk.Combobox(self.__recommendations_tab,
                                                         textvariable=self.__recommendations_type_str)
        self.__recommendations_title_entry = tkinter.Entry(self.__recommendations_tab,
                                                           textvariable=self.__recommendations_title_str, width=40)
        self.__recommendations_results_text = tkinter.Text(self.__recommendations_tab)
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
        self.__rating_shows_canvas = tkinter.Canvas(self.__ratings_tab, )
        self.__rating_movies_canvas = tkinter.Canvas(self.__ratings_tab)

        self.__rating_shows_label = tkinter.Label(self.__rating_shows_canvas,
                                                  text="Please Load a Show File to Populate the Shows Pie-Chart")
        self.__rating_movies_label = tkinter.Label(self.__rating_movies_canvas,
                                                   text="Please Load a Show File to Populate the Movie Pie-Chart")

        self.__rating_movies_canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=(0, 5))
        self.__rating_shows_canvas.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=(5, 0))
        self.__rating_shows_label.pack(side=tkinter.TOP, fill=tkinter.X)
        self.__rating_movies_label.pack(side=tkinter.TOP, fill=tkinter.X)
        self.__rating_shows_label.configure(font=("Ariel", 20))
        self.__rating_movies_label.configure(font=("Ariel", 20))

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
        Static method used to alter Text GUI elements.
        """
        text_GUI.configure(state=tkinter.NORMAL)
        text_GUI.delete(0.0, tkinter.END)
        text_GUI.insert(tkinter.INSERT, text)
        text_GUI.configure(state=tkinter.DISABLED)

    def loadShows(self):  # CHeck Function NAme
        print("Select a Show file")
        self.__recommender.loadShows()
        self.__mutate_Text_GUI(self.__movies_list_text, self.__recommender.getMovieList())
        self.__mutate_Text_GUI(self.__tv_shows_list_text, self.__recommender.getTVList())
        self.__rating_shows_label['text'] = "Show Ratings"
        self.__rating_movies_label['text'] = "Movie Ratings"

    def loadBooks(self):  # CHeck Function NAme
        print("Select a Book file")
        self.__recommender.loadBooks()
        self.__mutate_Text_GUI(self.__books_list_text, self.__recommender.getBookList())

    def loadAssociations(self):
        print("Select an Association file")
        self.__recommender.loadAssociations()
        pass

    def creditInfoBox(self):
        title: str = "Project Information"
        message: str = "Team: Code Crusaders\nAnubhav Jaiswal\nPrayash Das"
        project_completion: str = "Project Completion: 03-May-2024"
        self.credit_info_messagebox = messagebox.showinfo(title, message, detail=project_completion)

    def searchShows(self):
        temp: str = self.__recommender.searchTVMovies(self.__shows_type_str.get(), self.__shows_title_str.get(),
                                                      self.__shows_director_str.get(), self.__shows_actor_str.get(),
                                                      self.__shows_genre_str.get())
        self.sts

    def searchBooks(self):
        pass

    def getRecommendations(self):
        pass


def main():
    recGUI = RecommenderGUI()
    tkinter.mainloop()


if __name__ == '__main__':
    main()
