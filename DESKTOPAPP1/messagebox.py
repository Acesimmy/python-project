from tkinter import *
from tkinter import messagebox

app =Tk()
app.title("Message Box")
app.geometry("700x700")


def click():
    messagebox.showinfo("information","you clicked me")

btn =Button(app,text="click me",command=click)
btn.pack()

def click1():
   messagebox.showwarning("warning","you clicked me")

btn1 =Button(app,text="click me",command=click1)
btn1.pack()

def click2():
   messagebox.showerror("error","you clicked me")

btn2 =Button(app,text="click me",command=click2)
btn2.pack()


app.mainloop()