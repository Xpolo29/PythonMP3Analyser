#Projet Maella V1

#Partie 0
#Importation des librairies (works !)
import os
import sys
import time
import math
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Entry
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import scipy.io.wavfile as wave2
import wave
import pyaudio
from numpy.fft import fft
from pydub import AudioSegment
import threading


#Partie 1
#demande avec GUI le nombre de fichier .mp3 (works !)
def returned(): 
    try:
        i = int(nb.get())
        if i <= 0 or i > 20:
            master.mainloop()
        master.quit()
        return i
    except ValueError:
        master.mainloop()


def TrueQuit():
    master.destroy()
    root.destroy()
    exit()


master = tk.Tk()
master.title('Programme Maella V1')
tk.Label(master, text="Nombre de fichier audio ? (20 max)").grid(row=1)
nb = tk.Entry(master)
nb.grid(row=1, column=1)
tk.Button(master, text='Annuler', command=TrueQuit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Valider', command=returned).grid(row=3, column=1, sticky=tk.W, pady=4)
master.mainloop()      
I = int(returned())
master.destroy()  

#Partie 2
#Selection des Fichiers (works !)
listMP3 = []
def TupleToStr(file_path):  
    str = ''.join(file_path)
    return str


while I > 0:
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selectionnez un fichier .mp3")
    if file_path:
        I = I-1
        str = TupleToStr(file_path)
        listMP3.append(str)
    else:
        ok = tk.messagebox.askokcancel(title='Attention', message='Pas de fichier selectionné !')
        if not ok:
            root.destroy()
            exit()


root = tk.Tk()
root.withdraw()
tk.messagebox.showinfo(title='Programme Maella V1', message='Tous les fichiers on été selectionnés')
root.destroy()

#Partie 3
#Etude des sons + streaming audio (works !)

def play(fname): #wav and wait for the end of the song played
    try:
        ding_wav = wave.open(fname, 'rb')
        ding_data = ding_wav.readframes(ding_wav.getnframes())
        audio = pyaudio.PyAudio()
        stream_out = audio.open(
            format=audio.get_format_from_width(ding_wav.getsampwidth()),
            channels=ding_wav.getnchannels(),
            rate=ding_wav.getframerate(), input=False, output=True)
        stream_out.start_stream()
        stream_out.write(ding_data)
        stream_out.stop_stream()
        stream_out.close()
        audio.terminate()
    except ValueError:
        root = tk.Tk()
        root.withdraw()
        ok = tk.messagebox.showerror(command=TrueQuit(), title='Erreur', message='Erreur lors de la lecture d\'un fichier')


def PutLongestSongFirst():   # Fusion keep the lentgth of the first element
    a = 0
    for x in listMP3:
        song = AudioSegment.from_file(x)
        t = song.duration_seconds
        if t > a:
            n = listMP3.index(x)
            a = t
    listMP3.insert(0, listMP3[n])
    del listMP3[n+1]


PutLongestSongFirst()


sound0 = AudioSegment.from_file(listMP3[0])
for x in listMP3:
    sound1 = AudioSegment.from_file(x)
    sound2 = sound0.overlay(sound1)
    sound0 = sound2
sound2.export('temp.wav', format='wav')
p = threading.Thread(target=play, args=('temp.wav', ))
p.start()


#Partie 4
#Rendu graphique

fig = plt.figure(1, figsize=[8.32, 6.24])
plt.autoscale(enable=True, axis='both')

if p.is_alive() is True:
    fs, data = wave2.read('temp.wav')
    n = data.size
    duree = int((1.0*n/(2*fs))+1)
    print(fs, data, duree, len(data))
    plt.axes(data)
    plt.show()

