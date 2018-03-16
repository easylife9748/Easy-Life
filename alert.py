from __future__ import print_function
import httplib2
import os

import os
import time
import datetime

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


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
    ant1='0'
    while True :
    
        """Shows basic usage of the Google Calendar API.

        Creates a Google Calendar API service object and outputs a list of the next
        10 events on the user's calendar.
        """
        credentials = get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        #print('Getting the upcoming 10 events')
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
            date = datetime.datetime.now()
            date1=str(date)
            #print(date1)
            d1=str(date.day)
            m1=str(date.month)
            y1=str(date.year)
            h1=str(date.hour)
            #print("h1======",h1)
            min1=str(date.minute)
           
            if eve=="medical"  :  
                #print( event['start'].get('dateTime'))
                
                #print(eve)
                
                try:
                        eve1=(event['description'])
                        #print (eve1)
                except  KeyError:
                        pass
              
                        #for i in range(4):
                try:
                    y=t[0]+t[1]+t[2]+t[3]
                    #print( y),
                    m=t[5]+t[6]
                    #print( m),
                    d=t[8]+t[9]
                    #print(d),
                except IndexError:
                    pass
                try:
                    h=t[11]+t[12]
##                    print( h),
                    min=t[14]+t[15]
##                    print( min),
##                    print(float(h)*60+float(min)),
##                    print(float(h1)*60+float(min1))
##                    print(d,d1)
##                    print(m,m1)
##                    print(y,y1)
                except IndexError:
                    pass
                ant=y+m+d+h+min
                #print (ant)
                #ant1='0'
                k=0

                if  y==y1 and float(m)==float(m1) and float(d)==float(d1) and (float(h1)*60+float(min1)) <= (float(h)*60+float(min)) and (float(h)*60+float(min)-30)<=(float(h1)*60+float(min1)) and ant!=ant1 :
                        while k!=3 :
                            os.system("pkill mpg123" ) 
                            os.system("espeak -ven+m3 \"urgent alert description \"")
                            
                            print( "aleeeeeeeeert")
##                                                    
                            os.system("espeak -ven+m3 \"urgent instruction\" -s 200")
                            mon_fichier = open("/home/pi/speak.txt", "w")
                            mon_fichier.write(eve1)
                            mon_fichier = open("/home/pi/speak.txt", "r")
                            os.system("espeak -v en -f speak.txt -s 200 " )
                             
                                                      
                            k+=1
                            ant1=ant
                           # 


                                
    ##        mon_fichier = open("/home/pi/speak.txt", "w")
    ##        mon_fichier.write( d)
    ##        mon_fichier = open("/home/pi/speak.txt", "r")
    ##        os.system("espeak -ven+m3 \"upcomping event at \"")
    ##        
    ##        os.system("espeak -v en -f speak.txt " )
    ##        os.system("espeak -ven+m3 \"slash\"")
    ##        
    ##        mon_fichier = open("/home/pi/speak.txt", "w")
    ##        mon_fichier.write( m)
    ##        mon_fichier = open("/home/pi/speak.txt", "r")
    ##        
    ##        
    ##        os.system("espeak -v en -f speak.txt " )
    ##        os.system("espeak -ven+m3 \"slash\"")
    ##        
    ##                
    ##        mon_fichier = open("/home/pi/speak.txt", "w")
    ##        mon_fichier.write( y)
    ##        mon_fichier = open("/home/pi/speak.txt", "r")
    ##        
    ##        
    ##        os.system("espeak -v en -f speak.txt " )
    ##        
    ##        os.system("espeak -ven+m3 \"at\"")               
    ##        mon_fichier = open("/home/pi/speak.txt", "w")
    ##        mon_fichier.write( h)
    ##        mon_fichier = open("/home/pi/speak.txt", "r")
    ##        
    ##        
    ##        os.system("espeak -v en -f speak.txt " )
    ##        
    ##        os.system("espeak -ven+m3 \"and\"")
    ##        mon_fichier = open("/home/pi/speak.txt", "w")
    ##        mon_fichier.write( m)
    ##        mon_fichier = open("/home/pi/speak.txt", "r")
    ##        os.system("espeak -v en -f speak.txt " )
    ##        os.system("espeak -ven+m3 \"minute\"")
    ##        
    ##            
    ##        os.system("espeak -ven+m3 \"description of event\"")
    ##        mon_fichier = open("/home/pi/speak.txt", "w")
    ##        mon_fichier.write( eve)
    ##        mon_fichier = open("/home/pi/speak.txt", "r")
    ##        os.system("espeak -v en -f speak.txt " )
    ##        
    ##        
    ##    
    ####        
    ####        
    ####        mon_fichier = open("/home/pi/speak.txt", "w")
    ####        mon_fichier.write(  str(event['summary']))
    ####        mon_fichier = open("/home/pi/speak.txt", "r")
    ####        os.system("espeak -ven+m3 \"the description is\"")
    ####        os.system("espeak -v en -f speak.txt " )


if __name__ == '__main__':
    main()



