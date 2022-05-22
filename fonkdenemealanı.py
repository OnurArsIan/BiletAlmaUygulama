from distutils.log import info


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


sikayetveonerihattı()