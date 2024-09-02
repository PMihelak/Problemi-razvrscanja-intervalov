def razvrscanje_boljse(intervali):

    izbrani_intervali = []
    intervali.sort(key=lambda x: x[1])
    urejeni_intervali = intervali

    stevecIntervalov = 0
    trenutniKonec = 0
    for interval in urejeni_intervali:

        if(interval[0] >= trenutniKonec):

            stevecIntervalov += 1
            trenutniKonec = interval[1]
            izbrani_intervali.append(interval)

    return izbrani_intervali

if __name__ == '__main__':

    datoteka = open('vhod.txt', 'r')
    vrstice = datoteka.readlines()

    intervali = []

    id = 0
    for vrstica in vrstice:

        vrstica = vrstica.strip("\n").strip("(").strip(")")
        vrstica = vrstica.split(",")
        
        intervali.append((int(vrstica[0]), int(vrstica[1]), None, id))
        id += 1

    izbrani_intervali = razvrscanje_boljse(intervali)

    for i in range(len(izbrani_intervali)):
        izbrani_intervali[i] = (izbrani_intervali[i][0], izbrani_intervali[i][1])

    izhod = open('izhod.txt', 'w', encoding="utf-8")
    izhod.write("Število razvrščenih intervalov = " + str(len(izbrani_intervali)) + "\nIzbrani intervali: " + ", ".join(str(x) for x in izbrani_intervali))
