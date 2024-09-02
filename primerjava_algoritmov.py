from razvrscanje_naivno import razvrscanje_naivno
from razvrscanje_boljse import razvrscanje_boljse
from razvrscanje_vecnitno_naivno import razvrscanje_vecnitno_naivno
from razvrscanje_vecnitno_boljse import razvrscanje_vecnitno_boljse
from razvrscanje_utezeno import razvrscanje_utezeno
from razvrscanje_utezeno_vecnitno import razvrscanje_utezeno_vecnitno
import math
import time
import matplotlib.pyplot
import random
import sys
import numpy as np

#nastavitve

matplotlib.rcParams.update({'font.size': 15})
sys.setrecursionlimit(100000000)

#Izberemo za katere algoritme opravljamo meritve, rezultati so nato prikazani na istem grafu
bool_razvrscanje_naivno = True
bool_razvrscanje_boljse = True
bool_razvrscanje_utezeno = False
bool_razvrscanje_vecnitno_naivno = False
bool_razvrscanje_vecnitno_boljse = False
bool_razvrscanje_utezeno_vecnitno = False

zac_st_intervalov = 10000 #število generiranih intervalov, pri katerem opravimo prvo meritev
povecanje_st_intervalov = 10000 #razlika med številoma intervalov med zaporednima meritvama

zac_st_niti = 3 #število procesorjev, pri katerem opravimo prvo meritev
povecanje_st_niti = 0 #razlika med številoma procesorjev med zaporednima meritvama

st_meritev = 10 #število različnih velikosti vhodov, pri katerih opravimo meritve
st_ponovitev = 5 #število ponovitev meritve pri istih velikostih vhodov, na koncu se izračuna povprečna vrednost meritev

min_zacetek = 0 #najmanjši možni začetek, ki ga lahko imajo generirani intervali
max_konec = 1000000000 #največji možni konec, ki ga lahko imajo generirani intervali
max_dolzina = (max_konec - min_zacetek) // 10 #največja dovoljena dolžina posameznega intervala

min_utez = 1 #najmanjša možna utež, ki jo lahko imajo generirani intervali
max_utez = 1 #največja možna utež, ki jo lahko imajo generirani intervali

izracun_napake = True #ali naj se izračuna povprečna relativna napaka meritev
if(st_ponovitev == 1):
    izracun_napake = False

#konec nastavitev

meritve_razvrscanje_naivno = []
meritve_razvrscanje_boljse = []
meritve_razvrscanje_utezeno = []
meritve_razvrscanje_vecnitno_naivno = []
meritve_razvrscanje_vecnitno_boljse = []
meritve_razvrscanje_utezeno_vecnitno = []

st_intervalov_seznam = []
st_intervalov = zac_st_intervalov
for i in range(st_meritev):
    st_intervalov_seznam.append(st_intervalov)
    st_intervalov += povecanje_st_intervalov

st_ponovitev += 10 # dodamo 10 ponovitev, ker prvih 10 pri merjenju časa ne upoštevamo

st_niti = zac_st_niti
st_niti_seznam = []
st_vhoda = 0
for i in range(len(st_intervalov_seznam)):

    st_vhoda_prvega = st_vhoda

    intervali = []
    for j in range(st_ponovitev):

        intervali.append([])

        id = 0
        for k in range(st_intervalov_seznam[i]):

            a,b = random.sample(range(min_zacetek, max_dolzina+1), 2)
            postavitev = random.randrange(min_zacetek, max_konec-max_dolzina+1)

            zac = min(a,b) + postavitev
            kon = max(a,b) + postavitev
            utez = random.randrange(min_utez,max_utez+1)

            intervali[j].append((zac,kon,id))
            id += 1

        st_vhoda += 1

    if(povecanje_st_niti > 0):
        st_niti_seznam.append(st_niti)
        st_niti += povecanje_st_niti

    meritve = []
    if(bool_razvrscanje_naivno):
        
        vsota_casov = 0
        for j in range(st_ponovitev):

            intervali_kopija = intervali.copy()

            start = time.time()
            resitev = razvrscanje_naivno(intervali_kopija[j])
            end = time.time()
            cas = end - start
            meritve.append(cas)

        meritve = meritve[10:]
        meritve_razvrscanje_naivno.append(meritve)

    meritve = []
    if(bool_razvrscanje_boljse):

        vsota_casov = 0
        for j in range(st_ponovitev):

            intervali_kopija = intervali.copy()

            start = time.time()
            resitev = razvrscanje_boljse(intervali_kopija[j])
            end = time.time()
            cas = end - start
            meritve.append(cas)
    
        meritve = meritve[10:]
        meritve_razvrscanje_boljse.append(meritve)
    
    meritve = []
    if(bool_razvrscanje_utezeno):

        vsota_casov = 0
        for j in range(st_ponovitev):

            intervali_kopija = intervali.copy()

            start = time.time()
            vsota_utezi, resitev = razvrscanje_utezeno(intervali_kopija[j])
            end = time.time()
            cas = end - start
            meritve.append(cas)

        meritve = meritve[10:]
        meritve_razvrscanje_utezeno.append(meritve)

    meritve = []
    if(bool_razvrscanje_vecnitno_naivno):

        vsota_casov = 0
        for j in range(st_ponovitev):

            intervali_kopija = intervali.copy()

            start = time.time()
            urejeni_intervali, resitev = razvrscanje_vecnitno_naivno(intervali_kopija[j], st_niti)
            end = time.time()
            cas = end - start
            meritve.append(cas)

        meritve = meritve[10:]
        meritve_razvrscanje_vecnitno_naivno.append(meritve)

    meritve = []
    if(bool_razvrscanje_vecnitno_boljse):

        vsota_casov = 0
        for j in range(st_ponovitev):

            intervali_kopija = intervali.copy()

            start = time.time()
            urejeni_intervali, resitev = razvrscanje_vecnitno_boljse(intervali_kopija[j], st_niti)
            end = time.time()
            cas = end - start
            meritve.append(cas)

        meritve = meritve[10:]
        meritve_razvrscanje_vecnitno_boljse.append(meritve)

    meritve = []
    if(bool_razvrscanje_utezeno_vecnitno):

        vsota_casov = 0
        for j in range(st_ponovitev):

            intervali_kopija = intervali.copy()

            start = time.time()
            vsota_utezi, urejeni_intervali, resitev = razvrscanje_utezeno_vecnitno(intervali_kopija[j], st_niti)
            end = time.time()
            cas = end - start
            meritve.append(cas)

        meritve = meritve[10:]
        meritve_razvrscanje_utezeno_vecnitno.append(meritve)


def izracun_povprecja(podatki):

    povprecje = [0] * len(podatki)
    for i in range(len(podatki)):
        
        povprecje[i] = (sum(podatki[i]) / len(podatki[i]))

    print("Povprečne vrednosti:", povprecje, "\n\n")
    return povprecje

def odstopanje(podatki):

    stevilo_meritev = len(podatki)
    vsota_meritev = sum(podatki)
    povprecje_meritev = vsota_meritev / stevilo_meritev

    vsota_odstopanj = 0
    for i in range(stevilo_meritev):

        vsota_odstopanj += ((podatki[i] - povprecje_meritev)**2)

    varianca = math.sqrt((1/(stevilo_meritev - 1)) * vsota_odstopanj)
    standardna_napaka = varianca / math.sqrt(stevilo_meritev)
    abs_napaka = 1.96 * standardna_napaka

    if(povprecje_meritev != 0):
        rel_napaka = 100 * (abs_napaka / povprecje_meritev)
    
    else:
        rel_napaka = 0

    return rel_napaka

def odstopanja(podatki, vecnitno):

    print("\nŠtevilo ponovitev meritev: ", st_ponovitev - 10)
    print("Število intervalov: ", st_intervalov_seznam)

    if(vecnitno):
        print("Število procesorjev: ", st_niti_seznam)
    
    seznam_napak = []
    for i in range(len(podatki)):
        seznam_napak.append(odstopanje(podatki[i]))

    povprecje_napak = sum(seznam_napak) / len(seznam_napak)

    print("Relativne napake:", seznam_napak)
    print("Povprečje relativnih napak:", povprecje_napak, "%")

    return povprecje_napak


tekst = []

seznam_plot = st_intervalov_seznam
if(povecanje_st_niti > 0):
    seznam_plot = st_niti_seznam

if(bool_razvrscanje_naivno):

    print("Meritve za naivno razvrščanje neuteženih intervalov na 1 procesorju:")

    if(izracun_napake): 
        odstopanja(meritve_razvrscanje_naivno, False)

    matplotlib.pyplot.plot(seznam_plot, izracun_povprecja(meritve_razvrscanje_naivno))
    tekst.append('Neuteženi intervali, 1 procesor (naivni algoritem)')

if(bool_razvrscanje_boljse):

    print("Meritve za boljše razvrščanje neuteženih intervalov na 1 procesorju:")

    if(izracun_napake): 
        odstopanja(meritve_razvrscanje_boljse, False)

    matplotlib.pyplot.plot(seznam_plot, izracun_povprecja(meritve_razvrscanje_boljse))
    tekst.append('Neuteženi intervali, 1 procesor (boljši algoritem)')

if(bool_razvrscanje_utezeno):

    print("Meritve za razvrščanje uteženih intervalov na 1 procesorju:")

    if(izracun_napake): 
        odstopanja(meritve_razvrscanje_utezeno, False)

    matplotlib.pyplot.plot(seznam_plot, izracun_povprecja(meritve_razvrscanje_utezeno))
    tekst.append('Uteženi intervali, 1 procesor')

if (bool_razvrscanje_vecnitno_naivno):

    print("Meritve za naivno razvrščanje neuteženih intervalov na več procesorjih:")

    if(izracun_napake): 
        odstopanja(meritve_razvrscanje_vecnitno_naivno, True)

    matplotlib.pyplot.plot(seznam_plot, izracun_povprecja(meritve_razvrscanje_vecnitno_naivno))
    tekst.append('Neuteženi intervali, več procesorjev (naivni algoritem)')

if(bool_razvrscanje_vecnitno_boljse):

    print("Meritve za boljše razvrščanje neuteženih intervalov na več procesorjih:")

    if(izracun_napake): 
        odstopanja(meritve_razvrscanje_vecnitno_boljse, True)

    matplotlib.pyplot.plot(seznam_plot, izracun_povprecja(meritve_razvrscanje_vecnitno_boljse))
    tekst.append('Neuteženi intervali, več procesorjev (boljši algoritem)')

if(bool_razvrscanje_utezeno_vecnitno):

    print("Meritve za razvrščanje uteženih intervalov na več procesorjih:")

    if(izracun_napake): 
        odstopanja(meritve_razvrscanje_utezeno_vecnitno, True)

    matplotlib.pyplot.plot(seznam_plot, izracun_povprecja(meritve_razvrscanje_utezeno_vecnitno))
    tekst.append('Uteženi intervali, več procesorjev')


matplotlib.pyplot.legend(tekst, loc='upper left')
matplotlib.pyplot.ylabel("Čas [s]")

if(povecanje_st_intervalov > 0):
    matplotlib.pyplot.xlabel("Število intervalov")
elif(povecanje_st_niti > 0):
    matplotlib.pyplot.xlabel("Število procesorjev")

matplotlib.pyplot.show()