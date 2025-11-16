class UcusProgrami():

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu=0):
        self.kod = kod
        self.varis = varis
        self.sure = sure
        self.kalkis = kalkis
        self.yolcu = yolcu
        self.kapasite = kapasite

    def anons_yap(self):
        return "{} sefer sayılı {}-{} uçuşumuz {}dk sürecektir".format(self.kod, self.kalkis, self.varis, self.sure)

    def koltuk_durumu(self):
        bos_koltuk = self.kapasite - self.yolcu
        return "{} uçuşunda toplam {} koltuk bulunmaktadır. {} koltuk dolu, {} koltuk boş.".format(
            self.kod, self.kapasite, self.yolcu, bos_koltuk)

    def bilet_satisi(self, bilet_adedi=1):
        if self.yolcu + bilet_adedi <= self.kapasite:
            self.yolcu += bilet_adedi
            kalan_koltuk = self.kapasite - self.yolcu
            return "{} adet bilet satılmıştır. Kalan koltuk sayısı: {}".format(bilet_adedi, kalan_koltuk)
        else:
            return "İşlem gerçekleştirilemedi. Yeterli boş koltuk yok."

    def bilet_iptali(self, bilet_adedi=1):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            return "{} adet bilet iptal edildi. Mevcut yolcu sayısı: {}".format(bilet_adedi, self.yolcu)
        else:
            return "İptal edilecek yeterli bilet yok."


ucus1 = UcusProgrami("tk127", "ank", "lon", "90", 180, 0)

print(ucus1.anons_yap())
print(ucus1.koltuk_durumu())
print(ucus1.bilet_satisi(50))
print(ucus1.koltuk_durumu())
print(ucus1.bilet_iptali(10))
print(ucus1.koltuk_durumu())



