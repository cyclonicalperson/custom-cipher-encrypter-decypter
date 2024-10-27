#Za kompajliranje .exe pokreni u terminalu: pyinstaller coderdecoder.spec

import tkinter as tk
from tkinter import ttk
import os
import sys

# Napravi prozor aplikacije
window = tk.Tk()
window.title('Coder/Decoder')

# Duzina i sirina prozora
window_width = 400
window_height = 150

# Uzmi velicine trenutnog ekrana
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Nadji srediste ekrana
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# Postavi velicinu prozora na sredinu ekrana
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Fiksiraj minimalnu velicinu prozora
min_width = 100
min_height = 60
window.minsize(min_width, min_height)

# Postavi ikonu prozora
icon = "Typewriter.ico"
if not hasattr(sys, "frozen"):
    icon = os.path.join(os.path.dirname(__file__), icon)
else:
    icon = os.path.join(sys.prefix, icon)
window.iconbitmap(default = icon)

# Namesti kolone prozora za njegove elemente
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

padding = {'padx': 5, 'pady': 5}
# Oznaka za textbox
ttk.Label(window, text = 'Unos teksta:').grid(column = 0, row = 1, **padding)

# Radio dugmici za izbor dekodera ili kodera
selected_mode = tk.StringVar() #izabrano dugme
r1 = ttk.Radiobutton(window, text='Encoding', value='1', variable = selected_mode)
r2 = ttk.Radiobutton(window, text='Decoding', value='2', variable = selected_mode)
selected_mode.set('1')  # Defaultno izabrano radio dugme (encoding)
r1.grid(column = 0, row = 0, **padding)
r2.grid(column = 1, row = 0, **padding)

# Textbox za unos
name_entry = ttk.Entry(window)
name_entry.grid(column = 1, row = 1, **padding)
name_entry.focus()

#Algoritam za kodiranje/dekodiranje
def translate():
    unos = name_entry.get() #Recenica za prevod

    #Recnici sa siframa za koder/dekoder
    recnik_sifra = {'o':'1','e':'2','r':'3','m':'4','a':'5','n':'6','i':'7','k':'8','u':'9','s':'0',' ':'$','t':']','j':'[','d':';','l':')','v':'!','p':'|','z':'&','g':'%','b':'('}
    recnik_srpski = {'1':'o','2':'e','3':'r','4':'m','5':'a','6':'n','7':'i','8':'k','9':'u','0':'s','$':' ',']':'t','[':'j',';':'d',')':'l','!':'v','|':'p','&':'z','%':'g','(':'b'}

    recenica = ''
    i1 = -1 #Pomocni indeks za obrtanje slova
    
    if selected_mode.get() == '1': #Enkodiranje
        #Prevod recenice u sifru
        for i in range(0, len(unos)):
            slovo = unos[i]
            if slovo in recnik_sifra:
                recenica += recnik_sifra[slovo]
            else:
                recenica += slovo
        
        #Obrtanje slova
        recenica_pom = list(recenica)
        for i in range(0, (len(recenica_pom) // 2), 2):
            recenica_pom[i], recenica_pom[i1] = recenica_pom[i1], recenica_pom[i]
            i1 -= 1
        i1 =- 1
        for i in range(0, (len(recenica_pom) // 3)):
            recenica_pom[i], recenica_pom[i1] = recenica_pom[i1], recenica_pom[i]
            i1 -= 2

        #Vracanje recenice
        recenica = ''
        for i in range(0, len(recenica_pom)):
            recenica += recenica_pom[i]
        window.output_label.config(text = recenica) #Stampanje recenice
        
    if selected_mode.get() == '2': #Dekodiranje
        #Prevod sifre u srpski
        for i in range(0,len(unos)):
            slovo = unos[i]
            if slovo in recnik_srpski:
                recenica += recnik_srpski[slovo]
            else:
                recenica += slovo

        # Obrtanje slova
        recenica_pom = list(recenica)
        for i in range(0, (len(recenica_pom) // 3)):
            recenica_pom[i],recenica_pom[i1]=recenica_pom[i1],recenica_pom[i]
            i1 -= 2
        i1 =- 1
        for i in range(0, (len(recenica_pom) // 2), 2):
            recenica_pom[i],recenica_pom[i1]=recenica_pom[i1],recenica_pom[i]
            i1 -= 1

        # Vracanje recenice
        recenica = ''
        for i in range(0,len(recenica_pom)):
            recenica += recenica_pom[i]
        window.output_label.config(text = recenica) #Stampanje recenice

# Dugme za pokretanje
submit_button = ttk.Button(window, text = 'Translate', command = translate)
submit_button.grid(column = 2, row = 1, **padding)

# Izlaz prevoda
window.output_label = ttk.Label(window)
window.output_label.grid(column = 0, row = 3, columnspan = 3, **padding)

# Pokreni prozor
window.mainloop()