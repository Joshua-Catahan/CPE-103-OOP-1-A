import tkinter as tk
import math

# Functions for calculation
def validate_input(entry):
    try:
        float(entry.get())
        return True
    except ValueError:
        result.set("Error! Invalid input.")
        return False

def add():
    if validate_input(entry1) and validate_input(entry2):
        value = float(entry1.get()) + float(entry2.get())
        result.set(value)
        update_history(f"{entry1.get()} + {entry2.get()} = {value}")

def subtract():
    if validate_input(entry1) and validate_input(entry2):
        value = float(entry1.get()) - float(entry2.get())
        result.set(value)
        update_history(f"{entry1.get()} - {entry2.get()} = {value}")

def multiply():
    if validate_input(entry1) and validate_input(entry2):
        value = float(entry1.get()) * float(entry2.get())
        result.set(value)
        update_history(f"{entry1.get()} * {entry2.get()} = {value}")

def divide():
    if validate_input(entry1) and validate_input(entry2):
        try:
            value = float(entry1.get()) / float(entry2.get())
            result.set(value)
            update_history(f"{entry1.get()} / {entry2.get()} = {value}")
        except ZeroDivisionError:
            result.set("Error! Division by zero.")
            update_history(f"{entry1.get()} / {entry2.get()} = Error (division by zero)")

def square_root():
    if validate_input(entry1):
        value = math.sqrt(float(entry1.get()))
        result.set(value)
        update_history(f"√{entry1.get()} = {value}")

def power():
    if validate_input(entry1) and validate_input(entry2):
        value = float(entry1.get()) ** float(entry2.get())
        result.set(value)
        update_history(f"{entry1.get()} ^ {entry2.get()} = {value}")

def sin_function():
    if validate_input(entry1):
        value = math.sin(math.radians(float(entry1.get())))
        result.set(value)
        update_history(f"sin({entry1.get()}) = {value}")

def cos_function():
    if validate_input(entry1):
        value = math.cos(math.radians(float(entry1.get())))
        result.set(value)
        update_history(f"cos({entry1.get()}) = {value}")

def tan_function():
    if validate_input(entry1):
        value = math.tan(math.radians(float(entry1.get())))
        result.set(value)
        update_history(f"tan({entry1.get()}) = {value}")

def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    result.set("")

def update_history(operation):
    history_text.insert(tk.END, operation + "\n")

def clear_history():
    history_text.delete('1.0', 'end')

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#D9DF82")

# Create StringVar to hold the result
result = tk.StringVar()

# Create the layout
tk.Label(root, text="Enter 1st number:",  bg='#D9DF82').grid(row=0, column=0)
entry1 = tk.Entry(root, bg="#EFEFD8")
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter 2nd number (if needed):",  bg='#D9DF82').grid(row=1, column=0)
entry2 = tk.Entry(root, bg="#EFEFD8")
entry2.grid(row=1, column=1)

# Buttons for basic operations
tk.Button(root, text="+", command=add, bg='#BABD8C').grid(row=2, column=0)
tk.Button(root, text="-", command=subtract, bg='#BABD8C').grid(row=2, column=1)
tk.Button(root, text="x", command=multiply, bg='#BABD8C').grid(row=3, column=0)
tk.Button(root, text="/", command=divide, bg='#BABD8C').grid(row=3, column=1)

# Buttons for additional operations
tk.Button(root, text="√", command=square_root, bg='#BABD8C').grid(row=4, column=0)
tk.Button(root, text="1st^(2nd)", command=power, bg='#BABD8C').grid(row=4, column=1)
tk.Button(root, text="sin(1st)", command=sin_function, bg='#BABD8C').grid(row=5, column=0)
tk.Button(root, text="cos(1st)", command=cos_function, bg='#BABD8C').grid(row=5, column=1)
tk.Button(root, text="tan(1st)", command=tan_function, bg='#BABD8C').grid(row=6, column=1)

# Clear button
tk.Button(root, text="Clear", command=clear, bg='#BABD8C').grid(row=6, column=0)
tk.Button(root, text="Clear History", command=clear_history, bg='#BABD8C').grid(row=16, column=0, columnspan=3)

# Label to show result
tk.Label(root, text="Result:", bg='#D9DF82').grid(row=8, column=0)
result_label = tk.Label(root, textvariable=result, bg='#D9DF82')
result_label.grid(row=8, column=1)

# Text widget for history
tk.Label(root, text="Calculation History:", bg="#D9DF82").grid(row=9, column=0, columnspan=3)
history_text = tk.Text(root, height=10, width=40, bg="#EFEFD8")
history_text.grid(row=10, column=0, columnspan=3)

# Start the main loop
root.mainloop()
