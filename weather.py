import pyowm
import os
import time

owm = pyowm.OWM('38e32c9eea23385bc6fa2e452f821eb5')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('Paris,FR')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
wi=w.get_wind()                  # {'speed': 4.6, 'deg': 330}
h=w.get_humidity()              # 87
t=w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
#observation_list = owm.weather_around_coords(-22.57, -43.12)
t1=str(t['temp'])
print("temperature",t['temp'])
mon_fichier = open("/home/pi/speak.txt", "w")
mon_fichier.write(t1)
mon_fichier = open("/home/pi/speak.txt", "r")
os.system("espeak -ven+m3 \"the temperature is \"")
os.system("espeak -v en -f speak.txt " )
          
h1=str(h)         
mon_fichier = open("/home/pi/speak.txt", "w")
mon_fichier.write(h1)
mon_fichier = open("/home/pi/speak.txt", "r")
os.system("espeak -ven+m3 \"the humidity is \"")
os.system("espeak -v en -f speak.txt " )
          
wi1=str(wi['speed'])         
mon_fichier = open("/home/pi/speak.txt", "w")
mon_fichier.write(wi1)
mon_fichier = open("/home/pi/speak.txt", "r")
os.system("espeak -ven+m3 \"the wind speed is \"")
os.system("espeak  -v en -f speak.txt " )


                                     
##tt=str( t['temp'])                                       
##mon_fichier.write(tt)
##mon_fichier = open("/home/pi/speak.txt", "r")
##contenu = mon_fichier.read()

                                     





#os.system("espeak \"today the temperature\"-l en -s 70")

#os.system("espeak -v en -f speak.txt -s 70 " )
#print(contenu)

##print("humidity",h)
##print("wind",wi)
##from Tkinter import * 
##
##fenetre = Tk()
##
####label = Label(fenetre, text=tt, bg="yellow", width=100, height=50)
####label.pack()
##canvas = Canvas(fenetre, width=800, height=800, background='yellow')
###ligne1 = canvas.create_line(75, 0, 75, 120)
###ligne2 = canvas.create_line(0, 60, 150, 60)
##txt = canvas.create_text(300, 40,text=w, font="Arial 16 italic", fill="red")
##txt = canvas.create_text(200, 60,text="temperature", font="Arial 16 italic", fill="blue")
##txt = canvas.create_text(300, 60,text=tt, font="Arial 16 italic", fill="blue")
##txt = canvas.create_text(200, 80,text="humidity", font="Arial 16 italic", fill="blue")
##txt = canvas.create_text(300, 80,text=h, font="Arial 16 italic", fill="blue")
##txt = canvas.create_text(200, 100,text="wind speed", font="Arial 16 italic", fill="blue")
##txt = canvas.create_text(400, 100, text=wi, font="Arial 16 italic", fill="blue")
##canvas.pack()


##liste = Listbox(fenetre)
##liste.insert(1, h)
##liste.insert(2, w)
##liste.insert(3, "jQuery")
##liste.insert(4, "CSS")
##liste.insert(5, "Javascript")
##
##liste.pack()
##os.system("espeak \"here_the_weather_report \"-s 100")
##fenetre.mainloop()
##time.sleep(5)
##fenetre.quit()
##fenetre.destroy()
