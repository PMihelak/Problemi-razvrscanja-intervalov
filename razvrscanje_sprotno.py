from bisect import insort as ins

def razvrscanje_sprotno(intervali):

    intervali.sort(key=lambda x: x[0])
    urejeni = intervali

    razvrsceni = []
    nerazvrsceni = []
    razvrsceni_cas = []

    cas = urejeni[0][0]
    st_intervalov = len(urejeni)

    while(len(razvrsceni) != st_intervalov):

        while(len(urejeni) != 0 and urejeni[0][0] <= cas):

            ins(nerazvrsceni, urejeni[0], key=lambda x:(x[1],x[0]))
            urejeni.pop(0)

        if(cas >= nerazvrsceni[0][1]):
        
            razvrsceni.append(nerazvrsceni[0])
            razvrsceni_cas.append((cas, nerazvrsceni[0][1] + cas))
            cas += nerazvrsceni[0][1]
            nerazvrsceni.pop(0)

        elif(len(urejeni) != 0):
            cas = min(nerazvrsceni[0][1], urejeni[0][0])

    return razvrsceni_cas

if __name__ == '__main__':

    datoteka = open('vhod.txt', 'r')
    vrstice = datoteka.readlines()

    intervali = []

    id = 0
    for vrstica in vrstice:

        vrstica = vrstica.strip("\n")
        vrstica = vrstica.split(",")
        
        intervali.append((int(vrstica[0]), int(vrstica[1]), None, id))
        id += 1

    razvrsceni = razvrscanje_sprotno(intervali)
    izhod = open('izhod.txt', 'w', encoding="utf-8")
    izhod.write("Razvrščeni intervali: " + ", ".join(str(x) for x in razvrsceni))