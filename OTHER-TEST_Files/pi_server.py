import serial, time

phone = serial.Serial('/dev/rfcomm0', baudrate=115200, timeout=0.1)
pico  = serial.Serial('/dev/ttyS0', baudrate=115200, timeout=0.1)

while True:
    if phone.in_waiting > 0:
        #phonemsg = phone.readline().decode('utf-8', 'ignore').strip()
        #if phonemsg == 'pingfromphone':
        #    pico.write(b'pingfromphone\n')
        msg = phone.read(phone.in_waiting).decode('utf-8', 'ignore').strip()
        print(f"phone sent {msg}") #debug print
        print("Forwarding to pico...")
        pico.write((msg+'\n').encode())
    if pico.in_waiting > 0:        
        #picomsg = pico.readline().decode('utf-8').strip()
        #if picomsg == 'pongfrompico':
        #    phone.write(b'pongfrompico\r\n')
        msg = pico.read(pico.in_waiting).decode('utf-8', 'ignore').strip()
        print(f"Pico sent {msg}") #debug print
        phone.write((msg+'\n').encode())

    time.sleep(0.05)
