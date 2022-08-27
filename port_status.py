import socket

def port_scanner(url):
    print('---------------------------------')
    print('[+] Ports :')

    ip = socket.gethostbyname (socket.gethostname()) # get the ip of the machine
    for port in range(250):	 # scan all ports between 1 to 250
        try:
            serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a socket
            serv.bind((ip,port)) # bind the socket to the port
        except:
            print('[OPEN] Port open :',port) # if the port is open, print the port number
        serv.close() #close connection

