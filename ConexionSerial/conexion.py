import serial
import requests

arduino = serial.Serial('COM3', 9600)
arduino.flush()

while True:
    try:
        bytes = arduino.readline()
        line = bytes.decode('utf-8').strip()
        line = line.rstrip('\n')
        data = line.split(' ')
        dic = {
            "humedad": data[0],
            "centigrados": data[1],
            "fahrenheit": data[2],
            "i_calor_c": data[3],
            "i_calor_f": data[4],
            "luz": data[5],
        }
        print(dic)
        resp = requests.post('http://localhost:4000/metrics', json=dic)
        resp = resp.json()
        print(resp)
    except KeyboardInterrupt:
        break
