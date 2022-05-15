import datetime

def hellouser():
    h="Biletgo'ya hoş geldiniz"
    hnew=h.center(40,'*')
    print(hnew)
    saatgun = datetime.datetime.now()
    tarih = datetime.datetime.strftime(saatgun, '%c')
    info=f"{tarih}".center(40,'*')
    print(info)
    
hellouser()

