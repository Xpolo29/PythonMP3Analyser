#Projet Maella V1

#Partie 0
#Importation des librairies (works !)
from time import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wave
from numpy.fft import fft
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Entry
from scipy.io import wavfile

#Partie 1
#demande avec GUI le nombre de fichier .mp3 (works !)
def returned(): 
    try:
        i=int(nb.get())
        if i <= 0 or i > 20:
            master.mainloop()
        master.quit()
        return i
    except ValueError:
        master.mainloop()

def quit():
    master.destroy()
    exit()

master = tk.Tk()
master.title('Programme Maella V1')
tk.Label(master, text="Nombre de fichier .mp3 ? (20 max)").grid(row=1)
nb = tk.Entry(master)
nb.grid(row=1, column=1)
tk.Button(master, text='Annuler', command=quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Valider', command=returned).grid(row=3, column=1, sticky=tk.W, pady=4)
master.mainloop()      
I=int(returned())
master.destroy()  

#Partie 2
#Selection des Fichiers (works !)
list1 = []
def TupleToStr(file_path):  
    str =  ''.join(file_path) 
    return str

while I > 0:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title = "Selectionnez un fichier .mp3")
        if file_path:
            I=I-1
            str = TupleToStr(file_path)
            print('Vous avez selectionné le fichier suivant : '+str)
            list1.append(str)
        else:
            ok = tk.messagebox.askokcancel(title='Attention', message='Pas de fichier selectionné !')
            if not ok:
                root.destroy()
                exit()

tk.messagebox.showinfo(title='Programme Maella V1', message='Tous les fichiers on été selectionnés')

#Partie 3
#Etude des .wav et rendu graphique

fs, data = wavfile.read(str)
n = data.size
duree = (1.0*n)/(fs*2)
print(fs,data, duree)


te = 1.0/fs
t = np.zeros(n)
for k in range(n):
    t[k] = te*k
fig = plt.figure(figsize=(12,4))
plot = plt.plot(t,data)
xlabel = plt.xlabel("t (s)")
ylabel = plt.ylabel("amplitude")
axis = plt.axis([0,duree,data.min(),data.max()])

x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]

fig = plt.figure(1, figsize=(5,3))
plt.plot(x, y, 'ro')
plt.savefig('figsize_test1.png',dpi=100)
plt.show()

