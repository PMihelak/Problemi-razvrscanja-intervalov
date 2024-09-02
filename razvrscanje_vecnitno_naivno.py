def razvrscanje_vecnitno_naivno(intervali, st_niti):

    intervali.sort(key=lambda x: x[1])
    intervali_procesor = []
    tr_konec = [0] * st_niti

    stevecIntervalov = 0
    for interval in intervali:

        max_konec = -1
        indeks_max_konca = -1
        for i in range(st_niti):
            if(interval[0]>=tr_konec[i] and tr_konec[i]>max_konec):
                indeks_max_konca = i
                max_konec = tr_konec[i]

        if(indeks_max_konca != -1):
            stevecIntervalov += 1
            tr_konec[indeks_max_konca] = interval[1]

            intervali_procesor.append(indeks_max_konca+1)
        
        else:
            intervali_procesor.append(0)

    return(intervali, intervali_procesor)

if __name__ == '__main__':

    datoteka = open('vhod.txt', 'r')
    vrstice = datoteka.readlines()

    intervali = []

    st_niti = 0
    id = -1
    for vrstica in vrstice:

        if(id == -1):
            st_niti = int(vrstica)
        
        else:
            vrstica = vrstica.strip("\n").strip("(").strip(")")
            vrstica = vrstica.split(",")
            intervali.append((int(vrstica[0]), int(vrstica[1]), None, id))

        id += 1

    urejeni_intervali,intervali_procesor = razvrscanje_vecnitno_naivno(intervali,st_niti)

    for i in range(len(urejeni_intervali)):
        urejeni_intervali[i] = (urejeni_intervali[i][0], urejeni_intervali[i][1])

    st_razvrscenih = sum(x > 0 for x in intervali_procesor)
    izhod = open('izhod.txt', 'w', encoding="utf-8")
    izhod.write("število razvrščenih intervalov = " + str(st_razvrscenih) + "\nUrejeni intervali po koncih: " + ", ".join(str(x) for x in urejeni_intervali) + "\nRazvrstitev intervalov: " + str(intervali_procesor))