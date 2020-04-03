#Projet Maella V1

#Partie 0
#Importation des librairies (works !)
from time import *
from math import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Entry

import numpy as np
import matplotlib.pyplot
import scipy.io.wavfile as wave
from numpy.fft import fft


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
#Etude des .mp3 et rendu graphique
rate,data = wave.read(file_path)
n = data.size
duree = 1.0*n/rate

print(rate)
print(duree)

te = 1.0/rate
t = np.zeros(n)
for k in range(n):
    t[k] = te*k
figure(figsize=(12,4))
plot(t,data)
xlabel("t (s)")
ylabel("amplitude") 
axis([0,0.1,data.min(),data.max()])
grid()

def tracerSpectre(data,rate,debut,duree):
    start = int(debut*rate)
    stop = int((debut+duree)*rate)
    spectre = np.absolute(fft(data[start:stop]))
    spectre = spectre/spectre.max()
    n = spectre.size
    freq = np.zeros(n)
    for k in range(n):
        freq[k] = 1.0/n*rate*k
    vlines(freq,[0],spectre,'r')
    xlabel('f (Hz)')
    ylabel('A')
    axis([0,0.5*rate,0,1])
    grid()
			

figure(figsize=(12,4))
tracerSpectre(data,rate,0.0,0.5)
axis([0,5000,0,1])


			
