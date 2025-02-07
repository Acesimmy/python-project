from tkinter import *

app = Tk()
app.title = "Scale"

app.geometry("500x500")

def scalle(input):
    print("Scale values are :"+input)


scale = Scale(app, from_=2, to_=100, command=scalle, orient=HORIZONTAL)
scale.grid(row=4,column=1)

app.mainloop()