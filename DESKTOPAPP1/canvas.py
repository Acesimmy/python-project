from tkinter import *

app = Tk()
app.title("Canvas Widget")

app.geometry("500x300")

canvas = Canvas(app,width=200,height=200)
canvas.pack()

canvas.create_line(0,0,200,100)
canvas.create_line(0,0,50,100)
canvas.create_rectangle(50,50,150,100)
canvas.create_oval(50,50,150,100)
canvas.create_polygon(50,50,150,50,100,100)
canvas.create_arc(50,50,100,150,start=0,extent=180)
canvas.create_text(120,100,text="Hi simmy")
app.mainloop()