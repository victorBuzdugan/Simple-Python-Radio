import vlc
from tkinter import *
from tkinter import ttk

radioStations = {
    'Kiss FM' : 'https://live.kissfm.ro/kissfm.aacp',
    'Europa FM' : 'https://astreaming.edi.ro:8443/EuropaFM_aac',
    'Digi FM' : 'http://edge76.rdsnet.ro:84/digifm/digifm.mp3',
    'Radio Iasi?' : 'http://89.238.227.6:8202/',
    'Virgin Radio' : 'https://astreaming.edi.ro:8443/VirginRadio_aac',
    'Radio ZU' : 'https://ivm.antenaplay.ro/liveaudio/radiozu/playlist.m3u8',
    'Magic FM' : 'https://live.magicfm.ro/magicfm.aacp',
    'Rock FM' : 'https://live.rockfm.ro/rockfm.aacp',
    'Pro FM' : 'https://edge126.rcs-rds.ro/profm/profm.mp3',
    'Guerilla' : 'https://live.guerrillaradio.ro:8443/guerrilla.aac',
    'm2O' : 'https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2o/radiom2o/master_ma.m3u8',
    'Antenne Bayern' : 'https://stream.antenne.de/antenne/stream/mp3'
}

radioStationsNames = sorted(radioStations, key=str.lower)

DEFAULT_RADIO = 'Kiss FM'

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
