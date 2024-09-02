import bintrees

def razvrscanje_vecnitno_boljse(intervali, st_niti):

    intervali.sort(key=lambda x: x[1])
    intervali_procesor = []
    tr_konci = bintrees.AVLTree()
    tr_konci.insert((0,1),None)

    stevecIntervalov = 0
    for interval in intervali:

        try:
            indeks = tr_konci.floor_key((interval[0],st_niti))
            indeks_max_konca = indeks[1]
            napaka = False

        except:
            napaka = True

        if(not napaka):
            stevecIntervalov += 1
            tr_konci.remove(indeks)
            tr_konci.insert((interval[1],indeks_max_konca), None)
            intervali_procesor.append(indeks_max_konca)

        else:
            intervali_procesor.append(0)

        st_zasedenih = len(tr_konci)
        if(st_zasedenih < st_niti):
            tr_konci.insert((0,st_zasedenih+1),None)

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

    urejeni_intervali,intervali_procesor = razvrscanje_vecnitno_boljse(intervali,st_niti)

    for i in range(len(urejeni_intervali)):
        urejeni_intervali[i] = (urejeni_intervali[i][0], urejeni_intervali[i][1])

    st_razvrscenih = sum(x > 0 for x in intervali_procesor)
    izhod = open('izhod.txt', 'w', encoding="utf-8")
    izhod.write("število razvrščenih intervalov = " + str(st_razvrscenih) + "\nUrejeni intervali po koncih: " + ", ".join(str(x) for x in urejeni_intervali) + "\nRazvrstitev intervalov: " + str(intervali_procesor))