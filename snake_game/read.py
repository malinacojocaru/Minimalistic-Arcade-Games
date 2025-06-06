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
            x_dir = 'center'
            y_dir = 'center'
            pressed = False

            if x < 2000:
                x_dir = 'left'
            elif x > 64000:
                x_dir = 'right'
            if y < 2000:
                y_dir = 'up'
            elif y > 64000:
                y_dir = 'down'
            if button < 200:
                pressed = True
            else:
                pressed = False

            return x_dir, y_dir, pressed