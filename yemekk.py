class YemekProgrami():

    def __init__(self, ad, yemek_adet, hazirlik_suresi, fiyat, kapasite):
        self.ad = ad
        self.yemek_adet = yemek_adet
        self.hazirlik_suresi = hazirlik_suresi
        self.fiyat = fiyat
        self.kapasite = kapasite
        self.siparis_adedi = 0
        self.toplam_kazanc = 0
    def siparis_al(self,adet=1):
        self.siparis_adedi += adet

        kazanc = adet+ self.fiyat

        self.toplam_kazanc += kazanc

        return "{} den {} adet siparis alındı {} tl dir"
    def menu(self):
        return "{} kodlu {} yemeği {}dk'da hazırlanacak, fiyatı {}TL'dir".format(self.ad,self.hazirlik_suresi, self.fiyat)

    def sure_guncelle(self, yeni_sure):
        eski_sure = self.hazirlik_suresi
        self.hazirlik_suresi = yeni_sure
        return "{} yemeğinin hazırlık süresi {}dk'dan {}dk'ya güncellendi".format(
            self.yemek_adi, eski_sure, yeni_sure)


class YemekProgrami():

    def __init__(self, ad, yemek_adet, hazirlik_suresi, fiyat, kapasite):
        self.ad = ad
        self.yemek_adet = yemek_adet
        self.hazirlik_suresi = hazirlik_suresi
        self.fiyat = fiyat
        self.kapasite = kapasite
        self.siparis_adedi = 0
        self.toplam_kazanc = 0
        self.fiyat_gecmisi = [fiyat]  # Fiyat geçmişini tutar

    def siparis_al(self, adet=1):
        if self.siparis_adedi + adet <= self.kapasite:
            self.siparis_adedi += adet
            kazanc = adet * self.fiyat
            self.toplam_kazanc += kazanc
            kalan_kapasite = self.kapasite - self.siparis_adedi
            return "{} den {} adet siparis alındı. Tutar: {}TL. Kalan kapasite: {}".format(
                self.ad, adet, kazanc, kalan_kapasite)
        else:
            return "Kapasite yetersiz! Maksimum {} adet sipariş alınabilir.".format(self.kapasite - self.siparis_adedi)

    def menu(self):
        return "{} yemeği {}dk'da hazırlanacak, fiyatı {}TL'dir. Mevcut kapasite: {}/{}".format(
            self.ad, self.hazirlik_suresi, self.fiyat, self.siparis_adedi, self.kapasite)

    def sure_guncelle(self, yeni_sure):
        eski_sure = self.hazirlik_suresi
        self.hazirlik_suresi = yeni_sure
        return "{} yemeğinin hazırlık süresi {}dk'dan {}dk'ya güncellendi".format(
            self.ad, eski_sure, yeni_sure)

    def fiyat_artir(self, miktar):
        eski_fiyat = self.fiyat
        self.fiyat += miktar
        self.fiyat_gecmisi.append(self.fiyat)
        return " {} fiyatı {}TL artırıldı! {}TL -> {}TL".format(
            self.ad, miktar, eski_fiyat, self.fiyat)

    def fiyat_azalt(self, miktar):
        eski_fiyat = self.fiyat
        if self.fiyat - miktar > 0:
            self.fiyat -= miktar
            self.fiyat_gecmisi.append(self.fiyat)
            return " {} fiyatı {}TL azaltıldı! {}TL -> {}TL".format(
                self.ad, miktar, eski_fiyat, self.fiyat)
        else:
            return " Fiyat 0'dan küçük olamaz!"

    def fiyat_guncelle(self, yeni_fiyat):
        eski_fiyat = self.fiyat
        self.fiyat = yeni_fiyat
        self.fiyat_gecmisi.append(self.fiyat)
        return "🔄 {} fiyatı güncellendi! {}TL -> {}TL".format(
            self.ad, eski_fiyat, yeni_fiyat)

    def hizli_fiyat_degisimi(self, artis_orani):
        eski_fiyat = self.fiyat
        artis_miktari = self.fiyat * (artis_orani / 100)
        self.fiyat += artis_miktari
        self.fiyat = round(self.fiyat, 2)
        self.fiyat_gecmisi.append(self.fiyat)
        return " {} fiyatında %{} artış! {}TL -> {}TL ({}TL artış)".format(
            self.ad, artis_orani, eski_fiyat, self.fiyat, round(artis_miktari, 2))

    def fiyat_gecmisini_goster(self):
        fiyat_str = " -> ".join([str(f) + "TL" for f in self.fiyat_gecmisi])
        return "📊 {} fiyat geçmişi: {}".format(self.ad, fiyat_str)

    def kazanc_raporu(self):
        return "{} yemeğinden toplam {} sipariş alındı. Toplam kazanç: {}TL".format(
            self.ad, self.siparis_adedi, self.toplam_kazanc)

print("=== HIZLI FİYAT DEĞİŞİMİ DEMOSİ ===\n")

yemek1 = YemekProgrami("Adana Kebap", 50, 15, 45, 100)
yemek2 = YemekProgrami("Lahmacun", 80, 10, 25, 150)

print("🍽️ Başlangıç Fiyatları:")
print(yemek1.menu())
print(yemek2.menu())

print("\n" + "=" * 50)
print("⚡ HIZLI FİYAT DEĞİŞİMLERİ")
print("=" * 50)


print(yemek1.hizli_fiyat_degisimi(15))  # %15 artış
print(yemek2.hizli_fiyat_degisimi(20))  # %20 artış


print(yemek1.fiyat_artir(8))  # 8TL artır
print(yemek2.fiyat_azalt(3))  # 3TL azalt


print(yemek1.acil_indirim(10))  # %10 indirim
print(yemek2.acil_indirim(25))  # %25 indirim


print(yemek1.fiyat_guncelle(60))

print("\n" + "=" * 50)
print("📊 FİYAT GEÇMİŞİ")
print("=" * 50)
print(yemek1.fiyat_gecmisini_goster())
print(yemek2.fiyat_gecmisini_goster())

print("\n" + "=" * 50)
print("📋 GÜNCEL DURUM")
print("=" * 50)
print(yemek1.menu())
print(yemek2.menu())





































