
import poplib
import email


SERVER = "server_name"   
USER = "easylife0015@gmail.com"
PASSWORD = "easylife0015"
 

server = poplib.POP3(SERVER)
server.user(USER)
server.pass_(PASSWORD)
 
 
