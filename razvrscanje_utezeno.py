from bisect import bisect_right as br

def razvrscanje_utezeno(intervali):

    intervali.insert(0, (0,0,0,-1))
    intervali.sort(key=lambda x: x[1]) 
    izbrani_intervali = []

    p = [0] * len(intervali)
    for i in range (len(intervali)):
        p[i] = br(intervali,intervali[i][0],key=lambda i: i[1])-1

    m = [0] * len(intervali)
    for i in range (1,len(intervali)):
        m[i] = max(intervali[i][2] + m[p[i]], m[i - 1])

    vsota_utezi = 0
    id = len(intervali) - 1
    while(id != 0):

        if(intervali[id][2] + m[p[id]] >= m[id - 1]):

            vsota_utezi += intervali[id][2]
            izbrani_intervali.append(intervali[id])
            id = p[id]

        else:
            id -= 1

    return vsota_utezi, izbrani_intervali
    
if __name__ == '__main__':

    datoteka = open('vhod.txt', 'r')
    vrstice = datoteka.readlines()

    intervali = []

    id = 0
    for vrstica in vrstice:

        vrstica = vrstica.strip("\n").strip("(").strip(")")
        vrstica = vrstica.split(",")
        
        intervali.append((int(vrstica[0]), int(vrstica[1]), int(vrstica[2]), id))
        id += 1

    vsota_utezi,izbrani_intervali = razvrscanje_utezeno(intervali)

    for i in range(len(izbrani_intervali)):
        izbrani_intervali[i] = (izbrani_intervali[i][0], izbrani_intervali[i][1], izbrani_intervali[i][2])

    izhod = open('izhod.txt', 'w', encoding="utf-8")
    izhod.write("Število razvrščenih intervalov = " + str(len(izbrani_intervali)) + "\nMaksimalna vsota uteži = " + str(vsota_utezi) + "\nIzbrani intervali: " + ", ".join(str(x) for x in izbrani_intervali))

