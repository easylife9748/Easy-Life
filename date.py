import pyowm
import os
import time
import datetime

date = datetime.datetime.now()
date1=str(date)
print(date1)
d=str(date.day)
m=str(date.month)
y=str(date.year)
h=str(date.hour)
min=str(date.minute)


mon_fichier = open("/home/pi/speak.txt", "w")
mon_fichier.write(d)
mon_fichier = open("/home/pi/speak.txt", "r")
os.system("espeak -v en -f speak.txt  " )
os.system("espeak \"slash\"")

mon_fichier = open("/home/pi/speak.txt", "w")
mon_fichier.write(m)
mon_fichier = open("/home/pi/speak.txt", "r")
os.system("espeak -v en -f speak.txt  " )
os.system("espeak \"slash\"")

mon_fichier = open("/home/pi/speak.txt", "w")
mon_fichier.write(y)
mon_fichier = open("/home/pi/speak.txt", "r")
os.system("espeak -v en -f speak.txt  " )
os.system("espeak -ven+f3 \"the time now:\"")

mon_fichier = open("/home/pi/speak.txt", "w")
mon_fichier.write(h)
mon_fichier = open("/home/pi/speak.txt", "r")
os.system("espeak -v en -f speak.txt " )
os.system("espeak \"and\"")


mon_fichier = open("/home/pi/speak.txt", "w")
mon_fichier.write(min)
mon_fichier = open("/home/pi/speak.txt", "r")
os.system("espeak -v en -f speak.txt  " )
os.system("espeak \"minute\"")

os.system("espeak -ven+f3 \"have a great time\"")

mon_fichier
                                    
                                    
contenu = mon_fichier.read()
                    # status=Clouds>

 # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}




                                     





##
##
##from Tkinter import * 
##
##fenetre = Tk()
##
####label = Label(fenetre, text=tt, bg="yellow", width=100, height=50)
####label.pack()
##canvas = Canvas(fenetre, width=600, height=100, background='yellow')
###ligne1 = canvas.create_line(75, 0, 75, 120)
###ligne2 = canvas.create_line(0, 60, 150, 60)
##txt = canvas.create_text(300, 40,text=date1, font="Arial 16 italic", fill="red")
##
##canvas.pack()
##
##
####liste = Listbox(fenetre)
####liste.insert(1, h)
####liste.insert(2, w)
####liste.insert(3, "jQuery")
####liste.insert(4, "CSS")
####liste.insert(5, "Javascript")
####
####liste.pack()
##
##fenetre.mainloop()
##time.sleep(5)
##fenetre.quit()
##fenetre.destroy()
##
