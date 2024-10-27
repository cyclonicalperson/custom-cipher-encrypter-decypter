# Za kompajliranje .exe pokreni u terminalu: pyinstaller coderdecoder.spec

import tkinter as tk
from tkinter import ttk
import os
import sys
import pyperclip

# Napravi prozor aplikacije
window = tk.Tk()
window.title('Coder/Decoder')

# Duzina i sirina prozora
window_width = 300
window_height = 90

# Uzmi velicine trenutnog ekrana
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Nadji srediste ekrana
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Postavi velicinu prozora na sredinu ekrana
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Fiksiraj minimalnu velicinu prozora
min_width = 300
min_height = 90
window.minsize(min_width, min_height)

# Postavi ikonu prozora
icon = "Typewriter.ico"
if not hasattr(sys, "frozen"):
    icon = os.path.join(os.path.dirname(__file__), icon)
else:
    icon = os.path.join(sys.prefix, icon)
window.iconbitmap(default=icon)

# Namesti kolone prozora za njegove elemente
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

# Dark mode styling
window.configure(bg='#2E2E2E')  # Background color
padding = {'padx': 3, 'pady': 3}

# Oznaka za textbox
label = ttk.Label(window, text='Unos teksta:', background='#2E2E2E', foreground='white')
label.grid(column=0, row=1, **padding)

# Textbox za unos
name_entry = ttk.Entry(window, style='Dark.TEntry')
name_entry.grid(column=1, row=1, **padding)
name_entry.focus()

# Radio dugmici za izbor dekodera ili kodera
selected_mode = tk.StringVar()  # izabrano dugme
r1 = ttk.Radiobutton(window, text='Encoding', value='1', variable=selected_mode, command=lambda: name_entry.focus(),
                     style='Dark.TRadiobutton')
r2 = ttk.Radiobutton(window, text='Decoding', value='2', variable=selected_mode, command=lambda: name_entry.focus(),
                     style='Dark.TRadiobutton')
selected_mode.set('1')  # Defaultno izabrano radio dugme (encoding)
r1.grid(column=0, row=0, **padding)
r2.grid(column=1, row=0, **padding)


# Algoritam za kodiranje/dekodiranje
def translate():
    unos = name_entry.get()  # Recenica za prevod

    # Recnici sa siframa za koder/dekoder
    recnik_sifra = {
        'A': '`', 'B': '-', 'C': '_', 'D': '+', 'E': '=', 'F': '[',
        'G': ']', 'H': '{', 'I': '}', 'J': '|', 'K': ';', 'L': ':',
        'M': '"', 'N': '/', 'O': '?', 'P': '.', 'Q': '>', 'R': ',',
        'S': '<', 'T': '!', 'U': '@', 'V': '#', 'W': '$', 'X': '%',
        'Y': '^', 'Z': '&', 'a': '*', 'b': '(', 'c': ')', 'd': '€',
        'e': '£', 'f': '¥', 'g': '¢', 'h': '₹', 'i': '₩', 'j': '₱',
        'k': '฿', 'l': '₫', 'm': '₪', 'n': 'μ', 'o': 'ψ', 'p': '∙',
        'q': '°', 'r': '⁃', 's': '∞', 't': '¶', 'u': '±', 'v': '¬',
        'w': '×', 'x': '¡', 'y': '÷', 'z': 'þ',
    }
    recnik_srpski = {
        '`': 'A', '-': 'B', '_': 'C', '+': 'D', '=': 'E', '[': 'F',
        ']': 'G', '{': 'H', '}': 'I', '|': 'J', ';': 'K', ':': 'L',
        '"': 'M', '/': 'N', '?': 'O', '.': 'P', '>': 'Q', ',': 'R',
        '<': 'S', '!': 'T', '@': 'U', '#': 'V', '$': 'W', '%': 'X',
        '^': 'Y', '&': 'Z', '*': 'a', '(': 'b', ')': 'c', '€': 'd',
        '£': 'e', '¥': 'f', '¢': 'g', '₹': 'h', '₩': 'i', '₱': 'j',
        '฿': 'k', '₫': 'l', '₪': 'm', 'μ': 'n', 'ψ': 'o', '∙': 'p',
        '°': 'q', '⁃': 'r', '∞': 's', '¶': 't', '±': 'u', '¬': 'v',
        '×': 'w', '¡': 'x', '÷': 'y', 'þ': 'z'
    }

    recenica = ''

    if selected_mode.get() == '1':  # Enkodiranje
        # Prevod recenice u sifru
        for i in range(0, len(unos)):
            slovo = unos[i]
            if slovo in recnik_sifra:
                recenica += recnik_sifra[slovo]
            else:
                recenica += slovo

        # Obrtanje recenice
        recenica_pom = list(recenica)
        for i in range(0, len(recenica_pom) // 2):
            recenica_pom[i], recenica_pom[-(i + 1)] = recenica_pom[-(i + 1)], recenica_pom[i]

        for i in range(0, len(recenica_pom) // 3):
            recenica_pom[i], recenica_pom[-(i + 1)] = recenica_pom[-(i + 1)], recenica_pom[i]

        # Vracanje recenice
        recenica = ''
        for i in range(0, len(recenica_pom)):
            recenica += recenica_pom[i]
        window.output_label.config(text=recenica)  # Stampanje recenice

        #Resizovanje prozora kako bi stala recenica na prozor
        global window_height
        height = window.output_label.winfo_height()
        window_height = 90 + height
        window.geometry(f'{window_width}x{window_height}')

    if selected_mode.get() == '2':  # Dekodiranje
        # Prevod sifre u srpski
        for i in range(0, len(unos)):
            slovo = unos[i]
            if slovo in recnik_srpski:
                recenica += recnik_srpski[slovo]
            else:
                recenica += slovo

        # Obrtanje slova
        recenica_pom = list(recenica)
        for i in range(0, len(recenica_pom) // 3):
            recenica_pom[i], recenica_pom[-(i + 1)] = recenica_pom[-(i + 1)], recenica_pom[i]

        for i in range(0, len(recenica_pom) // 2):
            recenica_pom[i], recenica_pom[-(i + 1)] = recenica_pom[-(i + 1)], recenica_pom[i]

        # Vracanje recenice
        recenica = ''
        for i in range(0, len(recenica_pom)):
            recenica += recenica_pom[i]
        window.output_label.config(text=recenica)  # Stampanje recenice


# Dugme za pokretanje
submit_button = ttk.Button(window, text='Translate', command=translate, style='Dark.TButton')
submit_button.grid(column=2, row=1, **padding)

# Izlaz prevoda
window.output_label = ttk.Label(window, wraplength=120, background='#2E2E2E', foreground='white')
window.output_label.grid(column=1, row=2, **padding)


def copy():
    text = window.output_label.cget('text')  # Fetchovanje teksta
    pyperclip.copy(text)  # Kopiranje teksta u clipboard
    copy_label = ttk.Label(window, text='Copied!', background='#2E2E2E',
                           foreground='#44a830')  # Potvrda uspesnog kopiranja
    copy_label.grid(column=0, row=2, **padding)
    window.after(2000, lambda: copy_label.config(text=''))  # Ocisti potvrdu nakon 2 sekunde (warning nije problem)


# Dugme za kopiranje prevedene recenice
copy_button = ttk.Button(window, text='Copy', command=copy, style='Dark.TButton')
copy_button.grid(column=2, row=2, **padding)

# Stilizovanje GUI-a
window.style = ttk.Style()
window.style.configure('Dark.TLabel', background='#2E2E2E', foreground='white')  # Label text
window.style.configure('Dark.TEntry', fieldbackground='#333333', foreground='black')  # Darker entry field background
window.style.configure('Dark.TRadiobutton', background='#2E2E2E', foreground='white')  # Radio button color
window.style.configure('Dark.TButton', background='#4D4D4D', foreground='black', borderwidth = 0)  # Button color
window.style.map('Dark.TButton', background=[('active', '#5A5A5A'), ('pressed', '#666666')])  # Button hover and press colors

# Pokreni prozor
window.mainloop()
