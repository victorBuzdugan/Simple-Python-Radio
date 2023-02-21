import vlc
import time

url = 'https://live.kissfm.ro/kissfm.aacp'


#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

#Define VLC player
player = instance.media_player_new()

#Define VLC media
media=instance.media_new(url)

#Set player media
player.set_media(media)

#Play the media
player.play()

a = input("Asa la misto")

# instance.wait()