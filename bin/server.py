import socket

import bin.settings as s


def action(data):
    return data.upper().encode("utf-8")


def run():
    sock = socket.socket()
    sock.bind((s.IP, s.PORT))

    sock.listen(1)

    print(f"start listen port {s.PORT}:")

    conn, addr = sock.accept()

    print("--- conection ---")

    a = 0  # количество литров в 5-ти литровом ведре
    b = 0  # количество литров в 3-х литровом ведре
    k = 0  # счетчик количества ходов
    while True and a!=4:
        raw_data = conn.recv(1024)
        data = raw_data.decode("utf-8")

        if not data:
            break

        if data == 'stop':
            conn.send('kill'.encode("utf-8"))
            break
        if data == "1":
            a = 5
            k += 1
            print(f'ADDR: {addr} В 5-ти литровом ведре {a} литров, в 3-х литровом ведре {b} литров,\
количество действий {k}')
        elif data == '2':  # порядок действий для пополнения 3-х литрового ведра
            b = 3
            k += 1
            print(f'ADDR: {addr} В 5-ти литровом ведре {a} литров,в 3-х литровом ведре {b} литров,\
количество действий {k}')
        elif data == '3':  # порядок действий для перелив. с 5-ти в 3-х лит.ведро
            b = b + a
            a = 0
            k += 1
            if b > 3:
                a = b - 3
                b = 3
            print(f'ADDR: {addr} В 5-ти литровом ведре {a} литров,в 3-х литровом ведре {b} литров,\
количество действий {k}')
        elif data == '4':  # порядок действий для перелив. с 3-х в 5-ти лит.ведро
            a = a + b
            b = 0
            k += 1
            if a > 5:
                b = a - 5
                a = 5
            print(f'ADDR: {addr} В 5-ти литровом ведре {a} литров,в 3-х литровом ведре {b} литров,\
количество действий {k}')
        elif data == '5':  # порядок действий для опустошения 3-х лит. ведра
            b = 0
            k += 1
            print(f'ADDR: {addr} В 5-ти литровом ведре {a} литров,в 3-х литровом ведре {b} литров,\
количество действий {k}')
        elif data == '6':  # порядок действий для опустошения 5-ти лит. ведра
            a = 0
            k += 1
            print(f'ADDR: {addr} В 5-ти литровом ведре {a} литров,в 3-х литровом ведре {b} литров,\
количество действий {k}')
        else:  # защита от дурака
            print(f'ADDR: {addr} вы ввели несуществующее значение, повторите ввод!')
        conn.send(action(data))
    if data != "stop":
        print(f'++++++++++Поздравляю с решением задачи в {k} ходов!!!+++++++++++++')

    conn.close()