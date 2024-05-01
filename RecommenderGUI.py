import tkinter
from tkinter import ttk
from Recommender import Recommender
class RecommenderGUI:
    def __init__(self):
        recommend=Recommender()
        self._main_window=tkinter.Toplevel()
        self._main_window.title('Media Recommender')
        self._main_window.geometry('1200x800')

        self._notebook_tab=ttk.Notebook(self._main_window)
        self._movie_tab=tkinter.Frame(self._notebook_tab)
        self._notebook_tab.add(self._movie_tab,text='Movies')
        self._notebook_tab.pack(expand=True,fill='both')

        self._movielist=tkinter.Text(self._movie_tab,wrap=tkinter.WORD)
        self._movielist.configure(state=tkinter.DISABLED)
        self._movielist.pack()

        list=recommend.getMovieList()
        if list:
            self._movielist.configure(state=tkinter.NORMAL)
            self._movielist.insert(tkinter.END,list)
            self._movielist.configure(state=tkinter.DISABLED)
        else:
            self._movielist.insert(tkinter.END,'No movie loaded yet.')

        self._notebook_tab2=ttk.Notebook(self._main_window)
        self._tvshows_tab=tkinter.Frame(self._notebook_tab2)
        self._notebook_tab2.add(self._tvshows_tab,text='TV Shows')
        self._notebook_tab2.pack(expand=True,fill='both')

        self._tvlist=tkinter.Text(self._tvshows_tab,wrap=tkinter.WORD)
        self._tvlist.configure(state=tkinter.DISABLED)
        self._tvlist.pack()

        list2=recommend.getTVList()
        if list2:
            self._tvlist.configure(state=tkinter.NORMAL)
            self._tvlist.insert(tkinter.END,list2)
            self._tvlist.configure(state=tkinter.DISABLED)
        else:
            self._tvlist.insert(tkinter.END,'No TV Shows loaded yet.')



        self._notebook_tab3=ttk.Notebook(self._main_window)
        self._books=tkinter.Frame(self._notebook_tab3)
        self._notebook_tab3.add(self._books,text='Books')
        self._notebook_tab3.pack(expand=True,fill='both')

        self._booklist=tkinter.Text(self._books,wrap=tkinter.WORD)
        self._booklist.configure(state=tkinter.DISABLED)
        self._booklist.pack()

        list3=recommend.getBookList()
        if list3:
            self._booklist.configure(state=tkinter.NORMAL)
            self._booklist.insert(tkinter.END,list3)
            self._booklist.configure(state=tkinter.DISABLED)
        else:
            self._booklist.insert(tkinter.END,'No books loaded yet.')

        self._show_button=tkinter.Button(self._main_window,text='Load Shows',command=recommend.loadShows)
        self._show_button.pack()

        self._book_button=tkinter.Button(self._main_window,text='Load Books',command=recommend.loadShows)
        self._book_button.pack()

        self._association_button=tkinter.Button(self._main_window,text='Load Associations',command=recommend.loadAssociations)




