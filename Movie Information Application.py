# Importing all required libraries
from tkinter import *
from tkinter import messagebox
from requests import *
from PIL import ImageTk, Image

# Use pip install requests & pip install pillow if needed.

root = Tk()

#
returned_title = StringVar()
returned_year = StringVar()
returned_rated = StringVar()
returned_released = StringVar()
returned_runtime = StringVar()
returned_genre = StringVar()
returned_director = StringVar()
returned_writer = StringVar()
returned_actors = StringVar()
returned_plot = StringVar()
returned_language = StringVar()
returned_country = StringVar()
returned_awards = StringVar()

poster_image = ImageTk.PhotoImage(Image.open("images/empty.jpg"))


# A function used to query the omdb database using the provided API key.
def query_omdb(search_string):
    query_json = get("http://www.omdbapi.com/?t=" + search_string + "&apikey=b2f11028").json()
    return query_json


# A function which downloads a given URL.
def download_image(url):
    data = get(url)
    if data.status_code == 200:
        with open("images/temp.jpg", 'wb') as f:
            f.write(data.content)


# A function which takes the input from the searchbar_entry and returns it as a string.
def retrieve_search():
    search_term = searchbar_entry.get()

    input_json = query_omdb(search_term)

    response = input_json['Response']

    # An if statement which checks if the API response is true, if false the API could not find a match.
    if response == "True":

        returned_title.set(input_json['Title'])
        returned_year.set(input_json['Year'])
        returned_rated.set(input_json['Rated'])
        returned_released.set(input_json['Released'])
        returned_runtime.set(input_json['Runtime'])
        returned_genre.set(input_json['Genre'])
        returned_director.set(input_json['Director'])
        returned_writer.set(input_json['Writer'])
        returned_actors.set(input_json['Actors'])
        returned_plot.set(input_json['Plot'])
        returned_language.set(input_json['Language'])
        returned_country.set(input_json['Country'])
        returned_awards.set(input_json['Awards'])
        returned_poster = input_json['Poster']

        # Download the new poster from the URL supplied in the JSON.
        download_image(returned_poster)
        new_poster = ImageTk.PhotoImage(Image.open("images/temp.jpg"))
        poster_label.configure(image=new_poster)
        poster_label.PhotoImage = new_poster

    else:
        messagebox.showinfo("Sorry!", "We couldn't find a movie by that name!")


def save_item():
    search_term = searchbar_entry.get()

    input_json = query_omdb(search_term)

    list_item = input_json['Title']

    wishlist_box.insert(1, list_item)


# The frame used to contain the search toolbar
search_frame = Frame(root)
search_frame.pack(side="top", fill=X)

searchbar_entry = Entry(search_frame)
searchbar_entry.pack(side="left")

# A button which when clicked calls the retrieve_search function.
search_button = Button(search_frame, text="Search!", command=retrieve_search)
search_button.pack(side="left")

# A button which when clicked calls the retrieve_search function.
save_button = Button(search_frame, text="Save!", command=save_item)
save_button.pack(side="left")

# The frame used to contain all movie info
info_frame = Frame(root)
info_frame.pack(side="left", fill=Y)

title_label = Label(info_frame, text="Title:")
title_label.grid(row=1, column=0)

title_output = Label(info_frame, textvariable=returned_title)
title_output.grid(row=1, column=2)

year_label = Label(info_frame, text="Year:")
year_label.grid(row=2, column=0)

year_output = Label(info_frame, textvariable=returned_year)
year_output.grid(row=2, column=2)

rated_label = Label(info_frame, text="Rating:")
rated_label.grid(row=3, column=0)

rated_output = Label(info_frame, textvariable=returned_rated)
rated_output.grid(row=3, column=2)

released_label = Label(info_frame, text="Release:")
released_label.grid(row=4, column=0)

released_output = Label(info_frame, textvariable=returned_released)
released_output.grid(row=4, column=2)

runtime_label = Label(info_frame, text="Runtime:")
runtime_label.grid(row=5, column=0)

runtime_output = Label(info_frame, textvariable=returned_runtime)
runtime_output.grid(row=5, column=2)

genre_label = Label(info_frame, text="Genre:")
genre_label.grid(row=6, column=0)

genre_output = Label(info_frame, textvariable=returned_genre)
genre_output.grid(row=6, column=2)

director_label = Label(info_frame, text="Director:")
director_label.grid(row=7, column=0)

director_output = Label(info_frame, textvariable=returned_director)
director_output.grid(row=7, column=2)

writer_label = Label(info_frame, text="Writer:")
writer_label.grid(row=8, column=0)

writer_output = Label(info_frame, textvariable=returned_writer)
writer_output.grid(row=8, column=2)

actors_label = Label(info_frame, text="Actors:")
actors_label.grid(row=9, column=0)

actors_output = Label(info_frame, textvariable=returned_actors)
actors_output.grid(row=9, column=2)

plot_label = Label(info_frame, text="Plot:")
plot_label.grid(row=10, column=0)

plot_output = Label(info_frame, textvariable=returned_plot)
plot_output.grid(row=10, column=2)

language_label = Label(info_frame, text="Language:")
language_label.grid(row=11, column=0)

language_output = Label(info_frame, textvariable=returned_language)
language_output.grid(row=11, column=2)

country_label = Label(info_frame, text="Country:")
country_label.grid(row=12, column=0)

country_output = Label(info_frame,textvariable=returned_country)
country_output.grid(row=12, column=2)

awards_label = Label(info_frame, text="Awards:")
awards_label.grid(row=13, column=0)

awards_output = Label(info_frame, textvariable=returned_awards)
awards_output.grid(row=13, column=2)

# The Frame used to contain the film poster
poster_frame = Frame(root)
poster_frame.pack(side="left", fill=Y)

poster_label = Label(poster_frame, image=poster_image)
poster_label.pack()

# The Frame used to contain the wish-list
wishlist_frame = Frame(root)
wishlist_frame.pack(side="right", fill=Y)

wishlist_label = Label(wishlist_frame, text="Wish-list:")
wishlist_label.pack()

wishlist_box = Listbox(wishlist_frame)
wishlist_box.pack()

root.mainloop()
