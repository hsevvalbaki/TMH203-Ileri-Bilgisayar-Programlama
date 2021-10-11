#!/usr/bin/env python
# coding: utf-8

# In[5]:


yukseklik=int(input("yükseklik değerini giriniz:"))
tabanuzunlugu=int(input("taban uzunluğu değerini giriniz:"))
alan=(yukseklik*tabanuzunlugu)/2
if alan<50:
    print("kucuk")
elif alan>50:
    print("buyuk")
else:
    print("eşit")


# In[6]:


a=int(input("bir tam sayı giriniz:"))
b=int(input("bir tam sayı giriniz:"))
carpim=(a*b)
if carpim>0:
    print("pozitif")
elif carpim<0:
    print("negatif")
else:
    print("sıfır")


# In[9]:


r=int(input("yarıçap değeri giriniz:"))
pi=3.14
alan=pi*pow(r,2)
cevre=2*pi*r
if alan>cevre:
    print("bu yarıçap değerindeki dairenin alanı çevresinden büyüktür")
elif alan<cevre:
    print("bu yarıçap değerindeki dairenin çevresi alanından büyüktür")
else:
    print("bu yarıçap değerindeki dairenin alanı ve çevresi birbirine eşittir")


# In[ ]:




