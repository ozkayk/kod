import random
import string
degisken= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu=int(input("şifre uzunluğu giriniz"))
sifre=""


for _ in range(sifre_uzunlugu):
    sifre += random.choice(degisken)

print("Oluşturulan Parola", sifre)
