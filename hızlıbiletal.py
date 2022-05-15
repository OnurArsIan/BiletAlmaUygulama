print("     Onur Truizm'e hoş geldiniz!")
print("     ------------------------")
bostarihler=["12.12.12"]
bosrota=["ankara-izmir","istanbul-adana"]
dolurota=[]
satılanb=0
while True:
    print("""
    
    Üye olup ve bilet almak için (1)
    BiletGo sıkça sorulan sorular için (2)
    GÜn sonu raporu(sadece yetkililer) (3)
    Tuşlayınız!!!""")
    print("\n \n")
    karar=int(input("   tuşlayınız:"))
    print("\n \n")
    if karar== 1:
        
        print("   hızlı bilet menüsüne hoş geldiniz")
        print("   ---------------------------------")
        print("\n \n")
        tarih= input("   Tarih giriniz(gg.aa.yy):")
        rotas=input("   rota giriniz(baslangıc-bitis):")
        print("\n \n")
        for x in range(1):
            if tarih in bostarihler and rotas in bosrota:
                print("   !!Mevcut bilet vardır!!")
                satılanb+=1
                dolurota.append(rotas)               
            else:
                print("   !!biletler tükenmiştir veya mevcut bilet yoktur!!")
        print("""
        Bir üst menüye dönmek için E
        Uygulamadan çıkmak için C 
        Tuşlayınız!""")
        print("\n \n")
        karar1=input("E or C:")    
        if karar1=="E":
           continue
        else:
            break
    elif karar==3:
        sorular=["1-ASDASDASDASDASDASD","2-SDSADASDASDASDASD","3-ASDASDASDASDASD"]
        
        for xxx in sorular:
            print(xxx)
            break 
    elif karar== 4:
        print("özet")
        for xxxx in dolurota:
            print("--------------------------------------------")
            print("   satılan bilet {} {}".format(xxxx,tarih))
            print("   satılan bilet sayısı {}".format(satılanb))
            print("--------------------------------------------")
            break
                
        
                
        
        