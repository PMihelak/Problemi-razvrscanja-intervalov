def razvrscanje_naivno(intervali):

    izbrani_intervali = []
    trenutni_konec = 0
    while(True):

        najboljsi_interval = None
        min_konec = None
        for interval in intervali:

            if(interval[0] >= trenutni_konec):
                if(min_konec is None or interval[1] < min_konec):

                    min_konec = interval[1]
                    najboljsi_interval = interval
                
        if(najboljsi_interval is not None):

            trenutni_konec = najboljsi_interval[1]
            izbrani_intervali.append(najboljsi_interval)
            intervali.remove(najboljsi_interval)

        else:
            break

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

    izbrani_intervali = razvrscanje_naivno(intervali)

    for i in range(len(izbrani_intervali)):
        izbrani_intervali[i] = (izbrani_intervali[i][0], izbrani_intervali[i][1])

    izhod = open('izhod.txt', 'w', encoding="utf-8")
    izhod.write("Število razvrščenih intervalov = " + str(len(izbrani_intervali)) + "\nIzbrani intervali: " + ", ".join(str(x) for x in izbrani_intervali))