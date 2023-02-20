import socket
from datetime import datetime
import uuid
server = '127.0.0.6'
port = 12001



clientsocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
clientsocket.connect((server,port))
IP=input('Enter IP Address  (HTTP works.I used the website acme.com(23.93.76.124) for testing my program): ')
request="GET http://"+IP+"/ HTTP/1.1\r\n\r\n"
clientsocket.send(request.encode()) # translated into a series of bytes to efficiently store the string
s=datetime.now() #Date time in HH:MM:SS:mm

print("Getting access to "+IP+' at '+str(s))
# Receive response
response_string = clientsocket.recv(4096)
e=datetime.now()
if not response_string:
    ee="No response try another ip"
    print(print(f"\033[91mError: {ee}\033[0m")) #Uded this format to clearly print the error in red color as i used the PYCHARM IDE
else:
    print("Proxy server responded at: "+str(e)+"\n"+ response_string.decode()) #convert bytes to string
# Close socket
starthour=s.hour #take hour from the datetime format
startmin=s.minute   #take min from the datetime format
startsec=s.second #take sec from the datetime format
startmicro=s.microsecond #take nicrosec from the datetime format
endhour=e.hour
endmin=e.minute
endsec=e.second
endmicro=e.microsecond
hours=endhour-starthour
mins=endmin-startmin
secs=endsec-startsec
microseconds=(endmicro-startmicro)
microseconds = int(str(microseconds)[:3])
if microseconds<0:
    microseconds=-1*microseconds

print('Total round trip was: '+str(hours)+':'+str(mins)+':'+str(secs)+':'+str(microseconds))
mac_address = uuid.getnode()
mac_address_hex = ':'.join(['{:02x}'.format((mac_address >> elements) & 0xff) for elements in range(0,8*6,8)][::-1])
#Used the help of https://www.codespeedy.com/how-to-get-mac-address-of-a-device-in-python/ for the mac address
print('Mac Address: '+mac_address_hex)
clientsocket.close()
print('Client socket closed')
