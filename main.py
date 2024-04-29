from pytube import YouTube
from moviepy.editor import *

id = input("Enter the video ID: ")

name = input("Enter the file name: ")

control = input("Shall we proceed? (y/n): ")

if control != "y":
    print("Exiting...")
    exit()

youtube_link = "https://www.youtube.com/watch?v="+id

yt = YouTube(youtube_link)
video = yt.streams.get_highest_resolution().download()

videoclip = VideoFileClip(video)
audioclip = videoclip.audio 

audioclip.write_audiofile(name+".wav")

videoclip.close()
audioclip.close()