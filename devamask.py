# Kütüphane Takip Sistemi
# Tüm kitapları saklayacak liste
kutuphane = []

# Kitap ID'si için sayaç
kitap_id_sayac = 1


def kitap_ekle():
    """Yeni kitap ekler"""
    global kitap_id_sayac

    print("\n--- Kitap Ekleme ---")
    try:
        ad = input("Kitap adı: ").strip()
        if not ad:
            print("❌ Kitap adı boş olamaz!")
            return

        yazar = input("Yazar adı: ").strip()
        if not yazar:
            print("❌ Yazar adı boş olamaz!")
            return

        yil = input("Yayın yılı: ").strip()
        if not yil.isdigit():
            print("❌ Yıl sayı olmalıdır!")
            return

        # Yeni kitap sözlüğü oluştur
        yeni_kitap = {
            "id": kitap_id_sayac,
            "ad": ad,
            "yazar": yazar,
            "yil": int(yil),
            "durum": "Müsait",
            "odunc_alan": None
        }

        kutuphane.append(yeni_kitap)
        kitap_id_sayac += 1
        print(f"✅ '{ad}' kitabı başarıyla eklendi! (ID: {yeni_kitap['id']})")

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")


def kitaplari_listele():
    """Tüm kitapları listeler"""
    print("\n--- Kütüphanedeki Kitaplar ---")

    if not kutuphane:
        print("📚 Kütüphanede henüz kitap yok.")
        return

    print(f"\n{'ID':<5} {'Kitap Adı':<30} {'Yazar':<20} {'Yıl':<6} {'Durum':<10} {'Ödünç Alan':<15}")
    print("-" * 100)

    for kitap in kutuphane:
        odunc_bilgi = kitap['odunc_alan'] if kitap['odunc_alan'] else "-"
        print(
            f"{kitap['id']:<5} {kitap['ad']:<30} {kitap['yazar']:<20} {kitap['yil']:<6} {kitap['durum']:<10} {odunc_bilgi:<15}")

    print(f"\nToplam kitap sayısı: {len(kutuphane)}")


def kitap_ara():
    """Kitap adına göre arama yapar"""
    print("\n--- Kitap Arama ---")

    if not kutuphane:
        print("📚 Kütüphanede henüz kitap yok.")
        return

    anahtar = input("Aramak istediğiniz kelime: ").strip().lower()

    if not anahtar:
        print("❌ Arama kelimesi boş olamaz!")
        return

    bulunan_kitaplar = [k for k in kutuphane if anahtar in k['ad'].lower()]

    if not bulunan_kitaplar:
        print(f"❌ '{anahtar}' kelimesini içeren kitap bulunamadı.")
        return

    print(f"\n✅ {len(bulunan_kitaplar)} adet kitap bulundu:\n")
    print(f"{'ID':<5} {'Kitap Adı':<30} {'Yazar':<20} {'Durum':<10}")
    print("-" * 70)

    for kitap in bulunan_kitaplar:
        print(f"{kitap['id']:<5} {kitap['ad']:<30} {kitap['yazar']:<20} {kitap['durum']:<10}")


def kitap_odunc_ver():
    """Kitap ödünç verir"""
    print("\n--- Kitap Ödünç Verme ---")

    if not kutuphane:
        print("📚 Kütüphanede henüz kitap yok.")
        return

    # Müsait kitapları göster
    musait_kitaplar = [k for k in kutuphane if k['durum'] == "Müsait"]

    if not musait_kitaplar:
        print("❌ Şu anda ödünç verilebilecek kitap yok.")
        return

    print("\nMüsait Kitaplar:")
    print(f"{'ID':<5} {'Kitap Adı':<30} {'Yazar':<20}")
    print("-" * 60)
    for kitap in musait_kitaplar:
        print(f"{kitap['id']:<5} {kitap['ad']:<30} {kitap['yazar']:<20}")

    try:
        kitap_id = input("\nÖdünç almak istediğiniz kitabın ID'si: ").strip()
        if not kitap_id.isdigit():
            print("❌ Geçersiz ID!")
            return

        kitap_id = int(kitap_id)

        # Kitabı bul
        kitap = None
        for k in kutuphane:
            if k['id'] == kitap_id:
                kitap = k
                break

        if not kitap:
            print("❌ Bu ID'ye sahip kitap bulunamadı!")
            return

        if kitap['durum'] == "Dolu":
            print(f"❌ Bu kitap zaten ödünç alınmış! (Ödünç alan: {kitap['odunc_alan']})")
            return

        kullanici = input("Adınız: ").strip()
        if not kullanici:
            print("❌ İsim boş olamaz!")
            return

        # Kitabı ödünç ver
        kitap['durum'] = "Dolu"
        kitap['odunc_alan'] = kullanici

        print(f"✅ '{kitap['ad']}' kitabı {kullanici} tarafından ödünç alındı.")

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")


def kitap_iade_al():
    """Kitap iade alır"""
    print("\n--- Kitap İade Alma ---")

    if not kutuphane:
        print("📚 Kütüphanede henüz kitap yok.")
        return

    # Ödünç verilmiş kitapları göster
    odunc_kitaplar = [k for k in kutuphane if k['durum'] == "Dolu"]

    if not odunc_kitaplar:
        print("❌ İade edilecek kitap yok.")
        return

    print("\nÖdünç Verilmiş Kitaplar:")
    print(f"{'ID':<5} {'Kitap Adı':<30} {'Ödünç Alan':<20}")
    print("-" * 60)
    for kitap in odunc_kitaplar:
        print(f"{kitap['id']:<5} {kitap['ad']:<30} {kitap['odunc_alan']:<20}")

    try:
        kullanici = input("\nİade eden kişinin adı: ").strip()
        if not kullanici:
            print("❌ İsim boş olamaz!")
            return

        # Kullanıcının kitaplarını bul
        kullanici_kitaplari = [k for k in kutuphane if k['odunc_alan'] and k['odunc_alan'].lower() == kullanici.lower()]

        if not kullanici_kitaplari:
            print(f"❌ {kullanici} adına kayıtlı ödünç kitap bulunamadı!")
            return

        print(f"\n{kullanici} adına kayıtlı kitaplar:")
        for i, kitap in enumerate(kullanici_kitaplari, 1):
            print(f"{i}. {kitap['ad']} (ID: {kitap['id']})")

        secim = input("\nİade edilecek kitabın numarasını seçin: ").strip()
        if not secim.isdigit() or int(secim) < 1 or int(secim) > len(kullanici_kitaplari):
            print("❌ Geçersiz seçim!")
            return

        secilen_kitap = kullanici_kitaplari[int(secim) - 1]

        # Kitabı iade al
        secilen_kitap['durum'] = "Müsait"
        secilen_kitap['odunc_alan'] = None

        print(f"✅ '{secilen_kitap['ad']}' kitabı başarıyla iade alındı!")

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")


def kitap_sil():
    """Bonus: Kitap silme özelliği"""
    print("\n--- Kitap Silme ---")

    if not kutuphane:
        print("📚 Kütüphanede henüz kitap yok.")
        return

    kitaplari_listele()

    try:
        kitap_id = input("\nSilmek istediğiniz kitabın ID'si: ").strip()
        if not kitap_id.isdigit():
            print("❌ Geçersiz ID!")
            return

        kitap_id = int(kitap_id)

        # Kitabı bul ve sil
        for i, kitap in enumerate(kutuphane):
            if kitap['id'] == kitap_id:
                onay = input(f"'{kitap['ad']}' kitabını silmek istediğinizden emin misiniz? (e/h): ").strip().lower()
                if onay == 'e':
                    kutuphane.pop(i)
                    print(f"✅ Kitap başarıyla silindi!")
                else:
                    print("❌ İşlem iptal edildi.")
                return

        print("❌ Bu ID'ye sahip kitap bulunamadı!")

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")


def menu():
    """Ana menü"""
    while True:
        print("\n" + "=" * 50)
        print("📚 KÜTÜPHANe TAKİP SİSTEMİ")
        print("=" * 50)
        print("1) Kitap Ekle")
        print("2) Kitapları Listele")
        print("3) Kitap Ara")
        print("4) Kitap Ödünç Ver")
        print("5) Kitap İade Al")
        print("6) Kitap Sil (Bonus)")
        print("7) Çıkış")
        print("=" * 50)

        secim = input("Seçiminiz (1-7): ").strip()

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
            kitap_sil()
        elif secim == "7":
            print("\n👋 Kütüphane Takip Sisteminden çıkılıyor... Güle güle!")
            break
        else:
            print("❌ Geçersiz seçim! Lütfen 1-7 arası bir sayı girin.")


# Programı başlat
if __name__ == "__main__":
    print("🎉 Kütüphane Takip Sistemine Hoş Geldiniz!")
    menu()

    # Basit Kütüphane Takip Sistemi

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
        print("Kitap eklendi!")


    def kitaplari_listele():
        if len(kutuphane) == 0:
            print("Kütüphanede kitap yok.")
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
            print("Kitap bulunamadı.")
        else:
            print("\n--- Bulunan Kitaplar ---")
            for kitap in bulunan:
                print(f"{kitap['ad']} - {kitap['yazar']} - {kitap['durum']}")


    def kitap_odunc_ver():
        kitaplari_listele()

        if len(kutuphane) == 0:
            return

        secim = int(input("Hangi kitap? (numara): ")) - 1

        if secim < 0 or secim >= len(kutuphane):
            print("Geçersiz numara!")
            return

        if kutuphane[secim]["durum"] == "Dolu":
            print("Bu kitap zaten ödünç verilmiş!")
            return

        kullanici = input("Kullanıcı adı: ")
        kutuphane[secim]["durum"] = "Dolu"
        kutuphane[secim]["kullanan"] = kullanici
        print("Kitap ödünç verildi!")


    def kitap_iade_al():
        kullanici = input("Kullanıcı adı: ")

        for kitap in kutuphane:
            if kitap["kullanan"] == kullanici:
                kitap["durum"] = "Müsait"
                kitap["kullanan"] = None
                print(f"{kitap['ad']} iade alındı!")
                return

        print("Bu kullanıcıda kitap yok.")


    def menu():
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
                print("Geçersiz seçim!")


    menu()