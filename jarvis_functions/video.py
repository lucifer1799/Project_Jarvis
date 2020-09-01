import vlc
import os
from jarvis_functions import speaker

def video(query):
        Instance = vlc.Instance()
        #print("hello")
        player = Instance.media_player_new()
        music_dir = 'F:\\vikash\\FUUL HD SONGS'
        songs = os.listdir(music_dir)
        j=1
        for i in songs:
                print(j,i)
                j=j+1
        print("which one do you want to play")
        n=int(input())
        Media = Instance.media_new(os.path.join(music_dir, songs[n-1]))
        player.set_media(Media)
        player.play()
        s=" "
        while(s!="quite"):
                s=input()
                if s=="pause":
                        player.pause()
                if s=="play":
                        player.play()
                
        player.stop()
