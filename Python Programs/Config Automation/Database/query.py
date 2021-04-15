from tkinter import *
from sitedatabase import database

def click():
    text=textbox.get()
    output.delete(0.0, END)
    iteration=0
    for i in range(0,3):
        if database[i]["Site"]==text:
            displaytext=f"{text} is a valid site"
            break
                
        elif iteration >= 2:
            displaytext=f"{text} is not a valid site"
            break

        elif database[i]["Site"]!=text:
            iteration=iteration+1
            continue
                
    output.insert(END,displaytext)

                    
def closeprogram():
    window.destroy()

window = Tk()
window.title("Site search")
window.configure(background="deep sky blue")
window.geometry("500x500")
photo1=PhotoImage(file="C:\GitExample1\Git\Python Programs\TKinter\mytestgif.gif")
Label (window, image=photo1, bg="deep sky blue") .grid(row=0, column=0, sticky=W)


Label(window, text="Enter Site Name",width=15, bg="black", fg="white",
 font="none 12 bold") .grid(row=1, column=0, pady=(50,0), sticky=W)

textbox=Entry(window, width=25, bg="white")
textbox.grid(row=4, column=0, sticky=W)
text=textbox.get()

Button(window, text="Submit", width=15, bg="lawn green", fg="black",command=click) .grid(
    row=5, column=0, sticky=W)
output= Text(window, width=60, height=6, bg="white", wrap=WORD)
output.grid(row=6, column=0, columnspan=2, sticky=W, pady=(0,20))

Label(window, text="Exit the program when finished", bg="black", fg="white", 
font="none 12 bold") .grid(row=9, column=0, pady=(20,0),sticky=W)

Button(window, text="Close program", width=15, command=closeprogram, bg="lawn green", 
fg="black") .grid(
    row=10, column=0, sticky=W)


window.mainloop()