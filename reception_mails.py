import poplib
import string, random
import StringIO, rfc822
import logging
import email
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
#print(str(message)),
# output message
print(message['From']),
print(message['Subject']),
print(message['Date']),
#print(message['text']),
#print(str(message.fp.read(100))),
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



        
#print(server.retr(numMessages)[1])
#server.get_content()
