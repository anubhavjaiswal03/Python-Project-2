import tkinter
from tkinter import ttk
from tkinter import messagebox
from Recommender import Recommender
class RecommenderGUI(Recommender):
    def __init__(self):
        self._recommender=Recommender()
        self.main_window=tkinter.Toplevel()
        self.main_window.title('Hello!')
        self.main_window.geometry('1200x800')
        self.notebook=ttk.Notebook(self.main_window)

        self.button1=tkinter.Button(text='Click',command=loadShows)
        self.button2=tkinter.Button(text='Books',command=loadBooks)
        self.button3=tkinter.Button(text='Associations',command=loadAssociations)

        self.Quit=tkinter.Button(text='Quit',command=self.main_window.destroy)

        def creditInfoBox(self):
            self.message='Code Crusaders\n'

            self.message=self.message+'Anubhav Jaiswal\n'
            self.message=self.message+'Prayash Das\n'
            self.message=self.message+f'\nProject Completed: {messagebox.showinfo('Project Completion Date','When was it completed?').strip()}'
            messagebox.showinfo('Team Information',self.message)








    tkinter.mainloop()


