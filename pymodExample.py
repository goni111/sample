from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import datetime, time

data = {}

def read_data(start_address, count):
    result = client.read_holding_registers(start_address, count, unit=1)
    print(result)
    count = 0
    for x in result.registers:
        data[start_address+count] = x
        count = count + 1

client = ModbusClient(method='rtu',
                      port='COM4',
                      stopbits=1,
                      bytesize=8,
                      parity='N',
                      baudrate=9600,
                      timeout=5)
                
connection = client.connect()
print(connection) 

while 1:
    read_data(0, 6)
    print(str(datetime.datetime.now()).split(".")[0])
    print("==============================")
    print("ENVIRONMENT MONITORING HOST")
    print("==============================")
    
    print("------------------------------")
    print("PM 2.5", data[0]/10, "μm")
    print("PM 10", data[1]/10, "μm")
    print("Temperature", data[2]/10, "°C")
    print("Humidity", data[3]/10, "%")
    print("Carbon Dioxide", data[5], "ppm")
    print("\n")
    print("\n")
    
    
    read_data(0x061, 10)
    read_data(0x077, 1)
    print("==============================")
    print("THREE PHASE METER")
    print("==============================")
    print("------------------------------")
    print('voltage of A phase',data[0x061]/10, 'V')
    print('voltage of B phase',data[0x062]/10, 'V')
    print('voltage of C phase',data[0x063]/10, 'V')
    print("------------------------------")
    print('electricity of A phase',data[0x064]/100, 'A')
    print('electricity of B phase',data[0x065]/100, 'A')
    print('electricity of C phase',data[0x066]/100, 'A')
    print("------------------------------")
    print('active power of A phase',data[0x067], 'W')
    print('active power of B phase',data[0x068], 'W')
    print('active power of C phase',data[0x069], 'W')
    print('total active power',data[0x06a], 'W')
    print("------------------------------")
    print('frequency',data[0x077]/100, 'Hz')
    print("------------------------------")
    print("\n")
    print("\n")
    
    read_data(0x00b, 10)
    print("==============================")
    print("ONE PHASE METER")
    print("==============================")
    print("------------------------------")
    print('voltage of phase',data[0x00b]/10, 'V')
    print('electricity of phase',data[0x00c]/100, 'A')
    print('active power of phase',data[0x00d], 'W')
    print('frequency',data[0x011]/100, 'Hz')
    print("------------------------------")
    print("\n")
    print("\n")
    time.sleep(10)
    time.sleep(10)



