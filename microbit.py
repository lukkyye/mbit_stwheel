import serial

class Mbit:
    #Constructor
    def __init__(self, baudrate, port):
        self.baudrate = baudrate
        self.port = port
        
    #Inicia el proceso de comunicacion mediante conexion Serial:
    def connect(self):
        serial_on = serial.Serial(baudrate=self.baudrate, port=self.port)
        print("Connected succesfully")
        return serial_on
    
    #Recorre la string, obtiene los numeros y luego retorna un promedio.
    @classmethod
    def get_numbers(cls, data, number_regex):
        numbers = number_regex.findall(data)
        return (sum(int(number) for number in numbers))/len(numbers)
    
    #Obtiene la informacion y la decodifica, devuelve una string.
    @classmethod
    def data_decoder(cls, serial_base):
        return serial_base.readline().decode().strip()