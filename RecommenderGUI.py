import tkinter
from tkinter import ttk
from Recommender import Recommender
import tkinter.messagebox as messagebox


class RecommenderGUI:
    def __init__(self, default_file_names=None):  # DELETE THE default_file_names parameter before submitting
        # self._recommend = Recommender(default_file_names)
        self._main_window = tkinter.Tk()
        self._main_window.title('Media Recommender')
        self._main_window.geometry('1200x800')

        tkinter.mainloop()

    def loadShows(self):
        pass

    def loadBooks(self):
        pass

    def creditInfoBox(self):
        pass


if __name__ == '__main__':
    file_paths = ["Input Files/books10.csv",
                  "Input Files/shows10.csv",
                  "Input Files/associated10.csv"]

    recGUI = RecommenderGUI(file_paths)
