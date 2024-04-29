import tkinter
from tkinter import ttk
from Recommender import Recommender
class RecommenderGUI(Recommender):
    def __init__(self):
        self._recommender=Recommender()
        self.main_window=tkinter.Toplevel()
        self.main_window.title('Hello!')
        self.main_window.geometry('1200x800')
        #self.movie_notebook=ttk.Notebook(self.main_window)
        #self.tvshow_titles=ttk.Notebook(self.main_window)
        #self.booktitle_author=ttk.Notebook(self.main_window)






    tkinter.mainloop()


