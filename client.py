import socket

def start_client():
    host = '127.0.0.1'  # Локальний хост (той самий, що і у сервера)
    port = 65432        # Порт (той самий, що і у сервера)

    # Створення сокета TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Підключено до сервера {host}:{port}")

    while True:
        # Відправка повідомлення серверу
        message = input("Ви: ")
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            print("З'єднання завершено клієнтом.")
            break

        # Отримання відповіді від сервера
        response = client_socket.recv(1024).decode('utf-8')
        if not response or response.lower() == 'exit':
            print("Сервер завершив з'єднання.")
            break
        print(f"Сервер: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
