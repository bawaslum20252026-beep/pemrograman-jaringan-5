import asyncio

HOST = '127.0.0.1'
PORT = 5000

async def send_request(id_client, message):
    try:
        reader, writer = await asyncio.open_connection(HOST, PORT)

        print(f"[Client-{id_client}] Mengirim: {message}")
        writer.write(message.encode())
        await writer.drain()

        data = await reader.read(1024)
        print(f"[Client-{id_client}] Balasan: {data.decode()}")

        # Tutup koneksi dengan sinyal 'exit'
        writer.write(b"exit")
        await writer.drain()

        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print(f"[Client-{id_client}] ERROR: {e}")

async def main():
    print("Menjalankan 10 request secara bersamaan (single-thread async)...\n")

    # Buat 10 task asynchronous
    tasks = [
        asyncio.create_task(send_request(i+1, f"Pesan ke-{i+1} dari client"))
        for i in range(10)
    ]

    # Jalankan semua task sekaligus
    await asyncio.gather(*tasks)

    print("\nSemua request selesai dikirim.")

if __name__ == "__main__":
    asyncio.run(main())
