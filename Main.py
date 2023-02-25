import vlc
from operator import itemgetter
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

radioStationsList = [radio for radio in radioStations.keys()]
radioStationsList.sort()

DEFAULT_RADIO = 'Kiss FM'

def play(radio):
    media = instance.media_new(radioStations.get(radio))
    player.set_media(media)
    player.play()

instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player = instance.media_player_new()

rootFrame = Tk()
rootFrame.title("Radio")

mainFrame = ttk.Frame(rootFrame, padding=20)

selectedRadio = StringVar()
selectRadio = ttk.Combobox(mainFrame, state='readonly', textvariable=selectedRadio)
selectRadio['values'] = radioStationsList
selectRadio.current(selectRadio['values'].index(DEFAULT_RADIO))
selectRadio.bind("<<ComboboxSelected>>", play(selectedRadio.get()))


nowPlayingLabel = ttk.Label(mainFrame, textvariable=selectedRadio)
playButton = ttk.Button(mainFrame, text="Play", command=lambda: play(selectedRadio.get()))

mainFrame.grid(column=0, row=0)
selectRadio.grid(column=1, row=0)
ttk.Label(mainFrame, text="Radio now playing:").grid(column=1, row=1)
nowPlayingLabel.grid(column=2, row=1)
playButton.grid(column=1, row=2, columnspan=2)


rootFrame.mainloop()
