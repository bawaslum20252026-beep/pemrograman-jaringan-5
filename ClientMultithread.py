import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 5001

def send_request(id_client):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        message = f"Request dari client-{id_client}"
        print(f"[KIRIM] {message}")
        client_socket.sendall(message.encode())

        response = client_socket.recv(1024).decode()
        print(f"[BALASAN] {response}")

        client_socket.sendall(b"exit")
        client_socket.close()
    except Exception as e:
        print(f"[ERROR] Client-{id_client}: {e}")

def main():
    threads = []

    start_time = time.time()
    print("Mengirim 10 request secara bersamaan ke server...\n")

    # Buat dan jalankan 10 thread client
    for i in range(10):
        t = threading.Thread(target=send_request, args=(i+1,))
        threads.append(t)
        t.start()

    # Tunggu semua thread selesai
    for t in threads:
        t.join()

    print(f"\nSelesai mengirim 10 request dalam {time.time() - start_time:.2f} detik")

if __name__ == "__main__":
    main()
