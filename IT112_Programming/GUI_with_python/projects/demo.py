import tkinter as tk

root = tk.Tk()
root.geometry("400x200")
root.title("Dropdown Example")

# Variable to hold selected value
selected_currency = tk.StringVar()
selected_currency.set("USD")  # Default value

# Options
options = ["USD", "EUR", "GBP", "JPY"]

# Create OptionMenu
dropdown = tk.OptionMenu(root, selected_currency, *options)
dropdown.pack(pady=20)

# Function to show selected value
def show_selection():
    print("Selected:", selected_currency.get())

button = tk.Button(root, text="Check Selection", command=show_selection)
button.pack()

root.mainloop()
