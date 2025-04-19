#!pip install pytube

from pytube import YouTube 
def download_video(url, saveLocation):
    youtube = YouTube(url)
    youtube.check_availability()
    stream = youtube.streams.get_highest_resolution()
    stream.download(output_path=saveLocation)

with open("BackEND/Videos.txt", "r") as urls:
     for url in urls:
        download_video(url.strip(), "BackEND/Videos Downloaded")
