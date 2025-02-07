from tkinter import *
from PIL import Image, ImageTk

app =Tk()
app.title("Static Image")

app.geometry("5000x5000")

lbl = Label(app,text="Static Image")
lbl.pack()

image = Image.open("./cat.jpeg")
photo = ImageTk.PhotoImage(image)

lblimg = Label(app,image= photo)
lblimg.grid(row=0,column=0)

image1 = Image.open("./cat1.jpeg")
photo1 = ImageTk.PhotoImage(image1)

lblimg1 = Label(app,image= photo1)
lblimg1.grid(row=0,column=1)

image2 = Image.open("./cat2.jpeg")
photo2 = ImageTk.PhotoImage(image2)

lblimg2 = Label(app,image= photo2)
lblimg2.grid(row=0,column=2)

image3 = Image.open("./cat3.jpeg")
photo3 = ImageTk.PhotoImage(image3)

lblimg3 = Label(app,image= photo3)
lblimg3.grid(row=0,column=3)

app.mainloop()