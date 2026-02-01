import socket
import sys

# Standard RFCOMM port (Channel 1)
PORT = 1

def start_server():
    try:
        # Create the Bluetooth socket
        server_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        
        # Binding to "" is the key to fixing the "bad bluetooth address" error
        # It allows the socket to use any available local adapter
        server_sock.bind(("", PORT))
        server_sock.listen(1)

        print(f"Robot Server is active on RFCOMM channel {PORT}")
        print("Waiting for your Samsung to connect...")

        # Wait for the phone to initiate connection
        client_sock, client_info = server_sock.accept()
        print(f"Accepted connection from {client_info}")

        while True:
            try:
                # Receive data from the phone
                data = client_sock.recv(1024)
                if not data:
                    break
                
                # Decode and clean up the message
                message = data.decode('utf-8').strip()
                print(f"Samsung Command: {message}")

                # Optional: Send a confirmation back to the phone
                response = f"Robot processed: {message}\n"
                client_sock.send(response.encode('utf-8'))

            except IOError:
                # This happens if the phone disconnects or moves out of range
                print("Connection lost.")
                break

    except Exception as e:
        print(f"Failed to start server: {e}")
    
    finally:
        if 'client_sock' in locals():
            client_sock.close()
        server_sock.close()
        print("Server closed.")

if __name__ == "__main__":
    start_server()
