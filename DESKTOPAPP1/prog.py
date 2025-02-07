from tkinter import *
from tkinter import ttk

app=Tk()
app.title("Combo Box")

app.geometry("500x500")
def handlesubmit():
    lbl.configure(text=combo.get())

combo = ttk.Combobox()

combo['values'] = (1,2,3,4,5,"text")
combo.current(1)
combo.grid(column=0,row=0)


sub_btn=Button(text ='Submit', command =handlesubmit,background="pink")
sub_btn.grid(column=0, row=1)
lbl = Label(app,text="")
lbl.grid(column=0, row=2)
app.mainloop()