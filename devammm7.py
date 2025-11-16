def asal_liste(baslangic, bitis):
    if bitis < 2:
        return "ikiden küçük asal yol ve bitis değeri iki olmaz"

    asal_mi = [True] * (bitis + 1)
    asal_mi[0] = asal_mi[1] = False


    for i in range(2, int(bitis) ** 0.5 + 1):
        if asal_mi[i]:
            for j in range(i*i, bitis, i):
                asal_mi[j]= False

    asallar = []

    for i in range(max(2, baslangic), bitis + 1):
        if asal_mi[i]:
            asallar.append(i)

    return asallar
print(asal_liste)




