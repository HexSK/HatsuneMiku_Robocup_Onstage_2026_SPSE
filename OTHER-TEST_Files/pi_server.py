import socket

# Bluetooth configuration
server_address = "00:00:00:00:00:00" # Listens on all available adapters
port = 1 # Standard RFCOMM port

# Create the Bluetooth socket
server_sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    server_sock.bind((server_address, port))
    server_sock.listen(1)
    
    print("Waiting for connection from PC...")
    client_sock, client_info = server_sock.accept()
    print(f"Accepted connection from {client_info}")

    # Receive data
    data = client_sock.recv(1024)
    print(f"Received: {data.decode('utf-8')}")

    # Send response
    response = "Hello from Raspberry Pi!"
    client_sock.send(response.encode('utf-8'))
    print(f"Sent: {response}")

except Exception as e:
    print(f"Error: {e}")

finally:
    client_sock.close()
    server_sock.close()
