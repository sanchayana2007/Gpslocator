
import socket
import threading
import datetime
from time import sleep
from random import randrange
device_id=1

def new_device():
        device_id=device_id+1

def format103message(command='login'):
        message='0000000000' + str(device_id)
        i=randrange(0,6)
        command=['login','login','login','Alarm1','Breakdown','jam']
        if command[i]== 'login':
                message=message+'BR00'
        elif command[i]== 'Alarm1':
                message=message+'BO01'
        elif command[i]== 'Alarm2':
                message=message+'BO02'
        else:
                print("Command not supported")

        #datetime 
        dtimestamp=datetime.datetime.now()
        stamp="%s%s%s%s%s%s" % (dtimestamp.day,dtimestamp.month,dtimestamp.year,dtimestamp.hour,dtimestamp.minute,dtimestamp.second)

        message=message+stamp

        #Message: Part4 poplulate and Location 
        Location="A330.4288S7036.8518W"
        message=message+Location

        #Message: part5  Populated Speed 
        message=message+"20.4"

        #Message: part6 Populate speed UTC time :
        stamp="%s%s%s" %(dtimestamp.hour,dtimestamp.minute,dtimestamp.second)

        message=message+stamp
        #Message part 7 populate Speed Miscelneous 
        message=message+"1000000AL000192C2C"

        return message


def tcp_client_message(TCP_IP,TCP_PORT):
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(5.0) ## Set the timeout 
        try:
                s.connect((TCP_IP,TCP_PORT))
                return s

        except socket.error as e:
                print("Socket Error at creation",e.errno,e.strerror)
                #check if teh conenction is fine
                if e.errno==10061:
                        print("ERROR:Client hit an timeout")

def send_data(s,MESSAGE):
        BUFFER_SIZE=5120
        data=''
        try:
                if s:
                        print(s)
                s.send(MESSAGE.encode())
                data=s.recv(BUFFER_SIZE)
                ##Handle Server response once we received 
                if data:
                        print("received data",data)
                elif data=='AR01':
                        print("Serevr Send a Stop request ")
                elif not data:
                        print('Server Is gone out Track not replying')
        except (KeyboardInterrupt,socket.error,socket.herror,socket.timeout) as e:
                print("Socket Error at Send",e.errno,e.strerror)
                '''     
                if s:
                        s.close()
                '''

def close_client(socketid):
        socketid.close()

if __name__=="__main__":

        TCP_IP='127.0.0.1'
        TCP_PORT=5005
        TIME_GAPPING=1

        #start a client 
        s=tcp_client_message(TCP_IP,TCP_PORT)

        #Send and Receiver Messages 
        for i in range(1,5):
                MESSAGE=format103message('Login')
                print('message',MESSAGE)
                send_data(s,MESSAGE)
                sleep(TIME_GAPPING)

        close_client(s)
