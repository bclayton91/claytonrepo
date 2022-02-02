
from tkinter import *
import time
from jinja2 import Environment, FileSystemLoader
import datetime
import os


window=Tk()
window.title('WANX Config Generator')
window.geometry('600x550')
window.configure(background="lavender")

Goudy = ("Goudy Old Style", "12", "bold")

def closeprogram():
    window.destroy()

def generateconfig():

    file_loader=FileSystemLoader('C:/GitExample1/Git/Python Programs/Riverbed')
    env=Environment(loader=file_loader)
    template=env.get_template('WANX.j2')
    output=template.render(
        hostname=hostnameEntry.get(),
        inPathDesc=inPathDescEntry.get(),
        inPathIp=inPathIpEntry.get(),
        inPathMask=inPathMaskEntry.get(),
        primaryip=primaryIpEntry.get(),
        primaryMask=primaryMaskEntry.get()
        )
    dtime=datetime.datetime.now()
    try:
        docname=f"WANX-config"
        fh=open(f'C:/GitExample1/Git/Python Programs/Riverbed/Configs/{docname}.txt', 'w')
        fh.write(output)
    except:
        os.makedirs('C:/GitExample1/Git/Python Programs/Riverbed/Configs')
        docname=f"WANX-config"
        fh=open(f'C:/GitExample1/Git/Python Programs/Riverbed/Configs/{docname}.txt', 'w')
        fh.write(output)


##Image Label
RiverbedImage=PhotoImage(file='C:/GitExample1/Git/Python Programs/Riverbed/Riverbed.gif')
RiverbedImageLabel=Label(window, image=RiverbedImage)
RiverbedImageLabel.grid(row=8, column=0)

##{{hostname}}
hostnameLabel=Label(window, bg="ivory", fg="black", text="Hostname", width=24, font=Goudy, anchor=W)
hostnameLabel.grid(row=9, column=0, sticky=W)
hostnameEntry=Entry(window, bg="white", fg="black", font=Goudy, width=27)
hostnameEntry.grid(row=10, column=0, sticky=W, pady=(0,20))

##{{inPathDesc}}
inPathDescLabel=Label(window, bg="ivory", fg="black", text="inPath description", width=24, font=Goudy, anchor=W)
inPathDescLabel.grid(row=11, column=0, sticky=W)
inPathDescEntry=Entry(window, bg="white", fg="black", font=Goudy, width=27)
inPathDescEntry.grid(row=12, column=0, sticky=W, pady=(0,20))

##{{inPathIp}}
inPathIpLabel=Label(window, bg="ivory", fg="black", text="inPath Ip address", width=24, font=Goudy, anchor=W)
inPathIpLabel.grid(row=13, column=0, sticky=W)
inPathIpEntry=Entry(window, bg="white", fg="black", font=Goudy, width=27)
inPathIpEntry.grid(row=14, column=0, sticky=W, pady=(0,20)) 

##{{inPathMask}}
inPathMaskLabel=Label(window, bg="ivory", fg="black", text="Mask", width=8, font=Goudy, anchor=W)
inPathMaskLabel.grid(row=13, column=1, sticky=W, padx=(10,0))
inPathMaskEntry=Entry(window, bg="white", fg="black", width=9, font=Goudy)
inPathMaskEntry.grid(row=14, column=1, sticky=W, padx=(10,0), pady=(0,20))

##{{primaryIp}}
primaryIpLabel=Label(window, bg="ivory", fg="black", text="Primary Ip address", width=24, font=Goudy, anchor=W)
primaryIpLabel.grid(row=16, column=0, sticky=W)
primaryIpEntry=Entry(window, bg="white", fg="black", font=Goudy, width=27)
primaryIpEntry.grid(row=17, column=0, sticky=W, pady=(0,20)) 

##{{primaryMask}}
primaryMaskLabel=Label(window, bg="ivory", fg="black", text="Mask", font=Goudy, width=8, anchor=W)
primaryMaskLabel.grid(row=16, column=1, padx=(10,0), sticky=W)
primaryMaskEntry=Entry(window, bg="white", fg="black", font=Goudy, width=9)
primaryMaskEntry.grid(row=17, column=1, sticky=W,padx=(10,0), pady=(0,20))

generateConfigButton=Button(window, bg="ivory", text="generate config", command=generateconfig, font=Goudy, width=15, anchor=W)
generateConfigButton.grid(row=30, column=0, sticky=W, pady=(0,20))
ExitButton=Button(window, bg="ivory", text="close program", command=closeprogram, font=Goudy, width=15, anchor=W)
ExitButton.grid(row=110, column=0, sticky=W)

window.mainloop()