import socket

HOST = '127.0.0.1'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server berjalan di {HOST}:{PORT}")
print("Menunggu koneksi client...")

while True:
    conn, addr = server_socket.accept()
    print(f"Terhubung dengan client {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print("Client memutuskan koneksi.")
            break

        print(f"Pesan dari client: {data}")
        conn.sendall(f"Server menerima: {data}".encode())

    conn.close()
