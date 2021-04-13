from tkinter import *

window = Tk()
window.title("My test program")
window.configure(background="deep sky blue")
window.geometry("500x300")
photo1=PhotoImage(file="mytestgif.gif")
Label (window, image=photo1, bg="deep sky blue") .grid(row=0, column=0, sticky=W)


Label(window, text="This is a just a test label", bg="black", fg="white",
 font="none 12 bold") .grid(row=1, column=0, pady=(0,50), sticky=W)

Label(window, text="This is a just a second test label", bg="black", fg="white", 
font="none 12 bold") .grid(row=5, column=0, sticky=W)






window.mainloop()