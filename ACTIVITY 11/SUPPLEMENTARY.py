import tkinter as tk
import math

def number1(event=0):
    entry.insert(tk.END, "1")
def number2(event=0):
    entry.insert(tk.END, "2")
def number3(event=0):
    entry.insert(tk.END, "3")
def number4(event=0):
    entry.insert(tk.END, "4")
def number5(event=0):
    entry.insert(tk.END, "5")
def number6(event=0):
    entry.insert(tk.END, "6")
def number7(event=0):
    entry.insert(tk.END, "7")
def number8(event=0):
    entry.insert(tk.END, "8")
def number9(event=0):
    entry.insert(tk.END, "9")
def number0(event=0):
    entry.insert(tk.END, "0")
def point(event=0):
    entry.insert(tk.END, ".")
def addition(event=0):
    entry.insert(tk.END, "+")
def subtraction(event=0):
    entry.insert(tk.END, "-")
def multiplication():
    entry.insert(tk.END, "*")
def division(event=0):
    entry.insert(tk.END, "/")
def clear(event=0):
    entry.delete(0, tk.END)
def delete(event=0):
    current_entry = entry.get()
    if len(current_entry) > 0:
        entry.delete(len(current_entry) - 1, tk.END)
def equal(event=0):
     result = eval(entry.get())
     entry.delete(0, tk.END)
     entry.insert(tk.END, str(result))
# SUPPLEMENTARY ACTIVITY
def sin():
    result = math.sin(math.radians(float(entry.get())))
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
def cos():
    result = math.cos(math.radians(float(entry.get())))
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
def tan():
    result = math.tan(math.radians(float(entry.get())))
    entry.delete(0, tk.END)
    entry.insert(0, str(result))
def power(event=0):
    entry.insert(tk.END, "**")
def open_parenthesis(event=0):
    entry.insert(tk.END, "(")
def close_parenthesis(event=0):
    entry.insert(tk.END, ")")

# Create main window
window = tk.Tk()
window.title("Advanced Calculator Interface")
window.resizable(False, False)
# Entry field
entry = tk.Entry(window, width=20, borderwidth=10, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Row 1
tk.Button(window, text="sin(n)", width=10, height=3, bd=4,command=sin).grid(row=2, column=0, sticky="we")
tk.Button(window, text="cos(n)", width=10, height=3, bd=4,command=cos).grid(row=2, column=1, sticky="we")
tk.Button(window, text="tan(n)", width=10, height=3, bd=4,command=tan).grid(row=2, column=2, sticky="we")
tk.Button(window, text="x^(n)", width=10, height=3, bd=4,command=power).grid(row=2, column=3, sticky="we")

# Row 2
tk.Button(window, text="7", width=10, height=3, bd=4,command=number7).grid(row=3, column=0, sticky="we")
tk.Button(window, text="8", width=10, height=3, bd=4,command=number8).grid(row=3, column=1, sticky="we")
tk.Button(window, text="9", width=10, height=3, bd=4,command=number9).grid(row=3, column=2, sticky="we")
tk.Button(window, text="/", width=10, height=3, bd=4,command=division).grid(row=3, column=3, sticky="we")

# Row 3
tk.Button(window, text="4", width=10, height=3, bd=4,command=number4).grid(row=4, column=0, sticky="we")
tk.Button(window, text="5", width=10, height=3, bd=4,command=number5).grid(row=4, column=1, sticky="we")
tk.Button(window, text="6", width=10, height=3, bd=4,command=number6).grid(row=4, column=2, sticky="we")
tk.Button(window, text="*", width=10, height=3, bd=4,command=multiplication).grid(row=4, column=3, sticky="we")

# Row 4
tk.Button(window, text="1", width=10, height=3, bd=4,command=number1).grid(row=5, column=0, sticky="we")
tk.Button(window, text="2", width=10, height=3, bd=4,command=number2).grid(row=5, column=1, sticky="we")
tk.Button(window, text="3", width=10, height=3, bd=4,command=number3).grid(row=5, column=2, sticky="we")
tk.Button(window, text="-", width=10, height=3, bd=4,command=subtraction).grid(row=5, column=3, sticky="we")

# Row 5
tk.Button(window, text="0", width=10, height=3, bd=4,command=number0).grid(row=6, column=0, sticky="we")
tk.Button(window, text=".", width=10, height=3, bd=4,command=point).grid(row=6, column=1, sticky="we")
tk.Button(window, text="+", width=10, height=3, bd=4,command=addition).grid(row=6, column=2, sticky="we")
tk.Button(window, text="Del", width=10, height=3, bd=4,command=delete).grid(row=6, column=3, sticky="we")

# Row 6
tk.Button(window, text="=", width=10, height=3, bd=4,command=equal).grid(row=7, column=3, sticky="we")
tk.Button(window, text="C", width=10, height=3, bd=4,command=clear).grid(row=7, column=2, sticky="we")
tk.Button(window, text=")", width=10, height=3, bd=4,command=close_parenthesis).grid(row=7, column=1, sticky="we")
tk.Button(window, text="(", width=10, height=3, bd=4,command=open_parenthesis).grid(row=7, column=0, sticky="we")

# Bind keys
window.bind("1", number1)
window.bind("2", number2)
window.bind("3", number3)
window.bind("4", number4)
window.bind("5", number5)
window.bind("6", number6)
window.bind("7", number7)
window.bind("8", number8)
window.bind("9", number9)
window.bind("0", number0)
window.bind(".", point)
window.bind("+", addition)
window.bind("-", subtraction)
window.bind("*", multiplication)
window.bind("/", division)
window.bind("(", open_parenthesis)
window.bind(")", close_parenthesis)
window.bind("^", power)
window.bind("<Return>", equal)  # Enter key for equal
window.bind("<BackSpace>", delete)  # Backspace key for delete
window.bind("<Delete>", clear)  # Delete key for clear

# Run the application
window.mainloop()
