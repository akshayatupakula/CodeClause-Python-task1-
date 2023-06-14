#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pygame
from tkinter import Tk, Button, Label, Listbox, messagebox

class MusicPlayer:
    def _init_(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x400")

        self.music_directory = "Music"  # Change this to your music directory path

        self.song_listbox = Listbox(self.root, width=30, height=15)
        self.song_listbox.pack(pady=10)

        self.load_button = Button(self.root, text="Load Music", command=self.load_music)
        self.load_button.pack(pady=10)

        self.play_button = Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.pause_button = Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=5)

        self.stop_button = Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.current_song_label = Label(self.root, text="")
        self.current_song_label.pack(pady=10)

        self.song_files = []

    def load_music(self):
        self.song_files = []
        self.song_listbox.delete(0, "end")
        
        for file in os.listdir(self.music_directory):
            if file.endswith(".mp3"):
                self.song_files.append(file)
                self.song_listbox.insert("end", file)
        
        if not self.song_files:
            messagebox.showinfo("Error", "No music files found in the directory.")

    def play_music(self):
        selected_song = self.song_listbox.curselection()
        
        if selected_song:
            song_index = int(selected_song[0])
            song_file = self.song_files[song_index]
            song_path = os.path.join(self.music_directory, song_file)
            
            pygame.mixer.init()
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

            self.current_song_label.config(text="Now Playing: " + song_file)

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.current_song_label.config(text="")

# Create the Tkinter window
root = Tk()

# Create an instance of the music player
music_player = MusicPlayer(root)

# Run the Tkinter event loop
root.mainloop()

