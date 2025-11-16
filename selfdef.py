class YemekProgrami():

    def __init__(self, kod, yemek_adi, hazirlik_suresi, fiyat, kapasite, siparis=0):
        self.kod = kod
        self.yemek_adi = yemek_adi
        self.hazirlik_suresi = hazirlik_suresi
        self.fiyat = fiyat
        self.siparis = siparis
        self.kapasite = kapasite

    def menu_anons(self):
        return "{} kodlu {} yemeği {}dk'da hazırlanacak, fiyatı {}TL'dir".format(
            self.kod, self.yemek_adi, self.hazirlik_suresi, self.fiyat)

    def stok_durumu(self):
        kalan_porsiyon = self.kapasite - self.siparis
        return "{} yemeğinde toplam {} porsiyon bulunmaktadır. {} porsiyon sipariş verildi, {} porsiyon kaldı.".format(
            self.yemek_adi, self.kapasite, self.siparis, kalan_porsiyon)

    def siparis_al(self, porsiyon_adedi=1):
        if self.siparis + porsiyon_adedi <= self.kapasite:
            self.siparis += porsiyon_adedi
            kalan_porsiyon = self.kapasite - self.siparis
            toplam_fiyat = porsiyon_adedi * self.fiyat
            return "{} porsiyon {} siparişi alındı. Toplam tutar: {}TL. Kalan porsiyon: {}".format(
                porsiyon_adedi, self.yemek_adi, toplam_fiyat, kalan_porsiyon)
        else:
            return "İşlem gerçekleştirilemedi. Yeterli stok yok."

    def siparis_iptal(self, porsiyon_adedi=1):
        if self.siparis >= porsiyon_adedi:
            self.siparis -= porsiyon_adedi
            iade_tutari = porsiyon_adedi * self.fiyat
            return "{} porsiyon sipariş iptal edildi. İade tutarı: {}TL. Mevcut sipariş sayısı: {}".format(
                porsiyon_adedi, iade_tutari, self.siparis)
        else:
            return "İptal edilecek yeterli sipariş yok."


# Test kodu
yemek1 = YemekProgrami("Y001", "Adana Kebap", 15, 45, 100, 0)

print(yemek1.menu_anons())
print(yemek1.stok_durumu())
print(yemek1.siparis_al(25))
print(yemek1.stok_durumu())
print(yemek1.siparis_iptal(5))
print(yemek1.stok_durumu())


class YemekProgrami():

    def __init__(self, ad, yemek_adet, hazirlik_suresi, fiyat, kapasite):
        self.ad = ad
        self.yemek_adet = yemek_adet
        self.hazirlik_suresi = hazirlik_suresi
        self.fiyat = fiyat
        self.kapasite = kapasite
        self.siparis_adedi = 0
        self.toplam_kazanc = 0

    def siparis_al(self, adet=1):
        if self.siparis_adedi + adet <= self.kapasite:
            self.siparis_adedi += adet
            kazanc = adet * self.fiyat  # Düzeltildi: * yerine + vardı
            self.toplam_kazanc += kazanc
            kalan_kapasite = self.kapasite - self.siparis_adedi
            return "{} den {} adet siparis alındı. Tutar: {}TL. Kalan kapasite: {}".format(
                self.ad, adet, kazanc, kalan_kapasite)
        else:
            return "Kapasite yetersiz! Maksimum {} adet sipariş alınabilir.".format(self.kapasite - self.siparis_adedi)

    def menu(self):
        return "{} yemeği {}dk'da hazırlanacak, fiyatı {}TL'dir. Mevcut kapasite: {}/{}".format(
            self.ad, self.hazirlik_suresi, self.fiyat, self.siparis_adedi,
            self.kapasite)  # Düzeltildi: format parametreleri eksikti

    def sure_guncelle(self, yeni_sure):
        eski_sure = self.hazirlik_suresi
        self.hazirlik_suresi = yeni_sure
        return "{} yemeğinin hazırlık süresi {}dk'dan {}dk'ya güncellendi".format(
            self.ad, eski_sure, yeni_sure)  # Düzeltildi: yemek_adi yerine ad

    def kazanc_raporu(self):
        return "{} yemeğinden toplam {} sipariş alındı. Toplam kazanç: {}TL".format(
            self.ad, self.siparis_adedi, self.toplam_kazanc)

    def stok_durumu(self):
        kalan = self.kapasite - self.siparis_adedi
        return "{} - Toplam kapasite: {}, Sipariş: {}, Kalan: {}".format(
            self.ad, self.kapasite, self.siparis_adedi, kalan)

    def fiyat_guncelle(self, yeni_fiyat):
        eski_fiyat = self.fiyat
        self.fiyat = yeni_fiyat
        self.fiyat_gecmisi.append(self.fiyat)
        return " {} fiyatı güncellendi! {}TL -> {}TL".format(
            self.ad, eski_fiyat, yeni_fiyat)

yemek1 = YemekProgrami("Adana Kebap", 50, 15, 45, 100)
yemek2 = YemekProgrami("Lahmacun", 80, 10, 25, 150)

print("=== MENÜ ===")
print(yemek1.menu())
print(yemek2.menu())

print("\n=== SİPARİŞLER ===")
print(yemek1.siparis_al(20))
print(yemek1.siparis_al(15))
print(yemek2.siparis_al(30))

print("\n=== GÜNCEL DURUM ===")
print(yemek1.stok_durumu())
print(yemek2.stok_durumu())

print("\n=== KAZANÇ RAPORU ===")
print(yemek1.kazanc_raporu())
print(yemek2.kazanc_raporu())

print("\n=== SÜRE GÜNCELLEMESİ ===")
print(yemek1.sure_guncelle(18))
print(yemek1.menu())