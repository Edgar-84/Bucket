import socket

def run():
	sock = socket.socket()
	sock.connect(('localhost', 9090))
	while sock:
		deistvie = input('''сделай выбор
                1 - пополнить ведро 5-ти литровое
                2 - пополнить ведро 3-х литровое
                3 - перелить с 5-ти литрового ведра в 3-х литровое
                4 - перелить с 3-х литрового ведра в 5-ти литровое
                5 - вылить 3-х литровое ведро
                6 - вылить 5-ти литровое ведро
                : ''')
		sock.send(deistvie.encode('utf-8'))

		raw_data = sock.recv(1024)
		data = raw_data.decode("utf-8")
		print(f"Get: {data}")
		if data == 'kill':
			sock.close()
			break