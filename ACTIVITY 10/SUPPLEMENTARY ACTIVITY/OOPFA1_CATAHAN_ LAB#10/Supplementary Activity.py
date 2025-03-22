import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from time import strftime
from datetime import datetime

window = tk.Tk()
window.title('BIRTHDAY INFORMATION - LAB #10')
window.configure(bg="#36393e")
window.geometry('500x350')
window.iconbitmap('557birthdaycake1_100853.ico')

def show_date():
    current_date = strftime('%Y-%m-%d')
    date_label.config(text=current_date)
    date_label.after(1000, show_date)


def choice_month(event):
    month = event.widget.get()
    print("Your birth month:", month)


def choice_day(event):
    day = event.widget.get()
    print("Your birth day:", day)


def choice_year(event):
    year = event.widget.get()
    print("Your birth year:", year)


def choice():
    showinfo(title="Selection", message=f'You selected {month_input.get()}/{day_input.get()}/{year_input.get()}')


def age():
    selected_year = int(year_input.get())
    current_year = 2025
    age = current_year - selected_year
    showinfo(title="Check Age", message=f'Your age is {age} years old')


def days_until_next_birthday():
    selected_month = month_input.get().strip()
    selected_day = int(day_input.get())
    selected_year = int(year_input.get())


    months = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    selected_month_number = months.get(selected_month, None)

    if selected_month_number is None:
        showinfo(title="Error", message="Invalid month selection.")
        return

    today = datetime.today()
    next_birthday = datetime(today.year, selected_month_number, selected_day)

    if today > next_birthday:
        next_birthday = datetime(today.year + 1, selected_month_number, selected_day)


    days_remaining = (next_birthday - today).days
    showinfo(title="Days Until Next Birthday", message=f'Days until next birthday: {days_remaining} days')


ttk.Label(window, text="SELECT THE MONTH OF YOUR BIRTH :", background="#36393e", foreground="#CED4DA",
          font=("Times New Roman", 12)).grid(column=0, row=5, padx=5, pady=25)
ttk.Label(window, text="SELECT THE DAY OF YOUR BIRTH :", background="#36393e", foreground="#CED4DA",
          font=("Times New Roman", 12)).grid(column=0, row=15, padx=5, pady=25)
ttk.Label(window, text="SELECT THE YEAR OF YOUR BIRTH :", background="#36393e", foreground="#CED4DA",
          font=("Times New Roman", 12)).grid(column=0, row=25, padx=5, pady=25)

month_input = tk.StringVar()
month = ttk.Combobox(window, width=27, textvariable=month_input, background="#808080")
day_input = tk.StringVar()
day = ttk.Combobox(window, width=27, textvariable=day_input, background="#808080")
year_input = tk.StringVar()
year = ttk.Combobox(window, width=27, textvariable=year_input, background="#808080")

month['values'] = (' January',
                   ' February',
                   ' March',
                   ' April',
                   ' May',
                   ' June',
                   ' July',
                   ' August',
                   ' September',
                   ' October',
                   ' November',
                   ' December')
day['values'] = [str(i) for i in range(1, 32)]
year['values'] = [str(i) for i in range(1970, 2025)]

month.grid(column=1, row=5)
month.current()
day.grid(column=1, row=15)
day.current()
year.grid(column=1, row=25)
year.current()

ttk.Label(window, text="CURRENT DATE:", background="#36393e", foreground="#CED4DA", font=("Times New Roman", 12)).grid(
    column=0, row=40)
date_label = ttk.Label(window, font=('Times New Roman', 12, 'bold'), background="#36393e", foreground="#CED4DA", )
date_label.grid(column=0, row=45)

show_date()

tk.Button(window, text="SHOW BIRTH DATE", command=choice, bg='#CED4DA').grid(column=1, row=40)
tk.Button(window, text="SHOW AGE", command=age, bg='#CED4DA').grid(column=1, row=45)
tk.Button(window, text="DAYS UNTIL NEXT BIRTHDAY", command=days_until_next_birthday, bg='#CED4DA').grid(column=0,
                                                                                                        row=50)
month.bind("<<ComboboxSelected>>", choice_month)
day.bind("<<ComboboxSelected>>", choice_day)
year.bind("<<ComboboxSelected>>", choice_year)

window.mainloop()
