import tkinter as tk  # Graphical User Interface

# Setting up window
root = tk.Tk()
root.geometry()
root.resizable(False, False)

button_values = [
    ["C", "( )", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
]

top_row = ["C", "( )", "%"]
side_row = ["÷", "x", "-", "+", "="]

row_count = len(button_values)
column_count = len(button_values[0])

root.title("Basic Calculator")  # Name of app
frame = tk.Frame(root)
frame.pack()
label = tk.Label(
    frame,
    text="0",
    font=("Garamond", 45),
    background="white",
    foreground="pink",
    anchor="e",
    width=column_count
)
label.grid(row=0, column=0, columnspan=column_count, sticky="nsew")

# Track current expression
expression = ""


def clear_all():
    global expression
    expression = ""
    label["text"] = "0"


def remove_decimal_zero(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    global expression

    if value in top_row:
        if value == "C":
            clear_all()

        elif value == "( )":
            # Alternate between adding "(" and ")"
            if expression.count("(") == expression.count(")"):
                expression += "("
            else:
                expression += ")"
            label["text"] = expression if expression else "0"

        elif value == "%":
            try:
                result = eval(expression.replace("x", "*").replace("÷", "/"))
                result = result / 100
                expression = str(result)
                label["text"] = remove_decimal_zero(result)
            except:
                label["text"] = "Error"
                expression = ""

    elif value in side_row:
        if value == "=":
            try:
                result = eval(expression.replace("x", "*").replace("÷", "/"))
                label["text"] = remove_decimal_zero(result)
                expression = str(result)
            except:
                label["text"] = "Error"
                expression = ""
        else:
            expression += value
            label["text"] = expression

    else:
        if value == "+/-":
            try:
                if expression:
                    result = -1 * float(eval(expression.replace("x", "*").replace("÷", "/")))
                    expression = str(result)
                    label["text"] = remove_decimal_zero(result)
            except:
                label["text"] = "Error"
                expression = ""
        elif value == ".":
            expression += value
            label["text"] = expression
        elif value in "0123456789":
            if label["text"] == "0" and expression == "":
                expression = value
            else:
                expression += value
            label["text"] = expression


for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tk.Button(
            frame,
            text=value,
            font=("Garamond", 45),
            width=column_count - 1,
            height=1,
            command=lambda value=value: button_clicked(value)
        )
        button.grid(row=row + 1, column=column)


root.update()
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root_x = int((screen_width / 2) - (root_width / 2))
root_y = int((screen_height / 2) - (root_height / 2))

root.geometry(f"{root_width}x{root_height}+{root_x}+{root_y}")
root.mainloop()