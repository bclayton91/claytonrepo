from tkinter import *
from jinja2 import Environment, FileSystemLoader
import os

def closeprogram():
    window.destroy()

def get_vpnrtr_config():
    outputBox.delete(0.0,END)
    Site=siteNameTextBox.get()
    output=template.render(
    Site=Site,
    Site_Id=siteIdTextBox.get(),
    Primary_Hub=primaryHubTextBox.get(),
    Secondary_Hub=secondaryHubTextBox.get(),
    Tertiary_Hub=tertiaryHubTextBox.get(),
    Community_String=communityStringTextBox.get()
    )

    docname=(f"{Site}-VPN-RTR-CONFIG")
    try:
        fh=open(f'C:\GitExample1\Git\Python Programs\Config Automation\Configurations\{docname}.txt', 'w')
        fh.write(output)
        fh.close()
        displaytext=f"Configuration generated for site: \"{Site}\"\nConfiguration stored in the following directory: C:\GitExample1\Git\Python Programs\Config Automation\Configurations"
        outputBox.insert(END,displaytext)
    except:
        os.makedirs('C:\GitExample1\Git\Python Programs\Config Automation\Configurations')
        fh=open(f'C:\GitExample1\Git\Python Programs\Config Automation\Configurations\{docname}.txt', 'w')
        fh.write(output)
        fh.close()
        displaytext=f"Configuration generated for site: \"{Site}\"\nConfiguration stored in the following directory: C:\GitExample1\Git\Python Programs\Config Automation\Configurations"
        outputBox.insert(END,displaytext)

file_loader=FileSystemLoader('C:\GitExample1\Git\Python Programs\Config Automation\Templates')
env=Environment(loader=file_loader)
template=env.get_template('VPNRTR.j2')

window=Tk()
window.title("Configuration Generator")
window.configure(background="deep sky blue")
window.geometry('550x740')

photo1=PhotoImage(file="C:\GitExample1\Git\Python Programs\TKinter\mytestgif.gif")
photoLabel=Label (window, image=photo1, bg="deep sky blue") 
photoLabel.grid(row=0, column=0, sticky=W)

myfont=("Goudy Old Style","12","bold")

siteNameLabel=Label(window, text="Enter Site Name:", bg="black", fg="white", width=15,
font=myfont, anchor=W)
siteNameLabel.grid(row=1, column=0, sticky=W)
siteNameTextBox=Entry(window, width=23, bg="white")
siteNameTextBox.grid(row=2, column=0, pady=(0,20), sticky=W)

siteIdLabel=Label(window, text="Enter Site Id", bg="black", fg="white", width=15,
font=myfont, anchor=W)
siteIdLabel.grid(row=3, column=0, sticky=W)
siteIdTextBox=Entry(window, width=23, bg="white")
siteIdTextBox.grid(row=4, column=0, sticky=W, pady=(0,20))

primaryHubLabel=Label(window, text="Enter primary hub ip address", bg="black", fg="white",
font=myfont, width=25, anchor=W)
primaryHubLabel.grid(row=5, column=0, sticky=W)
primaryHubTextBox=Entry(window, width=38, bg="white")
primaryHubTextBox.grid(row=6, column=0, sticky=W, pady=(0,20))

secondaryHubLabel=Label(window, text="Enter secondary hub ip address", bg="black", fg="white",
font=myfont, width=25, anchor=W)
secondaryHubLabel.grid(row=7, column=0, sticky=W)
secondaryHubTextBox=Entry(window, bg="white", width=38)
secondaryHubTextBox.grid(row=8, column=0, sticky=W, pady=(0,20))

tertiaryHubLabel=Label(window, text="Enter tertiary hub ip address", bg="black", fg="white",
font=myfont, width=25, anchor=W)
tertiaryHubLabel.grid(row=9, column=0, sticky=W)
tertiaryHubTextBox=Entry(window, bg="white", width=38)
tertiaryHubTextBox.grid(row=10, column=0, sticky=W, pady=(0,20))

communityStringLabel=Label(window, text="Enter community string", bg="Black", fg="white",
font=myfont, width=25, anchor=W)
communityStringLabel.grid(row=11, column=0, sticky=W)
communityStringTextBox=Entry(window, bg="white", width=38)
communityStringTextBox.grid(row =12, column=0, pady=(0,20), sticky=W)

getConfigButton=Button(window, text="Get configuration", command=get_vpnrtr_config, bg="lawn green", fg="black", width=15)
getConfigButton.grid(row=13, column=0, sticky=W)
outputBox=Text(window, width=50, height=5, bg="white", fg="black", wrap=WORD, font="none 10",)
outputBox.grid(row=14, column=0, columnspan=2, pady=(0,20))

exitButton=Button(window, text="Close program", width=15, command=closeprogram, bg="lawn green", 
fg="black",) 
exitButton.grid(row=20, column=0, sticky=W)



window.mainloop()