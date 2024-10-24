n=input('Prevod u srpski(srp) ili sifrovano(sif)? (za kraj razgovora=> "kraj") : ')
recnik_sifra = {'o':'1','e':'2','r':'3','m':'4','a':'5','n':'6','i':'7','k':'8','u':'9','s':'0',' ':'$','t':']','j':'[','d':';','l':')','v':'!','p':'|','z':'&','g':'%','b':'('}
recnik_srpski = {'1':'o','2':'e','3':'r','4':'m','5':'a','6':'n','7':'i','8':'k','9':'u','0':'s','$':' ',']':'t','[':'j',';':'d',')':'l','!':'v','|':'p','&':'z','%':'g','(':'b'}
while n != "kraj":
    d = ''
    g1 = -1
    if n == 'sif':
        n = input('Recenica: ')
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
        print(d)
    if n == 'srp':
        n = input('Recenica: ')
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
        print(d)
    n=input("Prevod u srpski ili sifrovano? : ")
exit()
