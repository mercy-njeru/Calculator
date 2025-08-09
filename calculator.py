import tkinter as tk #Graphical User Interface
from tkinter import ttk


#Setting up window
root = tk.Tk()
#Size
root.geometry("400x500")
root.resizable(False, False)

#Name of top
#root.title("Mercy Calculator!")
label = tk.Label(root, text="Mercy Calculator!", font=("Garamond", 24))
label.pack(padx=50, pady=5 )

textbox = tk.Text(root, height=3, width=200, font=("Garamond", 16) )
textbox.pack()
grid = tk.Tk

root.mainloop()






