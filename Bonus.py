'''import tkinter
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Recommender import Recommender

file_paths=["Input Files/books100.csv",
                  "Input Files/shows100.csv",
                  "Input Files/associated10.csv"]
rec=Recommender(file_paths)

main_window=tkinter.Tk()
main_window.geometry('1200x1000')
main_window.title("Ratings Analysis")


notebook = ttk.Notebook(main_window)
notebook.pack(fill=tkinter.BOTH, expand=True)


ratings_tab = ttk.Frame(notebook)
notebook.add(ratings_tab, text="Ratings")

movie_canvas = tkinter.Canvas(ratings_tab, width=400, height=300)
movie_canvas.pack(side=tkinter.LEFT, padx=10, pady=10)


tv_canvas = tkinter.Canvas(ratings_tab, width=400, height=300)
tv_canvas.pack(side=tkinter.LEFT, padx=10, pady=10)


rec.loadBooks()
rec.loadShows()


movie_stats = rec.getMovieStats()
tv_stats = rec.getTVStats()


movie_rating_distribution = movie_stats.get('rating_distribution', {})
tv_rating_distribution = tv_stats.get('rating_distribution', {})



movie_rating_distribution=movie_stats.get('rating_distribution',{})
tv_rating_distribution=tv_stats.get('rating_distribution',{})


if isinstance(movie_rating_distribution,str):
    movie_rating_distribution={
        item.split(':')[0].strip(): float(item.split(':')[1].replace('%','').strip())
        for item in movie_rating_distribution.split(', ')
    }
if isinstance(tv_rating_distribution,str):
    tv_rating_distribution={
        item.split(':')[0].strip(): float(item.split(':')[1].replace('%', '').strip())
        for item in tv_rating_distribution.split(', ')
    }



def show_pie(data,title,ax):
    ax.pie(data.values(),labels=data.keys(),autopct='%1.2f%%',startangle=90,wedgeprops={'linewidth':1,'edgecolor':'black'},textprops={'fontsize':8})
    ax.axis('equal')
    ax.set_title(title)


def create_pie_chart(data, title, ax):
    ax.pie(data.values(), labels=data.keys(), autopct='%1.2f%%', startangle=90,wedgeprops={'linewidth':1,'edgecolor': 'black'},textprops={'fontsize':8})
    ax.axis('equal')
    ax.set_title(title)


create_pie_chart(movie_rating_distribution, 'Movie Ratings', ax_movie)
create_pie_chart(tv_rating_distribution, 'TV Show Ratings', ax_tv)


movie_chart = FigureCanvasTkAgg(fig_movie, master=movie_canvas)
movie_chart.get_tk_widget().pack()


tv_chart = FigureCanvasTkAgg(fig_tv, master=tv_canvas)
tv_chart.get_tk_widget().pack()


main_window.mainloop()'''

import matplotlib.pyplot as plt

# Sample dictionary with rating categories and their distribution values
rating_distribution = {'R': 4.0, 'ALL': 12.0, '18+': 18.0, '7+': 2.0, '13+': 28.0, '16+': 22.0, 'None': 4.0, 'NR': 6.0, 'PG-13': 2.0, 'G': 2.0}

# Extract labels and values from the dictionary
labels = list(rating_distribution.keys())
values = list(rating_distribution.values())

# Create the pie chart
plt.figure(figsize=(5, 5))  # Adjust figure size as needed
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)  # Display percentages with one decimal place
plt.axis('equal')  # Ensure a circular shape

# Customize the chart (optional)
plt.title('Movie Rating Distribution')  # Add a title
plt.legend(loc='best')  # Add a legend

# Display the chart
plt.show()

