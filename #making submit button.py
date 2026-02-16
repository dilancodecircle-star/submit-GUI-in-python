#making submit button 
from tkinter import*
window =Tk()
window.title(text = "Atheena code")
entry = Entry()
entry.pack()
entry.config(font = ("" , 50))
entry.config(bg = "black")
entry.config(fg = "green")
entry.config(width = 10)
def submit():
    uname = entry.get()
    print("hello " + uname)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1 , END)

submit = Button(window , text = "submit" , command = submit)
submit.pack(side = RIGHT)

delete = Button(window , text = "delete" , command = delete)
delete.pack(side = RIGHT)

backspace = Button(window , text = "backspace" , command = backspace)
backspace.pack(side = RIGHT)
window.mainloop()
