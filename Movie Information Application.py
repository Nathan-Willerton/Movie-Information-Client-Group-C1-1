import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        master.title("Movie Information Application")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
