import bintrees

def rek(intervali, maska_id, vsota_utezi, tr_konci, st_niti):

    global max_vsota_utezi
    global max_maska
    global intervali_maska

    if(vsota_utezi > max_vsota_utezi):
        max_vsota_utezi = vsota_utezi
        max_maska = intervali_maska.copy()

    if(maska_id >= len(intervali)):
        return
    
    interval = intervali[maska_id]

    try:
        indeks = tr_konci.floor_key((interval[0],st_niti))
        indeks_max_konca = indeks[1]
        napaka = False

    except:
        napaka = True

    if(not napaka):

        tr_konci2 = tr_konci.copy()
        tr_konci2.remove(indeks)
        tr_konci2.insert((interval[1],indeks_max_konca), None)

        intervali_maska[maska_id] = indeks_max_konca
        nova_vsota = vsota_utezi+intervali[maska_id][2]

        st_zasedenih = len(tr_konci)
        if(st_zasedenih < st_niti):
            tr_konci2.insert((0,st_zasedenih+1),None)

        rek(intervali, maska_id+1, nova_vsota, tr_konci2, st_niti)
        intervali_maska[maska_id] = 0

    rek(intervali, maska_id+1, vsota_utezi, tr_konci, st_niti)

def razvrscanje_utezeno_vecnitno(intervali, st_niti):

    global max_vsota_utezi
    global max_maska
    global intervali_maska

    intervali.sort(key=lambda x: x[1])     
    intervali_maska = [0] * len(intervali)
    max_vsota_utezi = 0
    max_maska = []

    trenutni_konci = bintrees.AVLTree()
    trenutni_konci.insert((0,1),None)

    rek(intervali,0,0,trenutni_konci, st_niti)
    
    return(max_vsota_utezi, intervali, max_maska)

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
            intervali.append((int(vrstica[0]), int(vrstica[1]), int(vrstica[2]), id))

        id += 1

    vsota_utezi, urejeni_intervali, intervali_procesor = razvrscanje_utezeno_vecnitno(intervali, st_niti)

    for i in range(len(urejeni_intervali)):
        urejeni_intervali[i] = (urejeni_intervali[i][0], urejeni_intervali[i][1], urejeni_intervali[i][2])

    st_razvrscenih = sum(x > 0 for x in intervali_procesor)
    izhod = open('izhod.txt', 'w', encoding="utf-8")
    izhod.write("število razvrščenih intervalov = " + str(st_razvrscenih) + "\nMaksimalna vsota uteži = " + str(vsota_utezi) +  "\nUrejeni intervali po koncih: " + ", ".join(str(x) for x in urejeni_intervali) + "\nRazvrstitev intervalov: " + str(intervali_procesor))