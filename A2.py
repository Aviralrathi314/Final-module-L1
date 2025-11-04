from tkinter import*
window = Tk()
window.title("Welcome app")
window.geometry('350x300')
l1 = Label(window,text = "Welcome to my app", fg="blue" , bg = "yellow", font = ("Times", 20), height = 2, width = 300)
l2 = Label(window,text = "Enter your name", fg="green" , bg = "yellow", font = ("Times", 20), height = 1, width = 100)
e1 = Entry(window,font = ("Times", 20), width = 300)

def display():
    n = e1.get()
    global m

    m = "Hello" +n +"Welcome to the app"
    tb.insert(END,m)

tb = Text(height = 3)
b1 = Button(window,text = "Click me", fg = "blue", bg = "Pink", font = ("Times", 20), height = 2, width = 200, command = display)

l1.pack()
l2.pack()
e1.pack()
b1.pack()
tb.pack()
window.mainloop()