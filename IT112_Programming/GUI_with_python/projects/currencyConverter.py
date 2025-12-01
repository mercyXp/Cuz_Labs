from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('curency converter')
root.geometry('400x400')

tframe = Frame(root, width=400, height=100,bg='navyblue') # Create a frame
tframe.pack(fill='x')

# Add a label inside the frame
title_label = tk.Label(tframe, text="Currency Converter", fg="white", bg="navyblue", font=('Lexend', 18, 'bold'))
title_label.place(relx=0.5, rely=0.5, anchor='center')  # Center the text

lframe = Frame(root, width=400, height=300, bg = 'lightgray')
lframe.pack(fill='both', expand=True)

flabel1 = tk.Label(lframe, text="FROM:", bg ='lightgray', font=('Lexend', 10))
flabel1.pack()
flabel1.grid(row=0, column=0, padx=10, pady=10)



root.mainloop()