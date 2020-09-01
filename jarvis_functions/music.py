import os
from jarvis_functions import speaker

def music(query):
            music_dir = 'F:\\vikash\\fav music'
            songs = os.listdir(music_dir)
            for i in songs:
                print(i)
            st = "which one you want to play :"
            print(st)
            speaker.speak(st);
            n=int(input())
            os.startfile(os.path.join(music_dir, songs[n-1]))
