import tkinter as tk

def number1():
    entry.insert(tk.END, "1")
def number2():
    entry.insert(tk.END, "2")
def number3():
    entry.insert(tk.END, "3")
def number4():
    entry.insert(tk.END, "4")
def number5():
    entry.insert(tk.END, "5")
def number6():
    entry.insert(tk.END, "6")
def number7():
    entry.insert(tk.END, "7")
def number8():
    entry.insert(tk.END, "8")
def number9():
    entry.insert(tk.END, "9")
def number0():
    entry.insert(tk.END, "0")
def point():
    entry.insert(tk.END, ".")
def addition():
    entry.insert(tk.END, "+")
def subtraction():
    entry.insert(tk.END, "-")
def multiplication():
    entry.insert(tk.END, "*")
def division():
    entry.insert(tk.END, "/")

def clear():
    entry.delete(0, tk.END)

def delete():
    current_text = entry.get()
    if len(current_text) > 0:
        entry.delete(len(current_text) - 1, tk.END)

def equal():
     result = eval(entry.get())
     entry.delete(0, tk.END)
     entry.insert(tk.END, str(result))



# Create main window
window = tk.Tk()
window.title("Simple Calculator Interface")

# Entry field
entry = tk.Entry(window, width=20, borderwidth=10, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Row 1
tk.Button(window, text="7", width=10, height=3, bd=4,command=number7).grid(row=2, column=0, sticky="we")
tk.Button(window, text="8", width=10, height=3, bd=4,command=number8).grid(row=2, column=1, sticky="we")
tk.Button(window, text="9", width=10, height=3, bd=4,command=number9).grid(row=2, column=2, sticky="we")
tk.Button(window, text="/", width=10, height=3, bd=4,command=division).grid(row=2, column=3, sticky="we")

# Row 2
tk.Button(window, text="4", width=10, height=3, bd=4,command=number4).grid(row=3, column=0, sticky="we")
tk.Button(window, text="5", width=10, height=3, bd=4,command=number5).grid(row=3, column=1, sticky="we")
tk.Button(window, text="6", width=10, height=3, bd=4,command=number6).grid(row=3, column=2, sticky="we")
tk.Button(window, text="*", width=10, height=3, bd=4,command=multiplication).grid(row=3, column=3, sticky="we")

# Row 3
tk.Button(window, text="1", width=10, height=3, bd=4,command=number1).grid(row=4, column=0, sticky="we")
tk.Button(window, text="2", width=10, height=3, bd=4,command=number2).grid(row=4, column=1, sticky="we")
tk.Button(window, text="3", width=10, height=3, bd=4,command=number3).grid(row=4, column=2, sticky="we")
tk.Button(window, text="-", width=10, height=3, bd=4,command=subtraction).grid(row=4, column=3, sticky="we")

# Row 4
tk.Button(window, text="0", width=10, height=3, bd=4,command=number0).grid(row=5, column=0, sticky="we")
tk.Button(window, text=".", width=10, height=3, bd=4,command=point).grid(row=5, column=1, sticky="we")
tk.Button(window, text="+", width=10, height=3, bd=4,command=addition).grid(row=5, column=2, sticky="we")
tk.Button(window, text="Del", width=10, height=3, bd=4,command=delete).grid(row=5, column=3, sticky="we")

# Row 5
tk.Button(window, text="=", width=32, height=3, bd=4,command=equal).grid(row=6, column=0, columnspan=3, sticky="we")
tk.Button(window, text="C", width=10, height=3, bd=4,command=clear).grid(row=6, column=3, sticky="we")

# Run the application
window.mainloop()
