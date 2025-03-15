from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='First number')
        self.t1 = Entry(bd=5, width=45)
        self.t1.place(x=170, y=50)
        self.lbl1.place(x=45, y=50)


        self.lbl2 = Label(win, text='Second number')
        self.t2 = Entry(bd=5, width=45)
        self.lbl2.place(x=45, y=100)
        self.t2.place(x=170, y=100)


        self.lbl3 = Label(win, text='Result')
        self.t3 = Entry(bd=5, width=45)
        self.lbl3.place(x=45, y=150)
        self.t3.place(x=170, y=150)

#BUTTONS

        self.btn1 = Button(win, text='Add', command=self.add)
        self.btn1.place(x=45, y=200)

        self.btn2 = Button(win, text='Subtract', command=self.sub)
        self.btn2.place(x=125, y=200)

        self.btn3 = Button(win, text='Multiply', command=self.multiply)
        self.btn3.place(x=225, y=200)

        self.btn4 = Button(win, text='Divide', command=self.divide)
        self.btn4.place(x=325, y=200)

        self.btn5 = Button(win, text='Clear', command=self.clear)
        self.btn5.place(x=415, y=200)


    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def multiply(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def divide(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1/num2
        self.t3.insert(END, str(result))

    def clear(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.title('CALCULATOR ENGINE')
window.geometry("500x300+10+10")
window.configure(bg="lightblue")

window.mainloop()
