import tkinter as tk
from tkinter import * # for side

top = tk.Tk()

top.title("pack-method")

top.geometry("400x300")

btn = Button(top, text="Login")

btn.pack(side = RIGHT)

top.mainloop()