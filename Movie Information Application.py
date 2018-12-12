# Importing the tkinter library with alias tk.
from tkinter import *
from requests import *
from PIL import ImageTk, Image


# A function which downloads a given URL.
def download_image(url):
    response = get(url)
    if response.status_code == 200:
        with open("images/temp.jpg", 'wb') as f:
            f.write(response.content)


# A function which contains all the tkinter gui items and their positioning.
def create_gui():
    # The frame used to contain the search toolbar
    search_frame = Frame(root, bg="blue")
    search_frame.pack(side="top", fill=X)

    searchbar_entry = Entry(search_frame)
    searchbar_entry.pack(side="left")

    search_button = Button(search_frame, text="Search!")
    search_button.pack(side="left")

    # The frame used to contain all movie info
    info_frame = Frame(root, bg="green")
    info_frame.pack(side="left", fill=Y)

    title_label = Label(info_frame, text="Title:")
    title_label.grid(row=1, column=0)

    title_output = Entry(info_frame)
    title_output.grid(row=1, column=2)

    year_label = Label(info_frame, text="Year:")
    year_label.grid(row=2, column=0)

    year_output = Entry(info_frame)
    year_output.grid(row=2, column=2)

    rating_label = Label(info_frame, text="Rating:")
    rating_label.grid(row=3, column=0)

    rating_output = Entry(info_frame)
    rating_output.grid(row=3, column=2)

    release_label = Label(info_frame, text="Release:")
    release_label.grid(row=4, column=0)

    release_output = Entry(info_frame)
    release_output.grid(row=4, column=2)

    release_label = Label(info_frame, text="Release:")
    release_label.grid(row=4, column=0)

    release_output = Entry(info_frame)
    release_output.grid(row=4, column=2)

    runtime_label = Label(info_frame, text="Runtime:")
    runtime_label.grid(row=5, column=0)

    runtime_output = Entry(info_frame)
    runtime_output.grid(row=5, column=2)

    genre_label = Label(info_frame, text="Genre:")
    genre_label.grid(row=6, column=0)

    genre_output = Entry(info_frame)
    genre_output.grid(row=6, column=2)

    director_label = Label(info_frame, text="Director:")
    director_label.grid(row=7, column=0)

    director_output = Entry(info_frame)
    director_output.grid(row=7, column=2)

    writers_label = Label(info_frame, text="Writers:")
    writers_label.grid(row=8, column=0)

    writers_output = Entry(info_frame)
    writers_output.grid(row=8, column=2)

    actors_label = Label(info_frame, text="Actors:")
    actors_label.grid(row=9, column=0)

    actors_output = Entry(info_frame)
    actors_output.grid(row=10, column=2)

    plot_label = Label(info_frame, text="Plot:")
    plot_label.grid(row=10, column=0)

    plot_output = Entry(info_frame)
    plot_output.grid(row=10, column=2)

    language_label = Label(info_frame, text="Language:")
    language_label.grid(row=11, column=0)

    language_output = Entry(info_frame)
    language_output.grid(row=11, column=2)

    country_label = Label(info_frame, text="Country:")
    country_label.grid(row=12, column=0)

    country_output = Entry(info_frame)
    country_output.grid(row=12, column=2)

    awards_label = Label(info_frame, text="Awards:")
    awards_label.grid(row=13, column=0)

    awards_output = Entry(info_frame)
    awards_output.grid(row=13, column=2)

    # The Frame used to contain the film poster
    poster_frame = Frame(root, bg="red")
    poster_frame.pack(side="left", fill=Y)

    u = "https://m.media-amazon.com/images/M/MV5BMTQ4MzkzNjcxNV5BMl5BanBnXkFtZTcwNzk4NTU0Mg@@._V1_SX300.jpg"

    download_image(u)

    poster_image = ImageTk.PhotoImage(Image.open("images/temp.jpg"))

    poster_label = Label(poster_frame, image=poster_image)
    poster_label.pack()

    # The Frame used to contain the wish-list
    wishlist_frame = Frame(root, bg="cyan")
    wishlist_frame.pack(side="right", fill=Y)

    wishlist_label = Label(wishlist_frame, text="WISH-LIST AREA")
    wishlist_label.pack()


root = Tk()

create_gui()

root.mainloop()
