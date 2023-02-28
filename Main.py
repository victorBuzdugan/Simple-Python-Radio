import vlc
import json
import os
from tkinter import *
from tkinter import ttk

#import radio stations file
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, './RadioStations.json')
with open(file_path, 'r') as jsonFile:
  radioStations = json.load(jsonFile)
radioStations.pop("_comment")
DEFAULT_RADIO = list(radioStations.keys())[0]
radioStationsNames = sorted(radioStations, key=str.lower)

def playRadio():
    radio = selectedRadio.get()
    media = instance.media_new(radioStations.get(radio))
    player.set_media(media)
    player.play()

def stopRadio():
    player.stop()

def updateCombobox(event):
    playRadio()

def previousRadio():
    currentRadioIndex = radioStationsNames.index(selectedRadio.get())
    maxRadioIndex = len(radioStationsNames)-1
    if currentRadioIndex == 0:
        selectRadioCombobox.set(radioStationsNames[maxRadioIndex])
    else:
        selectRadioCombobox.set(radioStationsNames[currentRadioIndex-1])
    playRadio()

def nextRadio():
    currentRadioIndex = radioStationsNames.index(selectedRadio.get())
    maxRadioIndex = len(radioStationsNames)-1
    if currentRadioIndex == maxRadioIndex:
        selectRadioCombobox.set(radioStationsNames[0])
    else:
        selectRadioCombobox.set(radioStationsNames[currentRadioIndex+1])
    playRadio()

#initialize VLC
instance = vlc.Instance()
instance.log_unset()
player = instance.media_player_new()

#initialize Tkinter
rootFrame = Tk()
rootFrame.title("Radio")
mainFrame = ttk.Frame(rootFrame, padding=20)

#region Widget creation
selectedRadio = StringVar()
selectRadioCombobox = ttk.Combobox(
    mainFrame,
    state='readonly',
    justify='center',
    values=radioStationsNames,
    height=20,
    textvariable=selectedRadio
)
selectRadioCombobox.current(radioStationsNames.index(DEFAULT_RADIO))
selectRadioCombobox.bind("<<ComboboxSelected>>", updateCombobox)
playButton = ttk.Button(mainFrame, text="Play", command=playRadio)
stopButton = ttk.Button(mainFrame, text="Stop", command=stopRadio)
previousButton = ttk.Button(mainFrame, text="Prev", command=previousRadio)
nextButton = ttk.Button(mainFrame, text="Next", command=nextRadio)
#endregion

#region Widget arrangement
mainFrame.grid(column=0, row=0)
selectRadioCombobox.grid(column=1, row=0, columnspan=2, padx=5, pady=5)
playButton.grid(column=1, row=2, padx=5, pady=5)
stopButton.grid(column=2, row=2, padx=5, pady=5)
previousButton.grid(column=1, row=3, padx=5, pady=5)
nextButton.grid(column=2, row=3, padx=5, pady=5)
#endregion

playRadio()

rootFrame.mainloop()
