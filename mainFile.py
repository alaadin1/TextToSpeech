from tkinter import *
from tkinter import ttk
from typing import Collection
from gtts import gTTS
from playsound import playsound

#for the tkinter library, we can use widgets to make our GUI
#we have to always pass the parent wehnever we istnatiate a widget property 
#there are several configurations options for the widgets, such as specfiyin text, buttons (and what they do),labels, etc
# for the button option, we can create it using ttk.Button(root, text = 'Hello', command = 'buttonpressed) command is a function that is called when we press hte button
# to get all info on all options for a widget: button.configure()


def textToSpeech():
    message = text.get()
    speech = gTTS(text=message)
    speech.save('speech.mp3')
    playsound('speech.mp3')

def exit ():
    root.destroy()

def reset():
    msg.set("")

root = Tk()

#Initialize the window
root.geometry('600x400')
root.configure(bg='ghost white')
root.title('TEXT TO SPEACH')
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)
msg = StringVar()

#add the labels and entries
content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=0, relief="ridge", width=150, height=100)
titleLabel = ttk.Label(content, text = 'TEXT TO SPEECH PROGRAM', font = 'arial 20 bold', background='ghost white')
promptLabel = ttk.Label(content, text = 'Enter Text:', font= 'arial 14 bold ' )
text = ttk.Entry(content, textvariable= msg)

#add the buttons
playButt = ttk.Button(root, text = 'Play Sound', command=textToSpeech)
resetButt = ttk.Button(root, text = 'Clear Text', command=reset)
exitButt = ttk.Button(root, text = 'Exit', command=exit )


#Place the labels. buttons, and entries on the window
content.grid(column = 0, row = 0, sticky=(N,W,E,S))
frame.grid(column = 0, row = 0, columnspan = 2, rowspan = 1 )
titleLabel.grid(column= 2, row = 0)
text.grid(column=2, row = 5)
promptLabel.place(x=250, y =70)
playButt.place(x = 150, y = 150)
resetButt.place(x = 250, y = 150 )
exitButt.place(x = 350, y = 150)


root.mainloop()