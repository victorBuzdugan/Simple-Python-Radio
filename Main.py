import vlc
import time
from operator import itemgetter

radioStations = [
    {'name' : 'Kiss FM', 'url' : 'https://live.kissfm.ro/kissfm.aacp'},
    {'name' : 'Europa FM', 'url' : 'https://astreaming.edi.ro:8443/EuropaFM_aac'},
    {'name' : 'Digi FM', 'url' : 'http://edge76.rdsnet.ro:84/digifm/digifm.mp3'},
    {'name' : 'Radio Iasi?', 'url' : 'http://89.238.227.6:8202/'},
    {'name' : 'Virgin Radio', 'url' : 'https://astreaming.edi.ro:8443/VirginRadio_aac'},
    {'name' : 'Radio ZU', 'url' : 'https://ivm.antenaplay.ro/liveaudio/radiozu/playlist.m3u8'},
    {'name' : 'Magic FM', 'url' : 'https://live.magicfm.ro/magicfm.aacp'},
    {'name' : 'Rock FM', 'url' : 'https://live.rockfm.ro/rockfm.aacp'},
    {'name' : 'Pro FM', 'url' : 'https://edge126.rcs-rds.ro/profm/profm.mp3'},
    {'name' : 'Guerilla', 'url' : 'https://live.guerrillaradio.ro:8443/guerrilla.aac'},
    {'name' : 'm2O', 'url' : 'https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2o/radiom2o/master_ma.m3u8'},
    {'name' : 'Antenne Bayern', 'url' : 'https://stream.antenne.de/antenne/stream/mp3'}
]

DEFAULT_RADIO = 'Kiss FM'

#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
instance.log_unset()

#Define VLC player
player = instance.media_player_new()

for radio in radioStations:
    radioIndex = radioStations.index(radio)
    print(radioIndex+1, '-', radioStations[radioIndex]['name'])

selectedRadio = 0
while True:
    # time.sleep(1)
    selectRadio = input("Select radio number ('0' for exit; default '1'): ") or '1'
    if selectRadio.lower() == 'n':
        if selectedRadio == len(radioStations)-1:
            selectedRadio = 0
        else:
            selectedRadio += 1
    elif selectRadio.lower() == 'p':
        if selectedRadio == 0:
            selectedRadio = len(radioStations)-1
        else:
            selectedRadio -= 1
    elif selectRadio == '0':
        break
    else:
        try:
            selectedRadio = int(selectRadio)-1
        except:
            continue
        else:
            if selectedRadio < 0 or selectedRadio > len(radioStations)-1:
                continue
    media = instance.media_new(radioStations[selectedRadio]['url'])
    player.set_media(media)
    player.play()
    print('\nNow playing:', radioStations[selectedRadio]['name'], '\n')
    continue
    