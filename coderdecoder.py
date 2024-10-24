import tkinter as tk
from tkinter import ttk

# Napravi prozor aplikacije
window = tk.Tk()
window.title('Coder/Decoder')

# Duzina i sirina prozora
window_width = 800
window_height = 500

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
window.iconbitmap('./Typewriter.ico')

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
    unos = name_entry.get()
    #n = input('Prevod u srpski(srp) ili sifrovano(sif)? (za kraj razgovora=> "kraj") : ')
    n = "sif"

    #Recnici sa siframa za koder/dekoder
    recnik_sifra = {'o':'1','e':'2','r':'3','m':'4','a':'5','n':'6','i':'7','k':'8','u':'9','s':'0',' ':'$','t':']','j':'[','d':';','l':')','v':'!','p':'|','z':'&','g':'%','b':'('}
    recnik_srpski = {'1':'o','2':'e','3':'r','4':'m','5':'a','6':'n','7':'i','8':'k','9':'u','0':'s','$':' ',']':'t','[':'j',';':'d',')':'l','!':'v','|':'p','&':'z','%':'g','(':'b'}

    if n == "sif": #while n != "kraj":
        d = ''
        g1 = -1
        if selected_mode.get() == '1':
            n = unos
            for i in range(0, len(n)):
                p = n[i]
                if p in recnik_sifra:
                    x = recnik_sifra[p]
                    d += x
                else:
                    d += p
            d1 = list(d)
            for g in range(0, (len(d1)//2), 2):
                d1[g],d1[g1]=d1[g1],d1[g]
                g1 -= 1
            g1 =- 1
            for g in range(0, (len(d1)//3)):
                d1[g],d1[g1]=d1[g1],d1[g]
                g1 -= 2
            d = ''
            for k in range(0, len(d1)):
                w = d1[k]
                d += w
            window.output_label.config(text = d)
        if selected_mode.get() == '2':
            n = unos
            for i in range(0,len(n)):
                p = n[i]
                if p in recnik_srpski:
                    x = recnik_srpski[p]
                    d += x
                else:
                    d += p
            d1 = list(d)
            for g in range(0,(len(d1)//3)):
                d1[g],d1[g1]=d1[g1],d1[g]
                g1 -= 2
            g1 =- 1
            for g in range(0,(len(d1)//2),2):
                d1[g],d1[g1]=d1[g1],d1[g]
                g1 -= 1
            d = ''
            for k in range(0,len(d1)):
                w = d1[k]
                d += w
            window.output_label.config(text = d)
        #n=input("Prevod u srpski ili sifrovano? : ")
    #exit()

# Dugme za pokretanje
submit_button = ttk.Button(window, text = 'Translate', command = translate)
submit_button.grid(column = 2, row = 1, **padding)

# Izlaz prevoda
window.output_label = ttk.Label(window)
window.output_label.grid(column = 0, row = 3, columnspan = 3, **padding)

# Pokreni prozor
window.mainloop()