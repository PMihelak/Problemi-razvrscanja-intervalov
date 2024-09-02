# Problemi-razvrscanja-intervalov
Repozitorij vsebuje implementacije algoritmov za razvrščanje intervalov in program za merjenje njihovih časov izvajanj. 
## Datoteke
- razvrscanje_naivno.py - implementacija naivnega algoritma za razvrščanje neuteženih intervalov na enem procesorju
- razvrscanje_boljse.py - implementacija boljšega algoritma za razvrščanje neuteženih intervalov na enem procesorju
- razvrscanje_utezeno.py - implementacija algoritma za razvrščanje uteženih intervalov na enem procesorju
- razvrscanje_vecnitno_naivno.py - implementacija naivnega algoritma za razvrščanje neuteženih intervalov na več procesorjih
- razvrscanje_vecnitno_boljse.py - implementacija boljšega algoritma za razvrščanje neuteženih intervalov na več procesorjih
- razvrscanje_utezeno_vecnitno.py - implementacija algoritma za razvrščanje uteženih intervalov na več procesorjih
- razvrscanje_sprotno.py - implementacija algoritma za sprotno razvrščanje neuteženih intervalov na več procesorjih
- primerjava_algoritmov.py - program za merjenje časov izvajanj implementiranih algoritmov
- vhod.txt - vhodni podatki za algoritme
- izhod.txt - izpis rezultatov
## Vhodni podatki
### Razvrščanje neuteženih intervalov na enem procesorju
V vsaki vrstici je podan en interval oblike (x,y), kjer je x začetek intervala, y pa konec.  
- programi, ki sprejmejo ta vhod: razvrscanje_naivno.py, razvrscanje_boljse.py
- primer vhoda:
  
    (0,5)  
    (6,10)  
    (2,3)  
    (5,8)  
    (1,7)  
### Razvrščanje uteženih intervalov na enem procesorju
V vsaki vrstici je podan en interval oblike (x,y,z), kjer je x začetek intervala, y njegov konec, z pa utež intervala.  
- programi, ki sprejmejo ta vhod: razvrscanje_utezeno.py
- primer vhoda:
  
    (0,2,2)  
    (3,5,2)  
    (6,8,6)  
    (1,3,4)  
    (4,5,3) 
### Razvrščanje neuteženih intervalov na več procesorjih
V prvi vrstici je podano število procesorjev, v vseh naslednjih pa so intervali oblike (x,y), kjer je x začetek intervala, y pa konec.
- programi, ki sprejmejo ta vhod: razvrscanje_vecnitno_naivno.py, razvrscanje_vecnitno_boljse.py
- primer vhoda:

    3  
    (3,5)  
    (2,8)  
    (2,5)  
    (8,9)  
    (3,7)    
### Razvrščanje uteženih intervalov na več procesorjih
V prvi vrstici je podano število procesorjev, v vseh naslednjih pa so intervali oblike (x,y,z), kjer je x začetek intervala, y njegov konec, z pa utež intervala.
- programi, ki sprejmejo ta vhod: razvrscanje_utezeno_vecnitno.py
- primer vhoda:
  
    5  
    (0,5,7)  
    (6,7,8)  
    (3,9,3)  
    (5,7,2)  
    (2,4,5)  
### Sprotno razvrščanje neuteženih intervalov
Vsaka vrstica vhoda je oblike x,y. Čas prihoda intervala predstavlja x, čas procesiranja pa y.
- programi, ki sprejmejo ta vhod: razvrscanje_sprotno.py
- primer vhoda:

    1,6  
    2,5  
    4,4  
    8,2  
    6,3  
    
### Primerjava algoritmov
Program izmeri časovne zahtevnosti zgoraj navedenih algoritmov tako, da določene algoritme izvaja na naključnih vhodnih podatkih. Poljubno lahko tudi nastavimo določene parametre:
- bool_razvrscanje_naivno (boolean) - ali naj se izvedejo meritve za naivni algoritem razvrščanja neuteženih intervalov na enem procesorju
- bool_razvrscanje_boljse (boolean) - ali naj se izvedejo meritve za boljši algoritem razvrščanja neuteženih intervalov na enem procesorju
- bool_razvrscanje_utezeno (boolean) - ali naj se izvedejo meritve za razvrščanje uteženih intervalov na enem procesorju
- bool_razvrscanje_vecnitno_naivno (boolean) - ali naj se izvedejo meritve za naivni algoritem razvrščanja neuteženih intervalov na več procesorjih
- bool_razvrscanje_vecnitno_boljse (boolean) - ali naj se izvedejo meritve za boljši algoritem razvrščanja neuteženih intervalov na več procesorjih
- bool_razvrscanje_utezeno_vecnitno (boolean) - ali naj se izvedejo meritve za razvrščanje uteženih intervalov na več procesorjih
- zac_st_intervalov (int) - število generiranih intervalov, pri katerem opravimo prvo meritev
- povecanje_st_intervalov (int) - razlika med številoma intervalov med zaporednima meritvama
- zac_st_niti (int) - število procesorjev, pri katerem opravimo prvo meritev
- povecanje_st_niti (int) - razlika med številoma procesorjev med zaporednima meritvama
- st_meritev (int) - število različnih velikosti vhodov, pri katerih opravimo meritve
- st_ponovitev (int) - število ponovitev meritve pri istih velikostih vhodov, na koncu se izračuna povprečna vrednost meritev
- min_zacetek (int) - najmanjši možni začetek, ki ga lahko imajo generirani intervali
- max_konec (int) - največji možni konec, ki ga lahko imajo generirani intervali
- max_dolzina (int) - največja dovoljena dolžina posameznega intervala
- min_utez (int) - najmanjša možna utež, ki jo lahko imajo generirani intervali
- max_utez (int) - največja možna utež, ki jo lahko imajo generirani intervali
- izracun_napake (boolean) - ali naj se izračuna povprečna relativna napaka meritev
