from tkinter import *

app=Tk()
app.title("Hello World")

app.geometry("500x500")

text = Text(app)
text.insert(INSERT,"Hello ......")
text.insert(END,"Bye...")
text.pack()
app.mainloop()