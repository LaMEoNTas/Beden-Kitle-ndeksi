#Made by LaMEoNTas
# BKİ == kg/boy^2
print("* BEDEN KİTLE İNDEKSİ HESAPLAMA *")
#%%
cevap=("H")
while ( cevap=="H"):
    try:
        boy=float(input("Boy  Girin (Örnek: 1.90) : "))
    except ValueError:
        print("HATA !")
        break
    if boy>2.51 or boy<=0:
        print("Sallama!")
        break
#%%    
    try:
        kilo=float(input("Kilo Girin (Örnek: 76) : "))
    except ValueError:
        print("HATA !")
        break
    if kilo<=0:
        print("Sallama!")
        break
#%%        
    BKİ=float(kilo/(boy**2))
    
    print(" \n ")
    print(BKİ)
#%% 
    if BKİ<20:
        print(" \n Zayıf")
    elif (BKİ>20)and(BKİ<25):
        print(" \n Normal")
    elif (BKİ>25)and(BKİ<30):
        print(" \n Kilolu")
    elif (BKİ>30)and(BKİ<35):
        print(" \n 1. Derece Obez")
    elif (BKİ>35)and(BKİ<40):
        print(" \n 2. Derece Obez")
#%%
    cevap=input("Çıkış Yapmak İster Misin?  (E/H) ")
    if (cevap=="E"):
        break




