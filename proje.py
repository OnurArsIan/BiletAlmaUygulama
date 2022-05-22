import datetime
import sqlite3
from tkinter.tix import LabelEntry

def hellouser():
    h="Biletgo'ya hoş geldiniz"
    hnew=h.center(40,'*')
    print(hnew)
    saatgun = datetime.datetime.now()
    tarih = datetime.datetime.strftime(saatgun, '%c')
    info=f"{tarih}".center(40,'*')
    print(info)

def usersqlite():
    user=[]
    print("-Bilet Alma Menüsü-")
    ad=input("Adınızı giriniz:")
    soyad=input("soyadınızı giriniz:")
    tc=input("Tc no giriniz:")
    numara=input("telefon numarası giriniz")
    user.append((ad,soyad,tc,numara))
    with sqlite3.connect('vt.sqlite') as vt:
        im=vt.cursor()
        im.execute("""CREATE TABLE IF NOT EXISTS users(ad,soyad,tc,numara)""")
        for x in user:
            im.execute("""INSERT INTO users VALUES (?,?,?,?)""",x)
            vt.commit() 
    print("kaydınız tamamlanmıştır.")

def biletal():
    
 
    bostarihler=["12.12.22","15.05.22","16.05.22"]
    bosrota=["ankara-izmir","istanbul-adana","izmir-ankara"]
    dolurota = []
    satılanb=0
    tarih= input("   Tarih giriniz(gg.aa.yy):")
    rotas=input("   rota giriniz(baslangıc-bitis):")
    print("\n \n")
    for x in range(1):
       if tarih in bostarihler and rotas in bosrota:
          print("   !!Mevcut bilet vardır!!")
          print("bilet rezerve edilmiştir")
          satılanb+=1
          dolurota.append(rotas)               
       else:
          print("   !!biletler tükenmiştir veya mevcut bilet yoktur!!")
    
    return dolurota,tarih,satılanb

        
def sıksorulansorular():
    
    sorular=["1-ASDASDASDASDASDASD","2-SDSADASDASDASDASD","3-ASDASDASDASDASD"]
        
    for xxx in sorular:
            print(xxx)
            
def kuponsorgu():
    class kuponsorgula:
     adress="no info"
        

     def __init__(self,kupon):
        self.kupon=kupon
        

     def intro(self):
        print("Merhaba kupon sorgulama ekranına Hoş geldiniz\n")   

     def sorgula(self):
        kuponlar=["Metro20","KamilKoç30","pamukkale10"]
        if (self.kupon in kuponlar):
            print("kuponunuz geçerlidir.\n Bilet Almadan önce vezne görevlisine bildiriniz.")
        else:
            print("kupon geçersiz")
         

            
        
        

    p1=kuponsorgula(kupon=input("kupon giriniz:"))
    p1.sorgula()
            
def sikayetveonerihattı():
       
 kullanıcılar= {}
 
 posta=input("kullanıcı e-posta: ")
 name=input("kullanıcı adı: ")
 surname=input("kullanıcı soyadı: ")
 info=input("Kullanıcı sikayet veya öneri: ")
 
 kullanıcılar[posta] ={

    "ad": name,
    "soyad" :surname,
    "sikayetveyaöneri" :info,


 }
 print(kullanıcılar)



            
    
def menu():
    while True:
       print("""\n 
       -bilet almak için (1)
       -Kupon Sorgulama (2)
       -BiletGo sıkça sorulan sorular için (3)
       -Sikayet ve öneri hattı(4)
       
       """)
       print("\n \n")
       karar=int(input("tuşlayınız:"))
       print("\n \n")

       
       if karar==1:
        usersqlite()
        biletal()
       elif karar==2:
         kuponsorgu()  
       elif karar==3:
        sıksorulansorular()
       elif karar==4:
        sikayetveonerihattı()
hellouser()        
menu()
           
