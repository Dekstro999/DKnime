import tkinter as tk
from tkinter import ttk
import vlc

def play_video():
    url = url_entry.get()
    if url:
        media = vlc.MediaPlayer(url)
        media.play()

# Crear la ventana principal
root = tk.Tk()
root.title("Video Player")
root.geometry("800x600")

# Crear y colocar los widgets
label_url = tk.Label(root, text="URL del video:", font=('Helvetica', 14, 'bold'))
label_url.pack(pady=10)

url_entry = tk.Entry(root, width=65, font=('Arial', 12))
url_entry.pack(pady=10)

play_button = tk.Button(root, text="Reproducir", command=play_video, font=('Helvetica', 14, 'bold'))
play_button.pack(pady=10)

root.mainloop()
