class UcusProgrami():

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.varis = varis
        self.sure = sure
        self.kalkis = kalkis
        self.yolcu = yolcu
        self.kapasite = kapasite

    def anons_yap(self):
        return "{} sefer sayılı {}-{} uçuşumuz 928dk sürecektir".format(self.kod, self.varis, self.sure, self.kalkis)

    def koltuk_sayisi(self,bilet_adedi=1):
        return "{} uçuşunda toplam {} koltuk bulunmaktadır".format(self.kod, self.koltuk_sayisi)
    def bilet_satişi(self):
        if self.yolcu + bilet_adedi <= self.kapasite:
           self.yolcu += bilet_adedi
           self.koltuk_sayisi_güncelleme()
            return "{} adet bilet satılmiştır kalan koltuk sayısı {}".format(bilet_adedi, self.koltuk_sayisi_güncelleme())
            else:
          print("işlem gerçekleştirilemedi")

    def bilet_adedi(self,bilet_adedi):
        self.yolcu >= bilet_adedi
        self.yolcu -= bilet_adedi
        self.koltuk_sayisi_güncelleme
        print("{} iptal bilet adedi {}".format(bilet_adedi,self.yolcu))

        ucus3.koltuk_sayisi()


ucus3 = UcusProgrami("tk127", "ank", "lon", "90", "120", "60")
