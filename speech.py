
import speech_recognition as sr
import datetime
import os
import signal
import subprocess
import time
import sys
import RPi.GPIO as GPIO
import time





duration=1
duration1=2
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

mlist=[]
loopme=1
r = sr.Recognizer()

cmd=1
cmd0=1
cmdk=1
while(cmdk==1):
	while(cmd0==1):
	    with sr.Microphone() as source:
		print "A moment of silence"
		r.adjust_for_ambient_noise(source, duration = 1)
		r.energy_threshold =1000
		print("Say something!")
		audio = r.listen(source,None,2)
		print("Trying to recognize audio")
	    try:
		
		t=r.recognize_google(audio)
		print "You just said " +t
	      
		if(t.find("hello")!=-1):                                                   
	 
		
			os.system("espeak -ven+f3 \"hello_alaa\"")
		
			os.system("espeak -ven+f3 \"i_hope_you_are_fine\"")
			cmd0=0
			cmd=1
			#proc2=subprocess.Popen(['python', 'mail.py'])
	    except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		os.system("espeak \"please_repeat_i_did_not_undestand\"")
		loopme=1
	    except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))



	while(cmd==1):
	 
	    with sr.Microphone() as source:
		print "A moment of silence"
		r.energy_threshold =800
		#r.dynamic_e-nergy_threshold = False
		#r.adjust_for_ambient_noise(source, duration = 1)
		#r.pause_threshold = 0.5
		
		print("Say something!")
		audio = r.listen(source,None,2)
		r.pause_threshold=0.5
		print("Trying to recognize audio")

	    try:
		
		t=r.recognize_google(audio)
		print "You just said00 " +t
	      
		if(t.find("assistance")!=-1):                                                   
		    #le=t.find("write")+len("write")+1
		    #t=t[le:]
		    #if(t=="text" or t=="text"):
			mon_fichier = open("/home/pi/chat.txt", "r")
			
	      		contenu = mon_fichier.read()
			os.system("espeak \"21 mode\"")
			#print(contenu)
			#os.system("espeak \"what_you_went_to_change\"")
                        print ("waiting 3 second ")
			time.sleep(3)

			cmd1=1
			while(cmd1==1):
	    			with sr.Microphone() as source:
	       				print "A moment of silence"
	       				r.energy_threshold =500
					r.adjust_for_ambient_noise(source, duration = 1)
					print("Say something for saving")
					r.pause_threshold=0.5

					audio = r.listen(source)
					print("Trying to recognize audio")
				try:		
			 		t=r.recognize_google(audio)
					print "You just said for change " +t
	
					print("sending__mail....")
					###############
					import smtplib
                                        from email.MIMEMultipart import MIMEMultipart
                                        from email.MIMEText import MIMEText

                                        msg = MIMEMultipart()
                                        msg['From'] = 'easylife0015@gmail.com'
                                        msg['To'] = 'alaa.bn.hassine@gmail.com'
                                        msg['Subject'] = '*********' 
                                        message = t
                                        msg.attach(MIMEText(message))
                                        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
                                        mailserver.ehlo()
                                        mailserver.starttls()
                                        mailserver.ehlo()
                                        mailserver.login('easylife0015@gmail.com', 'easylife0015')
                                        mailserver.sendmail('easylife0015@gmail.com', 'alaa.bn.hassine@gmail.com', msg.as_string())
                                        mailserver.quit()


					###############
		
					#audio = r.listen(source)
					#print("Trying to recognize audio")
					#b=r.recognize_google(audio)
					#if(b.find("yes")!=-1):                                             
					 #   print "hani bech nbadaletha beli t9oulou ",t
					#audio = r.listen(source)
	#				mon_fichier = open("/home/pi/chat.txt", "w")
		
					#print("Trying to recognize audio")
					#b=r.recognize_google(audio)
##					mon_fichier.write("" +t)	
##					mon_fichier = open("/home/pi/chat.txt", "r")
##					mon_fichier
##					os.system("espeak \"____________________________________________here_the_new_text\"")
##					print("here the new text")
##			      		contenu = mon_fichier.read()	
##					print(contenu)	

					#os.system("espeak \"ok_mester_alaa\"")	
					cmd1=0						
			
				


				except sr.UnknownValueError:
					print("Google Speech Recognition could not understand audio")
					loopme=1
				except sr.RequestError as e:
					print("Could not request results from Google Speech Recognition service; {0}".format(e))
		if(t.find("email")!=-1):                                                   
                        #le=t.find("write")+len("write")+1
                        #t=t[le:]
                        #if(t=="text" or t=="text"):
                        import poplib
                        import string, random
                        import StringIO, rfc822
                        import logging

                        SERVER = "pop.gmail.com"
                        USER  = "easylife0015@gmail.com"
                        PASSWORD = "easylife0015"

                        # connect to server
                        logging.debug('connecting to ' + SERVER)
                        server = poplib.POP3_SSL(SERVER)
                        #server = poplib.POP3(SERVER)

                        # login
                        logging.debug('logging in')
                        server.user(USER)
                        server.pass_(PASSWORD)

                        # list items on server
                        logging.debug('listing emails')
                        resp, items, octets = server.list()


                        numMessages = len(server.list()[1])

                        # download the first message in the list
                        id, size = string.split(items[numMessages-1])
                        resp, text, octets = server.retr(id)

                        # convert list to Message object
                        text = string.join(text, "\n")
                        file = StringIO.StringIO(text)
                        message = rfc822.Message(file)

                        # output message
                        print(message['From']),
                        print(message['Subject']),
                        print(message['Date']),
                      

			mon_fichier = open("/home/pi/speak.txt", "w")
                        mon_fichier.write(message['From'])
                        mon_fichier = open("/home/pi/speak.txt", "r")
                        os.system("espeak -ven+m3 \" you recieve a mail from\"")
                        os.system("espeak -v en -f speak.txt " )


                        mon_fichier = open("/home/pi/speak.txt", "w")
                        mon_fichier.write(message['Subject'])
                        mon_fichier = open("/home/pi/speak.txt", "r")
                        os.system("espeak -ven+m3 \"the subject is\"")
                        os.system("espeak -v en -f speak.txt " )
			

			#print(contenu)
			#os.system("espeak \"what_you_went_to_change\"")
		
		if(t.find("weather")!=-1):                                                   

			       
	
	      		       #os.system("espeak \"case one\"")
				#os.system("xpdf a1.pdf")
			       #proc=subprocess.Popen(['xpdf', 'a1.pdf'])
			       proc2=subprocess.Popen(['python', 'weather.py'])
		if(t.find("date")!=-1): 
                        #subprocess.call('mpg123 a3.mp3', shell=True)
                        deb=time.time()
			print(deb)


  		        proc3=subprocess.Popen(['python', 'date.py'])
			#os.system("espeak \"it s done\" -s 120 ")

		if(t.find("play")!=-1): 
                        #subprocess.call('mpg123 a3.mp3', shell=True)
  		        proc=subprocess.Popen(['mpg123', 'a3.mp3'])
  		        #proc1=subprocess.Popen(['python', 'blink1.py'])
  		        #GPIO.output(7, True)
  		        
                        #time.sleep(3)
			#os.system("mpg123 a3.mp3 ")
		if(t.find("close")!=-1):                                                   
			os.system("espeak \"it_is_done\" -s 100")	
			#os.kill(proc1.pid, signal.SIGKILL)#(proc.pid,signal.SIGNAL_SIGTERM)
			os.kill(proc2.pid, signal.SIGKILL)
		if(t.find("stop")!=-1):                                                   
			os.system("espeak \"it_is_done\" -s 100")	
			os.kill(proc.pid, signal.SIGKILL)#(proc.pid,signal.SIGNAL_SIGTERM)
			#os.kill(proc1.pid, signal.SIGKILL)
			#os.kill(proc.pid, signal.SIGKILL)
                        #GPIO.output(7, False)
		#t=r.recognize_google(audio)
		#print "You just said " +t		
		#if(t.find("bye")!=-1):                                                  
		
						
		#		os.system("espeak \"bye_mester_alaa\"")
		
	
		#		print("byeeeee <3 <3 <3")
				
		#		cmd0=1
		#		cmd=1
		#		cmd1=1	
		#		cmd=0

		    
	    except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		loopme=1
	    except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
	    except sr.RuntimeError as e:
		print("time out ; {0}".format(e))
