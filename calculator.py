import tkinter as tk #Graphical User Interface
from tkinter import ttk

#Setting up window
root = tk.Tk()
#Size
root.geometry()
root.resizable(False, False)

button_values = [
    ["C", "( )", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
]

top_row = ["C", "()", "%" ]
side_row = ["÷", "x", "-", "+", "="]

row_count = len(button_values)
column_count = len(button_values[0])

root.title("Basic Calculator") #Name of app
frame = tk.Frame(root)
frame.pack()
label = tk.Label(frame, text="0", font=("Garamond", 45), background="white", foreground="pink",
                 anchor= "e", width=column_count)



label.grid(row=0, column=0,
           columnspan=column_count, sticky="nsew")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tk.Button(frame, text=value,font=("Garamond", 45), width=column_count-1, height=1,
                           command=lambda value=value: button_clicked(value))
        button.grid(row=row+1, column=column)

#operations allowed: number1+number2, number1-number2, number1*number2, number1/number2

number1 = "0"
operator = None
number2 = None

def clear_all():
    global operator, number1, number2
    number1 = "0"
    operator = None
    number2 = None

def remove_decimal_zero(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global top_row, side_row, label, operator, number1, number2

    if value in top_row:
        if value == "C":
            clear_all()
            label["text"] = "0"

        elif value == "( )":
            pass

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_decimal_zero(result)

    elif value in side_row:
        if value == "=":
            if number1 is not None and operator is not None:
                number2 = label["text"].split(operator)[-1].strip()
                numnumber1 = float(number1)
                numnumber2 = float(number2)

                if operator == "÷":
                    label["text"] = remove_decimal_zero(numnumber1 / numnumber2)
                elif operator == "x":
                    label["text"] = remove_decimal_zero(numnumber1 * numnumber2)
                elif operator == "+":
                    label["text"] = remove_decimal_zero(numnumber1 + numnumber2)
                elif operator == "-":
                    label["text"] = remove_decimal_zero(numnumber1 - numnumber2)

                clear_all()

        elif value in "÷x-+":
            if operator is None:
                number1 = label["text"]
                operator = value
                number2 = label["text"]
                label["text"] =number1 + " " + operator + " "



    else:
        if value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_decimal_zero(result)
        elif value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value

root.update()
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root_x = int((screen_width / 2) - (root_width / 2))
root_y = int((screen_height / 2) - (root_height / 2))

root.geometry(f"{root_width}x{root_height}+{root_x}+{root_y}")














root.mainloop()







