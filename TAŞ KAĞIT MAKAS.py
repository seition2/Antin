from tkinter import *
import random
global kiskor
kiskor = 0
global biskor
biskor=0
sec = [0,1,2]
bskor = 0
cıkıs = ["q"]
kskor = 0

print(
    "Taş Kağıt Makas oyununa hoş geldiniz!\nİlk harfi büyük olacak şekilde yazınız(Taş)\nÇıkmak için q ya basınız\nİYİ EĞLENCELER!")

pencere = Tk()
pencere.title("ANTİN TAŞ KAĞIT MAKAS OYUNU")
pencere.config(bg="SlateBlue4")

ekrangn = pencere.winfo_screenwidth() // 3
ekranyk = pencere.winfo_screenheight() // 3
pencere.geometry("{}x{}+300+300".format(ekrangn,ekranyk))
kskor = Label(pencere,fg='cyan', font ='Comic 15 bold',
          bg='SlateBlue4', text= "Oyuncu:"+str(kiskor))
kskor.place(x= 10 , y=50)
bskor = Label(pencere,fg='cyan', font ='Comic 15 bold',
        bg ='SlateBlue4', text= "Bilgisayar:"+str(biskor))
bskor.place(x=350,y=50)
secimBilgisayar = Label(pencere,fg='cyan', font ='Comic 15 bold',
bg='SlateBlue4', text= "Bilgisayar Seçimi : ")
secimBilgisayar.place(x=110, y=90)

def Tas():
  global biskor
  global kiskor
  Bdeğeri = random.choice(sec)
  if Bdeğeri == 0: 
    print("Berabere Kaldınız...")
    secimBilgisayar.config(text="Bilgisayar Taşı Seçti")
  elif Bdeğeri == 2:
    print("Sen Kazandın")
    kiskor+=1
    kskor.config(text="Kullanıcı:"+str(kiskor))
    secimBilgisayar.config(text="Bilgisayar Makası Seçti")
  else:
    print("Maçı Kaybettiniz")
    biskor+=1
    bskor.config(text="Bilgisayar:"+str(biskor))
    secimBilgisayar.config(text="Bilgisayar Kağıdı  Seçti")
def kagit():
  global biskor
  global kiskor
  Bdeğeri =random.choice(sec)
  if Bdeğeri == 1:
    print("Berabere Kaldınız...")
    secimBilgisayar.config(text="Bilgisayar Kağıdı Seçti")
  elif Bdeğeri ==2:
    print("Sen Kazandın")
    kiskor+=1
    kskor.config(text="Kullanıcı:"+str(kiskor))
    secimBilgisayar.config(text="Bilgisayar Taşı Seçti")
  else:
    print("Maçı Kaybettiniz")
    secimBilgisayar.config(text="Bilgisayar Makası Seçti")
    biskor+=1
    bskor.config(text="Bilgisayar:"+str(biskor))
def makas():
  global biskor
  global kiskor
  Bdeğeri =random.choice(sec)
  if Bdeğeri == 2:
    print("Berabere Kaldınız...")
    secimBilgisayar.config(text="Bilgisayar Makası Seçti")
  elif Bdeğeri ==0:
    print("Sen Kazandın")
    kiskor+=1
    kskor.config(text="Kullanıcı:"+str(kiskor))
    secimBilgisayar.config(text="Bilgisayar Kağıdı Seçti")
  else:
    print("Maçı Kaybettiniz")
    secimBilgisayar.config(text="Bilgisayar Taşı Seçti")
    biskor+=1
    bskor.config(text="Bilgisayar:"+str(biskor))




dugmeTas= Button(pencere,text = 'TAŞ', command = Tas, width=15)
dugmeKagit=Button(pencere,text = 'KAĞIT' ,command=kagit, width= 15)
dugmeMakas= Button(pencere,text = 'MAKAS', command =makas, width=15)

dugmeTas.place(x=50,y = 150)
dugmeKagit.place(x=50,y =200)
dugmeMakas.place(x=50,y=250)
pencere.mainloop()



