import socket
import bin.settings as s
from bin.first import buckets, a, b


def action(data):
    return data.upper().encode("utf-8")

def run():
    sock = socket.socket()
    sock.bind((s.IP, s.PORT))

    sock.listen(1)

    print(f"start listen port {s.PORT}:")

    conn, addr = sock.accept()

    print("--- conection ---")


    count = 0  # счетчик количества ходов
    while True and a.bucket_napolnen != 4:
        raw_data = conn.recv(1024)
        data = raw_data.decode("utf-8")

        if not data:
            break

        if data == 'stop':
            conn.send('kill'.encode("utf-8"))
            break
        if data == "1":
            a.popoln()
            count += 1
            a.result()
            print(f"Количество дейсвтий: {count}")
        elif data == '2':
            b.popoln()
            count += 1
            a.result()
            print(f"Количество дейсвтий: {count}")
        elif data == '3':
            a.pereliv_v3()
            count += 1
            a.result()
            print(f"Количество дейсвтий: {count}")
        elif data == '4':
           a.pereliv_v5()
           count += 1
           a.result()
           print(f"Количество дейсвтий: {count}")
        elif data == '5':
            b.out()
            count += 1
            a.result()
            print(f"Количество дейсвтий: {count}")
        elif data == '6':
            a.out()
            count += 1
            a.result()
            print(f"Количество дейсвтий: {count}")
        else:  # защита от дурака
            print(f'ADDR: {addr} вы ввели несуществующее значение, повторите ввод!')
        conn.send(action(data))
    if data != "stop":
        print(f'++++++++++Поздравляю с решением задачи в {count} ходов!!!+++++++++++++')
    conn.close()