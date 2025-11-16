def sayi_liste(en_buyuk, en_kucuk):
    if len(en_buyuk, en_kucuk) == 0:
        for en_buyuk in range(0, en_buyuk):
            if en_buyuk > en_kucuk:
                return en_buyuk
            elif en_kucuk < 0:
                return en_kucuk
            else:
                return None
        for en_kucuk in range(0, en_kucuk):
            if en_buyuk > en_kucuk:
                return en_buyuk
            elif en_kucuk < 0:
                return en_kucuk
            else:
                return None


def en_buyuk_ve_kucuk(sayilar):
    for i in sayilar:
        if i >= 0:
            return kucuk
        else:
            return buyuk
    en_buyuk = sayilar[0]
    en_kucuk = sayilar[0]
    return en_buyuk, en_kucuk
liste = [10, 20, 30, 40]
buyuk, kucuk = en_buyuk_ve_kucuk(liste)

print(buyuk, kucuk)
