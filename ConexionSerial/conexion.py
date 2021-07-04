import serial

arduino = serial.Serial('COM3', 9600)
arduino.flush()

while True:
    try:
        bytes = arduino.readline()
        line = bytes.decode('utf-8').strip()
        line = line.rstrip('\n')
        data = line.split(' ')
        humedad = data[0]
        centigrados = data[1]
        farenheiht = data[2]
        hic = data[3]
        hif = data[4]
        luz = data[5]
        print(humedad)
        print(centigrados)
        print(farenheiht)
        print(hic)
        print(hif)
        print(luz)
    except KeyboardInterrupt:
        break
