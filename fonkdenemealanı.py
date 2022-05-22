
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
    
kuponsorgu()
