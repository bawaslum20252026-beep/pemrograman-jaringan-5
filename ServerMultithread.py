import socket
import threading

HOST = '127.0.0.1'
PORT = 5001

def handle_client(conn, addr):
    print(f"[TERHUBUNG] Client {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print(f"[PUTUS] Client {addr}")
            break

        print(f"Pesan dari {addr}: {data}")
        reply = f"[Server balas ke {addr}] Pesan diterima: {data}"
        conn.sendall(reply.encode())

    conn.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    print(f"Server multithread berjalan di {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[INFO] Total client aktif: {threading.active_count() - 1}")

if __name__ == "__main__":
    main()
