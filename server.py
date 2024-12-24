import socket

def start_server():
    host = '127.0.0.1'  # Локальний хост
    port = 65432        # Порт для з'єднання

    # Створення сокета TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Очікування лише одного клієнта
    print(f"Сервер запущено на {host}:{port}")

    # Прийняття з'єднання
    client_socket, client_address = server_socket.accept()
    print(f"З'єднання встановлено з {client_address}")

    while True:
        # Отримання повідомлення від клієнта
        data = client_socket.recv(1024).decode('utf-8')
        if not data or data.lower() == 'exit':
            print("Клієнт завершив з'єднання.")
            break
        print(f"Клієнт: {data}")

        # Відправка повідомлення клієнту
        response = input("Ви: ")
        client_socket.send(response.encode('utf-8'))
        if response.lower() == 'exit':
            print("З'єднання завершено сервером.")
            break

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
