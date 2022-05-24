ozgur_eserler=[""]
def ozgurr () :
   while True :
    print("Robot olmadiginizi anlamamiz icin sifreye 1 giriniz")
    giris=input("Sifre ??  :")
    if giris==1:
        isim=raw_input("Isminizi giriniz : ")
        print(" Hosgeldiniz  Sayin {0}  ").format(isim)
        print(" Kutuphanemize seref verdiniz ")
        print(" Yapmak istediginiz islem kitap eklemek ise bosluga 7 giriniz ")
        print(" Yapmak istediginiz islem kitap silmek ise bosluga  17 giriniz ")
        islem=input("Yapmak istenilen islem kodu :")
        if islem==7:
            kitap=raw_input("Eklemek istediginiz kitabi yaziniz : ")
            if kitap in ozgur_eserler:
                print("Zaten olan bir kitabi sectiniz")
                kitap=raw_input("Eklemek istediginiz kitabi yaziniz :")
                ozgur_eserler.append(kitap)
                print("Yeni kitap listeniz {0} : ").format(ozgur_eserler)
                print("Basa donup yeni islem yapmak istiyorsaniz 12 i tuslayin , Bitirmek icin 13 u tuslayin")
                devamke=input("Tamam mi  , Devam mi : ")
                if devamke==13:
                    break
            else:
                ozgur_eserler.append(kitap)
                print("Yeni kitap listeniz {0} : ").format(ozgur_eserler)
                print("Basa donup yeni islem yapmak istiyorsaniz 12 i tuslayin , Bitirmek icin 13 u tuslayin")
                devamke = input("Tamam mi  , Devam mi : ")
                if devamke == 13:
                    break
        elif islem==17:
            kitap=raw_input("Silmek istediginiz kitabi yaziniz : ")
            if kitap in ozgur_eserler:
                ozgur_eserler.remove(kitap)
                print("Kitap basariyla silinmistir ")
                print("Yeni kitap listeniz {0}").format(ozgur_eserler)
                print("Basa donup yeni islem yapmak istiyorsaniz 12 i tuslayin , Bitirmek icin 13 u tuslayin ")
                devamke = input("Tamam mi  , Devam mi : ")
                if devamke == 13:
                    break
            else :
                print("Boyle bir kitap bulunmamaktadir!!")
                print("Basa donup yeni islem yapmak istiyorsaniz 12 i tuslayin , Bitirmek icin 13 u tuslayin ")
                devamke = input("Tamam mi  , Devam mi : ")
                if devamke == 13:
                    break

    else:
        print("Robot degilseniz lutfen  basa donup 1 i tuslayiniz")
print(ozgurr())


