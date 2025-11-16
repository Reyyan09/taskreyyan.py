kutuphane = []

def kitap_ekle():
    ad = input("Kitap adı: ")
    yazar = input("Yazar: ")
    yil = input("Yıl: ")

    kitap = {
        "ad": ad,
        "yazar": yazar,
        "yil": yil,
        "durum": "Müsait",
        "kullanan": None
    }
    kutuphane.append(kitap)
    print("Kitap eklendi")


def kitaplari_listele():
    if len(kutuphane) == 0:
        print("Kütüphanede kitap yok")
        return

    print("\n--- Kitaplar ---")
    for i, kitap in enumerate(kutuphane, 1):
        print(f"{i}. {kitap['ad']} - {kitap['yazar']} - {kitap['durum']}")


def kitap_ara():
    anahtar = input("Aranacak kelime: ").lower()
    bulunan = []

    for kitap in kutuphane:
        if anahtar in kitap["ad"].lower():
            bulunan.append(kitap)

    if len(bulunan) == 0:
        print("Kitap bulunamadı")
        return
    else:
        print("\n--- Bulunan Kitaplar ---")
        for kitap in bulunan:
            print(f"{kitap['ad']} - {kitap['yazar']} - {kitap['durum']}")


def kitap_odunc_ver():
    kitaplari_listele()
    if len(kutuphane) == 0:
        return

    secim = int(input("Hangi kitap (numara): ")) - 1

    if secim < 0 or secim >= len(kutuphane):
        print("Geçersiz numara")
        return

    if kutuphane[secim]["durum"] == "Dolu":
        print(f"Bu kitap alınmış Kitabı kullanan: {kutuphane[secim]['kullanan']}")
        return

    kullanici = input("Kullanıcı adı: ")
    kutuphane[secim]["durum"] = "Dolu"
    kutuphane[secim]["kullanan"] = kullanici
    print("Kitap ödünç verildi")



def kitap_iade_al():
    kullanici = input("Kullanıcı adı: ")

    for kitap in kutuphane:
        if kitap["kullanan"] == kullanici:
            kitap["durum"] = "Müsait"
            kitap["kullanan"] = None
            print(f"{kitap['ad']} iade alındı")
            return

    print("Bu kullanıcının kitabı yok")


def main():
    while True:
        print("\n=== KÜTÜPHANE SİSTEMİ ===")
        print("1) Kitap Ekle")
        print("2) Kitapları Listele")
        print("3) Kitap Ara")
        print("4) Kitap Ödünç Ver")
        print("5) Kitap İade Al")
        print("6) Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            kitaplari_listele()
        elif secim == "3":
            kitap_ara()
        elif secim == "4":
            kitap_odunc_ver()
        elif secim == "5":
            kitap_iade_al()
        elif secim == "6":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-6 arası bir sayı girin.")


if __name__ == "__main__":
    main()