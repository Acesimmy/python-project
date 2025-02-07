import tkinter as tk

def print_input1():
    value = entry1.get()
    listbox.insert(tk.END, f"Input 1: {value}")

def print_input2():
    value = entry2.get()
    listbox.insert(tk.END, f"Input 2: {value}")

def print_input3():
    value = entry3.get()
    listbox.insert(tk.END, f"Input 3: {value}")

# Create the main window
root = tk.Tk()
root.title("Input Box and Listbox Demo")

# Create input boxes
label1 = tk.Label(root, text="Input 1:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Input 2:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="Input 3:")
label3.grid(row=2, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

# Create listbox
listbox = tk.Listbox(root)
listbox.grid(row=3, columnspan=2)

# Create buttons
button1 = tk.Button(root, text="Print Input 1", command=print_input1)
button1.grid(row=4, column=0)

button2 = tk.Button(root, text="Print Input 2", command=print_input2)
button2.grid(row=4, column=1)

button3 = tk.Button(root, text="Print Input 3", command=print_input3)
button3.grid(row=5, column=0, columnspan=2)

root.mainloop()