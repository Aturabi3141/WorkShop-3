#!/usr/bin/env python
# coding: utf-8

# In[2]:


lst = [3,-3,0,5,-1]
lst= [0]
print (lst[1])
lst [4]=12
print(lst[10, 20, 30][1])


# In[ ]:


def main():
    data = [10,20,30,40,50,60]
    print(data[-1])
    print(data[-2])
    print(data[-3])
    print(data[-4])
    print(data[-5])
    print(data[-6])
main()


# In[ ]:


import math

karisikliste = [24.2, 2,4,"PYTHON","BİLİSİM", 19]
col = [23, [9.3,11.2,99.0], [23], [], 4, [0,0]]
print(col)
x = 4
y = 6
nums =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(nums[3])
nums[2] = (nums[0]+nums[9])/2
nums[1], nums[4] = sqrt(x), nums x+2*y


# In[ ]:


>>>s = "ABCDEFGHI"
>>>s[1]
a[x]
a[x+3]
a[max(x,y)]


# In[ ]:


karisikliste = [24.2, 4, "PYTHON", "BİLİSİM", 19, "Kelime", -0.03]


# In[ ]:


a = [2,4,6,8]
a + [1,3,5]
a = a + [1,3,5]
a += [10]
# a += 20 yanlış ifadedir!

print(a)


# In[ ]:


x = 2
a = [0,1]
a += [x]


# In[ ]:


def tablolustur():
    while True:
        a = []
        sayi = int(input("Bir Sayi giriniz: (ÇIKIŞ İÇİN -1 GİRİNİZ: )"))
        if sayi == "-1":
            print= ("Çıkış yapıldı")
            break
        else: 
            a + [sayi]
        print(a)
tablolustur()


# In[ ]:


def listolustur():
    sonuc = []
    girilensayi = 0
    while girilensayi>=0:
        girilensayi = int(input("Sayı giriniz ( Çıkış için -1 giriniz: )"))
        if girilensayi >=0:
            sonuc+=[girilensayi]
        return sonuc
def main():
    yaz = listolustur()
    print(yaz)
main()


# In[ ]:


def main():
    a = [0] * 10
    print(a)
    a = [3.4] *5
    print(a)
    a = 3* ["ABC"]
    n = 3
    a = n * ["abc", 22, 8.7]
main()


# In[ ]:


def main():
    toplam = 0.0
    girileceksayiadeti = 5
    sayilar = []
    print("Lütfen" ,girileceksayiadeti ,"adet sayi giriniz: ")
    for i in range(0, girileceksayiadeti):
        sayi = float(input(str(i+1) + ". sayiyi giriniz."))
        sayilar += [sayi]
        toplam += sayi
    for sayi in sayilar:
        print(end="Girilen Sayı : ")
        print(sayi, end="")
        print("ortalama: ", toplam/girileceksayiadeti)
main()


# In[ ]:


liste = list(range(0,21,2))
for i in range(-2,23):
    if i in liste:
        print(i, "eleman, ", liste, "listenin bir üyesidir")
    if i not in liste: 
        print(i, "eleman, ", liste, "listenin bir üyesi değildir")


# In[ ]:


a = [10,20,30,40]
b = a
print("a değişkeni", a)
b[2] = 35

print("b değişkeni", b)
print("a değişkeni", a)


# # Liste Sınırları Kodu 

# In[ ]:


#değerleri 0 olan 100 elemanlı bir liste oluşturunuz.

liste = [0]*100
x = int(input("Bir sayı giriniz: "))
if 0<= x<len(liste):
    liste[x]=1
    print("İndex içindedir")
else:
    print("Girilen değer index içinde değil.")
print(liste)


# # Dilimleme

# In[ ]:


lst = [10,20,30,40,50,60,70,80,90,100,110,120]
print(lst)
print(lst[0:3])
print(lst[4:8])
print(lst[-5:-3])
print(lst[:3])
print(lst[4:])
print(lst[:])
print(lst[-100:3])
print(lst[4:100])
print(lst[2:-2:2])
print(lst[::])


# In[25]:


liste = [1,2,3,4,5,6,7,8]
bsl = 0
bitis = 0
for bitis in range(0, 8):
    bitis += 1
    print(liste[bsl:bitis])
print("_____________________")
print(liste)
for bitis in range(0, 7):
    bitis += 1
    print(liste[bsl:-bitis])
    if bitis == 0:
        break
    


# In[4]:


a = list(range(10,51,10))
print(a)
del a[2]
print(a)

b = list(range(20))

print (b)

del b[5:15]

print(b)

del b[1], b[4]
print(b)


# In[7]:


import random

def topla(lst):
    sonuc = 0
    for eleman in lst:
        sonuc += eleman
        return result
def sifirata(lst):
    for i in range(len(lst)):
        lst[i]=0
def rastgeledegerata(n):
    sonuc=[]
    for i in range(n):
        rastgeledeger=random.randrange(100)
        sonuc += [rastgeledeger]
    return sonuc
def main():
    a = [2,4,6,8]
    print(a)
    print(sum(a))
    sifirata(a)
    print(a)
    print(sum(a))
    a = []
    print(a)
    print(sum(a))
    a=rastgeledegerata(10)
    print(a)
    print(sum(a))
    
main()
    


# In[11]:


liste = ["elma", "armut", "çilek"]
liste.append("erik")
print(liste)


# In[8]:


li1 = [1, 3, 4]
li2 = [10, 11, 12]
li1. append(li2)

print(li1)


# In[23]:


liste= [1,2,3,4,5,6,7,8]

liste.extend([9,10,11])
print(liste)

liste.insert(2,"python")
print(liste)

liste.pop()
liste
liste.pop(2)
liste
liste.remove(2)
liste
liste.index(4)
liste
liste = [1,1,1,1,2,3,4,5,6,6,7,8,6,8,5,43,23,4,6]
liste.count(1)
liste.sort()
liste


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




