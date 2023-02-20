
import socket
from _datetime import datetime,timedelta

host='127.0.0.6'
port = 12001
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    my_socket.bind((host,port))
    my_socket.listen(10)#Can listen to up to 10 connections

except :
    e = "line 9, in <module> my_socket.bind((host,port)) OSError: [WinError 10048] Only one usage of each socket address (protocol/network address/port) is normally permitted"
    print(f"\033[91mError: {e}\033[0m")
    exit()
print ("The server is ready to receive requests.")

while True:
    try:
        cSocket,addr = my_socket.accept()
        data = cSocket.recv(1024).decode() #convert bytes to string
        destinationip=data[data.find("http://")+len("http://"):].split("/",1)[0] #Parsing to get the destination ip of acme.com
    except:
        e = "Server could not parse client request"
        print(f"\033[91mError: {e}\033[0m")
        exit()

    print('The client wants access to : '+destinationip+' at '+str(datetime.now()))
    try:
        PORT=80
        newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        newsocket.connect((destinationip, PORT))
        newsocket.send(data.encode()) #translated into a series of bytes to efficiently store the string
    except:
        e = "Server could not communicate with destination server"
        print(f"\033[91mError: {e}\033[0m")
        exit()
    print("The client's request was sent to the destination server at: "+str(datetime.now()))
    try:
        result=newsocket.recv(4096)
    except:
        e = "No response id being sent by the destination server"
        print(f"\033[91mError: {e}\033[0m")
        exit()
    print("The response was recieved from the destination server at: " + str(datetime.now()))

    newsocket.close()
    cSocket.send(result)
    print("The response was sent back to the client at: "+str(datetime.now()))

    cSocket.close()
    print('The connection between server and client has been closed.')


