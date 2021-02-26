
#Analitik Hiyerarsi Prosesi
import numpy as np



n = int(input("Kriter veya alternatif sayısını giriniz:")) #matris boyut degeri

m1 = np.ones((n,n),dtype=float) #baslangıc icin birim matris olusturalım.

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        a=input("{}.satır {}.sutun degeri:".format(i+1,j+1))
        if len(a)>1:
            a=round(float(a[0])/float(a[2]),4) 
        m1[i,j]=float(a)  
mc=m1.copy()  
print("Baslangıc Matrisi:\n")      
print(m1) # 1.matris gorunumu
print("***********************")

#normalizasyon

for i in range(n):
    t = np.sum(mc[:,i])
    for j in range(n):
        mc[j,i] = np.round(mc[j,i]/t,4)
        
        
print("normalize edilmiş matris:\n")       
print(mc)

#oncelık vektorunun olusturulması
o_vektor = np.ones((n,1))
for i in range(n):
    o_vektor[i]=round(np.sum(mc[i,:])/n,4)
print("oncelik vektoru: \n\n",o_vektor)


#CR(tutarlılık oranı) hesabı
cr1 = np.zeros((n,1))
for i in range(n):
    cr1= cr1+(o_vektor[i]*m1[:,i])

cr1 = cr1[0,:].reshape(n,1)
print("oncelik vektoru degerleri ve baslangıc vektorunun ilgili sutununun carpımı:")
print(cr1)

#CI(Tutarlılık indeksi) bulunması
imax=0
for i in range(n):
    imax = imax+(cr1[i]/o_vektor[i])

imax = round(float(imax)/n,3)
tut_indeks=round((imax-n)/(n-1),3)
print("****************************************************")
print("tutarlılık indeksi :",tut_indeks)

#Tutarlılık oranının bulunması
RI_tablo = [0,0,0.58,0.90,1.12,1.24,1.32,1.41,1.45,1.49,1.51,1.48,1.56,1.57,1.59]
RI_deger = RI_tablo[n-1]
print("RI degeri :",RI_deger)
Tutarlilik_Orani = round(tut_indeks / RI_deger,3) #tutarlılık oranı(CR) = CI/RI
print("Tutarlılık oranı:",Tutarlilik_Orani)
if Tutarlilik_Orani <0.1: #tutarlılık oranı 0.1 den kucuk olmalı.
    print("""
>>>>>>>>>>>>>>>  isleminiz tutarlidir...         
          """)
else:
    print("karsılatırma matrisi tutarlı değildir.Islemleri tekrarlayin...")

