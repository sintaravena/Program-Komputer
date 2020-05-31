# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 07:41:33 2020

@author: hp
"""

i = 0

while i <= 10:
    print(i)
    # bagian ini wajib ada di dalam while
    #penambahan kuonter
    i = i+1

print("selesai")


i = 3

while i <= 10:
    print(i)
    # bagian ini wajib ada di dalam while
    #penambahan kuonter
    i = i+1

print("selesai")


k = 100
while k >= 90:
    print(k)
    k -= 1
print("")
print("selesai")
    


k = 100
while k >= 90:
    print(k)
    k = k- 1
print("")
print("selesai")



ulang = True
counter = 1
inputser = ""

while ulang == True :
    print("------------")
    inputser = input ("apakah program akan diulangi?(y/n)")
    if inputser == "y" :
        ulang = True
    else :
        ulang = False
    print("**************")
    
    
    
    
    
import random
#help (random. randrange)
maxPengulangan = 10
nAngka = 0
nGambar = 0
nPelemparan = 0

while nPelemparan < maxPengulangan :
    angkaergambar = random.randrange (0,2)
#   print(angkaorgambar)
    if angkaorgambar == 0:
        nGambar = nGambar + 1
    else :
        nAngka = nAngka + 1
        
    nPelemparan += 1

print ()
print(" Dari jumlah pelemparan", maxpengulangan," koin, diperoleh :", nAngka, "angka, diperoleh :" )