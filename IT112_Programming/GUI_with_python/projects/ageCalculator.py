import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Age Calculator")

root.geometry("700x400")

ageCalcLabel = tk.Label(root, text="AGE CALCULATOR", font = ('Comic Sans MS', 16, 'bold'))
ageCalcLabel.pack(pady=10)

ageCalcLabel = tk.Label(root, text="Enter your year of birth", font = ('Comic Sans MS', 12))
ageCalcLabel.pack(pady=10)

inputText = Entry(root, width = 30)
inputText.place(x=250, y=100)

resultLabel = tk.Label(root, text="", font=('Lexend', 12))
resultLabel.place(x=250, y=200)

def calculateAge():
    try:
        birthYear = int(inputText.get())
        currentYear = 2025
        age = currentYear - birthYear
        resultLabel.config(text=f"You are : {age} years")
    except ValueError:
        resultLabel.config(text="Please enter a valid year")

calcButton = Button(root, text="Calculate Age", bg = "green", fg = "white", command=calculateAge)
calcButton.place(x=300, y=150)

root.mainloop()