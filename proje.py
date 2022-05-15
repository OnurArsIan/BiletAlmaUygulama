import datetime

def hellouser():
    print("Biletgo ya hoş geldiniz")
    saatgun = datetime.datetime.now()
    tarih = datetime.datetime.strftime(saatgun, '%c')
    print(F"Güncel tarih ve saat bilgisi {tarih}")

hellouser()