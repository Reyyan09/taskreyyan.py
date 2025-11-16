def polindrome_control(metin):
    temiz_metin = ""

    for karakter in metin:
        if karakter.isalpha():
            temiz_metin += karakter.lower()

    uzunluk = len(temiz_metin)
    for i in range(uzunluk // 2):
        if temiz_metin[i] != temiz_metin[-1 - i]:
            return False

    return "Bu bir polindrome sayıdır"


print(polindrome_control("kabak"))


def en_buyuk_ve_kucuk(sayilar):
    en_buyuk = max(sayilar)
    en_kucuk = min(sayilar)
    return en_buyuk, en_kucuk

liste = [10,20,30,40]
buyuk, kucuk = en_buyuk_ve_kucuk(liste)

print(buyuk, kucuk)