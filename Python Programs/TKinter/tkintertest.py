from tkinter import *

def click():
    text=textbox.get()
    output.delete(0.0, END)

def closeprogram():
    window.destroy()

window = Tk()
window.title("My test program")
window.configure(background="deep sky blue")
window.geometry("500x400")
photo1=PhotoImage(file="mytestgif.gif")
Label (window, image=photo1, bg="deep sky blue") .grid(row=0, column=0, sticky=W)


Label(window, text="Enter parameters", bg="black", fg="white",
 font="none 12 bold") .grid(row=1, column=0, pady=(50,0), sticky=W)

textbox=Entry(window, width="20", bg="white")
textbox.grid(row=4, column=0, sticky=W)

Button(window, text="Submit", width=15, bg="yellow", fg="black",command=click) .grid(
    row=5, column=0, sticky=W)

Label(window, text="Exit the program when finished", bg="black", fg="white", 
font="none 12 bold") .grid(row=6, column=0, pady=(20,0),sticky=W)

Button(window, text="Close program", width=15, command=closeprogram, bg="yellow", 
fg="black") .grid(
    row=8, column=0, sticky=W)







window.mainloop()