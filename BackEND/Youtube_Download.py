#!pip install pytubefix
from pytubefix import YouTube
from pytubefix.cli import on_progress


def download_video(url, saveLocation):
    yt = YouTube(url, on_progress_callback = on_progress)
    print("Downloading " , yt.title)
    ys = yt.streams.get_highest_resolution()
    ys.download(saveLocation)


# For loop that goes through the text file of videos 
with open("BackEND/Videos.txt", "r") as urls:
    lines = urls.readlines() 
    for url in lines:
        url = url.strip() 
        print(url)
        download_video(url, "BackEND/Videos Downloaded")

# User videos? 

download_video(user_url, "BackEND/Videos Downloaded")





