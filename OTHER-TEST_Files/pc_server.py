import socket

# Replace with your Pi's Bluetooth MAC (find it by running 'hciconfig' on Pi)
server_address = "B8:27:EB:EF:E2:0C" 
port = 1 

try:
    # Create RFCOMM Bluetooth socket
    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    print(f"Connecting to {server_address}...")
    sock.connect((server_address, port))

    # Send Test Message
    message = "Test message from PC"
    sock.send(message.encode())
    print(f"Sent: {message}")

    # Receive Response
    data = sock.recv(1024)
    print(f"Received from Pi: {data.decode()}")

    sock.close()
except Exception as e:
    print(f"Error: {e}")
