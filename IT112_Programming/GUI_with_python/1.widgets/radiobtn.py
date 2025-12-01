import tkinter as tk 
from tkinter import *

root = tk.Tk()
root.title("Radio Button")
root.minsize(300,200)

# tk.Radiobutton(root, text ="Metabrains", value = 1).pack()

for text, value in [("Apple", 1),("Banana",2), ("Grape",3)]:
    tk.Radiobutton(root, text=text, value=value, indicator = 0).pack()

radio = IntVar()
rbtn1 =tk.Radiobutton(root, text="red",variable=radio,value="1")
rbtn1.pack()
rbtn2 = tk.Radiobutton(root, text="Green",variable=radio,value="2")
rbtn2.pack()
rbtn3 = tk.Radiobutton(root, text="Blue",variable=radio,value="3")
rbtn3.pack()

root.mainloop()