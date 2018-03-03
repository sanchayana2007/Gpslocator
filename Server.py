import socket 

TCP_IP='127.0.0.1'
TCP_PORT=5005
BUFFER_SIZE=93


s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(1)

print('Server Listning on Address ',TCP_IP,':',TCP_PORT)

while True:
	conn, addr  = s.accept()
	print('Client received with address:',addr,':',TCP_PORT)
	
	try:
		while True:
			data= conn.recv(BUFFER_SIZE)
			resp="received"
			
			if not data:
				print('No data is received ')
				break
				
	except (KeyboardInterrupt,socket.error,socket.herror,socket.timeout) as e :
		print("Error",e.errno,e.strerror)
		if e.errno=10053:
			print("Client as connected ")
			

s.close()


