from serial import SerialException
import microbit
import re
from vgamepad import VX360Gamepad
import time

print("===================================")
select_port = str(input("Select serial port to connect: "))
print("Baudrate at 115200 by default. Do you want to change it?")
decision = input("y/n: ")

match decision:
    case "y": baudrate = int(input("Select baudrate: "))
    
    case "n": baudrate = 115200

print("Triying to connect: ")
while True:
    try:
        get_serial_data = microbit.Mbit(baudrate, select_port).connect()
        control = VX360Gamepad()
        number_regex = re.compile(r'-?\d+')
        break
    except SerialException:
        print("Connection failed, trying again in: ")
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
    else:
        pass
        
    

while True:
    try:
        new_data_string = microbit.Mbit.data_decoder(get_serial_data)
        
        if new_data_string:
            # Convertir el valor del acelerómetro a un valor entre -32767 y 32767 (rango del joystick)
            joystick_value = int(microbit.Mbit.get_numbers(new_data_string, number_regex) * 32767 / 2048)  # Ajustar según el rango de tu acelerómetro

            # Actualizar el estado del joystick en el gamepad virtual
            control.left_joystick(x_value=-joystick_value, y_value=0)

            # Enviar el reporte al sistema
            control.update()
    except SerialException:
        print("Satus: Disconnected")
        time.sleep(1)
        quit("Re-launch again if you want to connect again")
    