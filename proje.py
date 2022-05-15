import datetime
import sqlite3

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
    
def menu():
    while True:
       print("""
    
       -bilet almak için (1)
       -BiletGo sıkça sorulan sorular için (2)
       -Gün sonu raporu(sadece yetkililer) (3)
       """)
       print("\n \n")
       karar=int(input("   tuşlayınız:"))
       print("\n \n")
       usersqlite()
