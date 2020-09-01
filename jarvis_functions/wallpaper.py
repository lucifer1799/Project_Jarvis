import ctypes
import os
from jarvis_functions import speaker
def wallpaper(query):
    pic_dir = 'C:\\Users\\Public\\Pictures'
    lst = os.listdir(pic_dir)
    j=1
    for i in lst:
        print(j,i)
        j=j+1
    print("which one do you want to set as wallpaper :")
    n=int(input())
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.join(pic_dir, lst[n-1]), 0)
