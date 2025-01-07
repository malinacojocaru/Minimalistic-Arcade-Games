import serial
import os
import platform

if platform.system() == "Windows":
    PORT = os.getenv('PORT', 'COM3')
else:
    PORT = os.getenv('PORT', '/dev/ttyACM0')
BAUDRATE = 115200

def smooth_data(old_value, new_value, threshold=2000):
    if abs(new_value - old_value) > threshold:
        return new_value
    return old_value

def parse_data():
    previous_values = [0, 0, 0]
    with serial.Serial(PORT, BAUDRATE) as ser:
        while True:
            line = ser.readline().decode('utf-8').strip()
            data = line.strip(" []").split(", ")
            if len(data) != 3 or any(d == '' for d in data):
                continue
            
            try:
                x, y, button = map(int, data)
            except ValueError:
                continue

            x = smooth_data(previous_values[0], x)
            y = smooth_data(previous_values[1], y)
            button = smooth_data(previous_values[2], button)

            previous_values = [x, y, button]

            return y
