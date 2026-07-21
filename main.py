import tkinter as tk
from PIL import Image, ImageTk
import pygame.mixer

def play_sound_animals(i):
    pygame.mixer.music.load(animals_sounds[i])
    pygame.mixer.music.play()

def play_sound_colours(index, jendela):
    if index == 0:
        jendela.configure(bg='blue')
    elif index == 1:
        jendela.configure(bg='green')
    elif index == 2:
        jendela.configure(bg='white')
    elif index == 3:
        jendela.configure(bg='red')
    elif index == 4:
        jendela.configure(bg='purple')
    elif index == 5:
        jendela.configure(bg='yellow')

    pygame.mixer.music.load(colours_sound[index])
    pygame.mixer.music.play()


gui = tk.Tk()
pygame.mixer.init()
gui.title("TB 1 Algoritma Lanjut Kelompok 7")

animals_picture = [
    "images/ayam.png",
    "images/bebek.png",
    "images/burung.png",
    "images/gajah.png",
    "images/monyet.png",
    "images/sapi.png",
]

animals_sounds = [
    "sounds/ayam.mp3",
    "sounds/bebek.mp3",
    "sounds/burung.mp3",
    "sounds/gajah.mp3",
    "sounds/monyet.mp3",
    "sounds/sapi.mp3",
]

colours = [
    "blue", "green", "white", "red", "purple", "yellow"
]
colours_sound = [
    "sounds/blue.mp3",
    "sounds/green.mp3",
    "sounds/white.mp3",
    "sounds/red.mp3",
    "sounds/purple.mp3",
    "sounds/yellow.mp3"
]

baris1 = tk.Frame(gui)
baris2 = tk.Frame(gui)
baris1.pack()
baris2.pack()


def ambil_foto(index, frame):
    gambar = Image.open(animals_picture[index])
    gambar = gambar.resize((200, 200))
    photo = ImageTk.PhotoImage(gambar)
    tombol_gambar = tk.Button(
        frame, image=photo, command=lambda i=index: play_sound_animals(i))
    tombol_gambar.photo = photo
    tombol_gambar.pack(side='left', padx=10, pady=10)

def colours_page():
    tombol_halaman_dua.config(state=tk.NORMAL)
    pygame.mixer.music.pause()
    gui_warna = tk.Toplevel()
    gui_warna.title("Halaman Warna")
    label_halaman_warna = tk.Label(gui_warna, text='Menu suara warna')
    label_halaman_warna.pack()

    frame_warna = tk.Frame(gui_warna)
    frame_warna.pack()

    num_columns = 3

    for i in range(len(colours)):
        tombol_warna = tk.Button(
            frame_warna, text=colours[i], command=lambda i=i: play_sound_colours(i, gui_warna))
        tombol_warna.grid(row=i // num_columns, column=i %
            num_columns, padx=10, pady=10)

    frame_warna.grid_rowconfigure(0, minsize=50)
    frame_warna.grid_columnconfigure(0, minsize=50)
    

def animals_page():
    tombol_halaman_satu.config(state=tk.DISABLED)
    tombol_halaman_dua.config(state=tk.NORMAL)
    judul = tk.Label(gui, text='Menu suara hewan')
    judul.pack()
    for i in range(len(animals_picture)):
        if i < 3:
            ambil_foto(i, baris1)
        else:
            ambil_foto(i, baris2)
    label = tk.Label(gui, text="Selamat datang di Aplikasi GUI Kelompok 7")
    label.pack()


label = tk.Label(
    gui, text="Selamat datang di program Aplikasi GUI Pyhton TB 1 Algoritma Lanjut - Kelompok 7\n\nAnggota:\nMochammad Irsyad Kurniawan - (41522010224)\nMuhammad Danu Setiawan - (41522010194)\nMuhammad Alfarisi - (41522010192)\n Annas Wicaksono - (41522010211)")
label.pack(pady=20)

frame = tk.Frame(gui)
frame.pack()

tombol_halaman_satu = tk.Button(
    frame, text="Animals Page", command=animals_page)
tombol_halaman_satu.pack(side="left", padx=10)

tombol_halaman_dua = tk.Button(
    frame, text="Colours Page", command=colours_page)
tombol_halaman_dua.pack(side="left", padx=10)

gui.mainloop()
