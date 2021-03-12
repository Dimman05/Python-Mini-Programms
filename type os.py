import struct
os_type = struct.calcsize('P')*8
print(os_type, 'bit')