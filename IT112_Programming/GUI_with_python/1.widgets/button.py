import tkinter as tk

root = tk.Tk()
root.title("The Button widget")

btn = tk.Button(root, text="Click Me!", relief = "raised", state="disabled").pack()
btn = tk.Button(root, text="Click Me!", relief = "sunken").pack()
btn = tk.Button(root, text="Click Me!", relief = "flat").pack()
btn = tk.Button(root, text="Click Me!", relief = "ridge").pack()
btn = tk.Button(root, text="Click Me!", relief = "groove").pack()
btn = tk.Button(root, text="Click Me!", relief = "solid").pack()

root.mainloop()