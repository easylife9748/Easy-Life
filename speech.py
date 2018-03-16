#from __future__ import print_function
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
                        we=0
                        da=0
	 
                        proc3=subprocess.Popen(['python', 'alert.py'])
			os.system("espeak -ven+f3 \"hello my dear \"")
		
			os.system("espeak -ven+f3 \"i hope you are fine\"")
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
	      
		if(t.find("assistance")!=-1) or (t.find("voice")!=-1):
                        os.system("pkill mpg123" ) 
                        we=0
                        da=0
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
                        os.system("pkill mpg123" ) 
                        we=0
                        da=0
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
		
		if(t.find("weather")!=-1)and we!=1:
                               

			       
                               da=0    
	      		       #os.system("espeak \"case one\"")
				#os.system("xpdf a1.pdf")
			       #proc=subprocess.Popen(['xpdf', 'a1.pdf'])
			       proc2=subprocess.Popen(['python', 'weather.py'])
                               we=1
                               os.system("pkill mpg123" ) 
		if(t.find("date")!=-1) or (t.find("time")!=-1)   or (t.find("day")!=-1) and da!=1 :
                        
                        we=0
                        #subprocess.call('mpg123 a3.mp3', shell=True)
                        deb=time.time()
			print(deb)
                        os.system("pkill mpg123" ) 

  		        proc3=subprocess.Popen(['python', 'date.py'])
			#os.system("espeak \"it s done\" -s 120 ")
                        da=1
                        
                        
		if(t.find("play")!=-1):
                        da=0
                        we=0#subprocess.call('mpg123 a3.mp3', shell=True)
  		        proc=subprocess.Popen(['mpg123', 'a3.mp3'])
  		        #proc1=subprocess.Popen(['python', 'blink1.py'])
  		        #GPIO.output(7, True)
  		        
                        #time.sleep(3)
			#os.system("mpg123 a3.mp3 ")
		#if(t.find("close")!=-1):                                                   
			#os.system("espeak \"it_is_done\" -s 100")	
			#os.kill(proc1.pid, signal.SIGKILL)#(proc.pid,signal.SIGNAL_SIGTERM)
			#os.kill(proc2.pid, signal.SIGKILL)
		if(t.find("stop")!=-1) or (t.find("close")!=-1):
                        da=0
                        we=0
			os.system("espeak \"clossing music\" -s 170")	
			os.kill(proc.pid, signal.SIGKILL)
		if(t.find("event")!=-1)or (t.find("even")!=-1) or (t.find("events")!=-1):
                        da=0
                        we=0
                        os.system("pkill mpg123" ) 
			#os.system("espeak \"it_is_done\" -s 100")	
                        #os.kill(proc.pid, signal.SIGKILL)
                        
                        import httplib2
                        import os

                        from apiclient import discovery
                        from oauth2client import client
                        from oauth2client import tools
                        from oauth2client.file import Storage

                        import datetime

                        try:
                            import argparse
                            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
                        except ImportError:
                            flags = None

                        # If modifying these scopes, delete your previously saved credentials
                        # at ~/.credentials/calendar-python-quickstart.json
                        SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
                        CLIENT_SECRET_FILE = 'client_secret.json'
                        APPLICATION_NAME = 'Google Calendar API Python Quickstart'


                        def get_credentials():
                            """Gets valid user credentials from storage.

                            If nothing has been stored, or if the stored credentials are invalid,
                            the OAuth2 flow is completed to obtain the new credentials.

                            Returns:
                                Credentials, the obtained credential.
                            """
                            home_dir = os.path.expanduser('~')
                            credential_dir = os.path.join(home_dir, '.credentials')
                            if not os.path.exists(credential_dir):
                                os.makedirs(credential_dir)
                            credential_path = os.path.join(credential_dir,
                                                           'calendar-python-quickstart.json')

                            store = Storage(credential_path)
                            credentials = store.get()
                            if not credentials or credentials.invalid:
                                flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
                                flow.user_agent = APPLICATION_NAME
                                if flags:
                                    credentials = tools.run_flow(flow, store, flags)
                                else: # Needed only for compatibility with Python 2.6
                                    credentials = tools.run(flow, store)
                                print('Storing credentials to ' + credential_path)
                            return credentials

                        def main():
                            """Shows basic usage of the Google Calendar API.

                            Creates a Google Calendar API service object and outputs a list of the next
                            10 events on the user's calendar.
                            """
                            credentials = get_credentials()
                            http = credentials.authorize(httplib2.Http())
                            service = discovery.build('calendar', 'v3', http=http)

                            now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
                            print('Getting the upcoming 10 events')
                            eventsResult = service.events().list(
                                calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
                                orderBy='startTime').execute()
                            events = eventsResult.get('items', [])

                            if not events:
                                print('No upcoming events found.')
                            for event in events:
                                start = event['start'].get('dateTime', event['start'].get('date'))
                                #print(start, event['summary'])
                                t=str(event['start'].get('dateTime'))
                                eve=str(event['summary'])
                                if eve!="medical" :  
                                    print( event['start'].get('dateTime'))
                                    
                                    print(eve)
                                    
                                    try:
                                            eve1=str(event['description'])
                                            print (eve1)
                                    except  KeyError:
                                            pass
                                  
                                            #for i in range(4):
                                    try:
                                        y=t[0]+t[1]+t[2]+t[3]
                                        print( y),
                                        m=t[5]+t[6]
                                        print( m),
                                        d=t[8]+t[9]
                                        print(d),
                                    except IndexError:
                                        pass
                                    try:
                                        h=t[11]+t[12]
                                        print( h),
                                        min=t[14]+t[15]
                                        print( min),

                                    except IndexError:
                                        pass
                                                            
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( d)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    os.system("espeak -ven+m3 \"upcomping event on \" -s 200")
                                    
                                    os.system("espeak -v en -f speak.txt  -s 190" )
                                    os.system("espeak -ven+m3 \"slash\" -s 200")
                                    
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( m)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    
                                    
                                    os.system("espeak -v en -f speak.txt -s 200 " )
                                    os.system("espeak -ven+m3 \"slash \" -s 200" )
                                    
                                            
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( y)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    
                                    
                                    os.system("espeak -v en -f speak.txt -s 200 " )
                                    
                                    os.system("espeak -ven+m3 \"at\" -s 200")               
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( h)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    
                                    
                                    os.system("espeak -v en -f speak.txt " )
                                    
                                    os.system("espeak -ven+m3 \"and\"")
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( min)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    os.system("espeak -v en -f speak.txt " )
                                    os.system("espeak -ven+m3 \"minute\"")
                                    
                                        
                                    os.system("espeak -ven+m3 \"description of event\"")
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( eve)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    os.system("espeak -v en -f speak.txt " )



                        if __name__ == '__main__':
                            main()


		if(t.find("medical")!=-1)or (t.find("medical")!=-1):                                                   
			#os.system("espeak \"it_is_done\" -s 100")	
                        #os.kill(proc.pid, signal.SIGKILL)
                        os.system("pkill mpg123" ) 
                        da=0
                        we=0
                        import httplib2
                        import os

                        from apiclient import discovery
                        from oauth2client import client
                        from oauth2client import tools
                        from oauth2client.file import Storage

                        import datetime

                        try:
                            import argparse
                            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
                        except ImportError:
                            flags = None

                        # If modifying these scopes, delete your previously saved credentials
                        # at ~/.credentials/calendar-python-quickstart.json
                        SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
                        CLIENT_SECRET_FILE = 'client_secret.json'
                        APPLICATION_NAME = 'Google Calendar API Python Quickstart'


                        def get_credentials():
                            """Gets valid user credentials from storage.

                            If nothing has been stored, or if the stored credentials are invalid,
                            the OAuth2 flow is completed to obtain the new credentials.

                            Returns:
                                Credentials, the obtained credential.
                            """
                            home_dir = os.path.expanduser('~')
                            credential_dir = os.path.join(home_dir, '.credentials')
                            if not os.path.exists(credential_dir):
                                os.makedirs(credential_dir)
                            credential_path = os.path.join(credential_dir,
                                                           'calendar-python-quickstart.json')

                            store = Storage(credential_path)
                            credentials = store.get()
                            if not credentials or credentials.invalid:
                                flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
                                flow.user_agent = APPLICATION_NAME
                                if flags:
                                    credentials = tools.run_flow(flow, store, flags)
                                else: # Needed only for compatibility with Python 2.6
                                    credentials = tools.run(flow, store)
                                print('Storing credentials to ' + credential_path)
                            return credentials

                        def main():
                            """Shows basic usage of the Google Calendar API.

                            Creates a Google Calendar API service object and outputs a list of the next
                            10 events on the user's calendar.
                            """
                            credentials = get_credentials()
                            http = credentials.authorize(httplib2.Http())
                            service = discovery.build('calendar', 'v3', http=http)

                            now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
                            print('Getting the upcoming 10 events')
                            eventsResult = service.events().list(
                                calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
                                orderBy='startTime').execute()
                            events = eventsResult.get('items', [])

                            if not events:
                                print('No upcoming events found.')
                            for event in events:
                                start = event['start'].get('dateTime', event['start'].get('date'))
                                #print(start, event['summary'])
                                t=str(event['start'].get('dateTime'))
                                eve=str(event['summary'])
                                if eve=="medical" :  
                                    print( event['start'].get('dateTime'))
                                    
                                    print(eve)
                                    
                                    try:
                                            eve1=str(event['description'])
                                            print (eve1)
                                    except  KeyError:
                                            pass
                                  
                                            #for i in range(4):
                                    try:
                                        y=t[0]+t[1]+t[2]+t[3]
                                        print( y),
                                        m=t[5]+t[6]
                                        print( m),
                                        d=t[8]+t[9]
                                        print(d),
                                    except IndexError:
                                        pass
                                    try:
                                        h=t[11]+t[12]
                                        print( h),
                                        min=t[14]+t[15]
                                        print( min),

                                    except IndexError:
                                        pass
                                                            
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( d)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    os.system("espeak -ven+m3 \"upcomping event on \" -s 200")
                                    
                                    os.system("espeak -v en -f speak.txt  -s 190" )
                                    os.system("espeak -ven+m3 \"slash\" -s 200")
                                    
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( m)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    
                                    
                                    os.system("espeak -v en -f speak.txt -s 200 " )
                                    os.system("espeak -ven+m3 \"slash \" -s 200" )
                                    
                                            
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( y)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    
                                    
                                    os.system("espeak -v en -f speak.txt -s 200 " )
                                    
                                    os.system("espeak -ven+m3 \"at\" -s 200")               
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( h)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    
                                    
                                    os.system("espeak -v en -f speak.txt " )
                                    
                                    os.system("espeak -ven+m3 \"and\"")
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( min)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    os.system("espeak -v en -f speak.txt " )
                                    os.system("espeak -ven+m3 \"minute\"")
                                    
                                        
                                    os.system("espeak -ven+m3 \"description of event\"")
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( eve)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    os.system("espeak -v en -f speak.txt " )
                                    
                                    os.system("espeak -ven+m3 \"medical instruction\"")
                                    mon_fichier = open("/home/pi/speak.txt", "w")
                                    mon_fichier.write( eve1)
                                    mon_fichier = open("/home/pi/speak.txt", "r")
                                    os.system("espeak -v en -f speak.txt " )
                                    #event['summary']='medical0'


                        if __name__ == '__main__':
                            main()




			#(proc.pid,signal.SIGNAL_SIGTERM)
			#os.kill(proc1.pid, signal.SIGKILL)
			#os.kill(proc.pid, signal.SIGKILL)
                        #GPIO.output(7, False)
		#t=r.recognize_google(audio)
		#print "You just said " +t
                if(t.find("thank")!=-1) or (t.find("thanks")!=-1):
                    os.system("pkill mpg123" ) 
                    os.system("espeak -ven+f3 \"not at all my dear \"")
##		if(t.find("bye")!=-1):                                                  
##		
##						
##				os.system("espeak  -ven+f3  \"bye my dear \"")
##		
##	
##				print("byeeeee <3 <3 <3")
##				
##				cmd0=1
##				cmd=1
##				cmd1=1	
##				cmd=0

		    
	    except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
		loopme=1
	    except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
	    except sr.RuntimeError as e:
		print("time out ; {0}".format(e))
