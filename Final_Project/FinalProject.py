class Yemek():
    def __init__(self, name,baharat,yag,su,tuz,pisme_suresi):
        self.name=name
        self.baharat=baharat
        self.yag=yag
        self.su=su
        self.tuz=tuz
        self.pisme_suresi=pisme_suresi
    def ekle(self,malzeme):
        print(f"\t{malzeme} eklenir.")
    def karıştır(self):
        print("\tYemek karistirilir.")
    def pisir(self):
        print(f"\t{self.name} {self.pisme_suresi} dakika pisirilir.")
    def kavur(self,malzeme):
        print(f"\t{malzeme} kavrulur.")
    def yika(self,malzeme):
        print(f"\t{malzeme} yikanir.")
    def servis(self):
         print(f"{self.name} servise hazır. Afiyet olsun!")

class MercimekCorbasi(Yemek):
    def __init__(self, name,baharat,yag,su,tuz,pisme_suresi,mercimek,un,salca):
        super().__init__(name,baharat,yag,su,tuz,pisme_suresi)
        self.mercimek=mercimek
        self.un=un
        self.salca=salca
    def suz(self):
        print(f"\t{self.name} suzulur.")
class KuruFasulye(Yemek):
    def __init__(self, name,baharat,yag,su,tuz,pisme_suresi,fasulye,sogan,biber,salca):
        super().__init__(name,baharat,yag,su,tuz,pisme_suresi)
        self.fasulye=fasulye
        self.sogan=sogan
        self.biber=biber
        self.salca=salca
    def hasla(self):
        print(f"\t{self.fasulye} haslanir.")    
class Pilav(Yemek):
    def __init__(self, name, baharat, yag, su, tuz,pisme_suresi,pirinc):
        super().__init__(name, baharat, yag, su, tuz,pisme_suresi)
        self.pirinc=pirinc
    def demleme(self):
        print(f"\t{self.name} demlenir.")


print("           Asli'nin Tarif Defteri        ")
print()
while True:
    print("Yemekler:")
    print("1-Mercimek Corbasi")
    print("2-Kuru Fasulye")
    print("3-Pilav")
    while True:
        secim=int(input("Ogrenmek istediginiz tarifi seciniz: "))
        if(secim<=0 or secim>3):
            print("Lütfen gecerli bir tarif numarasi giriniz.")
        else:
            break


    if(secim==1):
        print("------Mercimek Corbasi Tarifi------")
        yemek=MercimekCorbasi("Mercimek corbasi","baharat","yag","su","tuz",15,"mercimek","un","salca")
        yemek.yika("Mercimek")
        yemek.ekle("Yag")
        yemek.ekle("Un")
        yemek.kavur("Un")
        yemek.ekle("Salca")
        yemek.karıştır()
        yemek.ekle("Tuz")
        yemek.ekle("Baharat")
        yemek.ekle("Su")
        yemek.pisir()
        yemek.suz()
        yemek.servis()
    elif(secim==2):
        print("------Kuru Fasulye Tarifi------")
        yemek1=KuruFasulye("Kuru Fasulye","baharat","yag","su","tuz",40,"fasulye","sogan","biber","salca")
        yemek1.yika("Fasulye")
        yemek1.hasla()
        yemek1.ekle("Yag")
        yemek1.ekle("Sogan")
        yemek1.ekle("biber")
        yemek1.kavur("Biber ve sogan")
        yemek1.ekle("Domates")
        yemek1.karıştır()
        yemek1.ekle("Salca")
        yemek1.kavur("Salca")
        yemek1.ekle("su")
        yemek1.ekle("Tuz")
        yemek1.ekle("Baharat")
        yemek1.pisir()
        yemek1.servis()
    elif(secim==3):
        print("------Pirinc Pilavi Tarifi------")
        yemek2=Pilav("Pirinc Pilavi","baharat","yag","su","tuz",10,"pirinc")
        yemek2.yika("Pirinc")
        yemek2.ekle("Yag")
        yemek2.ekle("Pirinc")
        yemek2.kavur("Pirinc")
        yemek2.ekle("tuz")
        yemek2.ekle("Baharat")
        yemek2.ekle("Su")
        yemek2.karıştır()
        yemek2.pisir()
        yemek2.demleme()
        yemek2.servis()
    devam=input("\nBaska bir tarifi ogrenmek ister misiniz?(e/h):")
    if(devam=="h" or devam=="H"):
        break
    else:continue
