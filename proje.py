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
       print("""
    
       -bilet almak için (1)
       -BiletGo sıkça sorulan sorular için (2)
       -Sikayet ve öneri hattı(3)
       """)
       print("\n \n")
       karar=int(input("   tuşlayınız:"))
       print("\n \n")

       
       if karar==1:
        usersqlite()
        biletal()
       elif karar==2:
        sıksorulansorular()
       elif karar==3:
        sikayetveonerihattı()
        
menu()
           
