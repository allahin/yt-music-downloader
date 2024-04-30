from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
from moviepy.editor import VideoFileClip
from ctypes import windll
import os
import tkinter as tk

windll.shcore.SetProcessDpiAwareness(1)

def download_and_convert():
    video_id = id_entry.get()
    youtube_link = "https://www.youtube.com/watch?v=" + video_id

    try:
        yt = YouTube(youtube_link)
        video = yt.streams.get_highest_resolution().download()
        messagebox.showinfo("Success", "Video downloaded successfully!")

        audio_file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Waveform Audio", "*.wav")])
        if not audio_file_path:
            return

        video_clip = VideoFileClip(video)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_file_path)
        audio_clip.close()
        video_clip.close()

        os.remove(video)

        messagebox.showinfo("Success", f"Audio saved successfully to {audio_file_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("YTDown")
root.resizable(False, False)
root.tk.call("source", "azure.tcl")
root.iconbitmap('icon.ico')
root.tk.call("set_theme", "dark")

id_label = ttk.Label(root, text="Enter the video ID:")
id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
id_entry = ttk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

download_button = ttk.Button(root, text="Download and Convert", command=download_and_convert)
download_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

root.mainloop()