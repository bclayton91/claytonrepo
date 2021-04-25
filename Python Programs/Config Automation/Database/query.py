#Import required libraries
from tkinter import *
from sitedatabase import database

##Define GUI Functions
def click():
    text=textbox.get()
    output.delete(0.0, END)
    iteration=0
    datalen=int(len(database))
    for i in range(0,datalen):
        if database[i]["Site"]==text:
            displaytext=f"Site {text} found in site database"
            break
                
        elif iteration >= (datalen-1):
            displaytext=f"{text} is not a valid site"
            break

        elif database[i]["Site"]!=text:
            iteration+=1
            continue
                
    output.insert(END,displaytext)

                    
def closeprogram():
    window.destroy()

##Set GUI parameters
window = Tk()
window.title("Site search")
window.configure(background="deep sky blue")
window.geometry("500x500")

##upload Gui Photo
photo1=PhotoImage(file="C:\GitExample1\Git\Python Programs\TKinter\mytestgif.gif")

##Create label to present photo
photoLabel=Label (window, image=photo1, bg="deep sky blue") 
photoLabel.grid(row=0, column=0, sticky=W)

##This label displays ("Enter Site Name") above textbox 
siteNameLabel=Label(window, text="Enter Site Name",width=15, bg="black", fg="white",
 font="none 12 bold") 
siteNameLabel.grid(row=1, column=0, pady=(50,0), sticky=W)

##Create textbox to collect user input
textbox=Entry(window, width=25, bg="white")
textbox.grid(row=4, column=0, sticky=W)

##This button is used to search database for user input
searchButton=Button(window, text="Search", width=15, bg="lawn green", fg="black",command=click) 
searchButton.grid(row=5, column=0, sticky=W)


output= Text(window, width=60, height=6, bg="white", wrap=WORD)
output.grid(row=6, column=0, columnspan=2, sticky=W, pady=(0,20))

exitLabel=Label(window, text="Exit the program when finished", bg="black", fg="white", 
font="none 12 bold") 
exitLabel.grid(row=9, column=0, pady=(20,0),sticky=W)

##Create button used to terminate program
exitButton=Button(window, text="Close program", width=15, command=closeprogram, bg="lawn green", 
fg="black") 
exitButton.grid(row=10, column=0, sticky=W)

##Run the program
window.mainloop()