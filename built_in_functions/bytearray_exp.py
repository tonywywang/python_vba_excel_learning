print(bytearray())  # bytearray(b'')
print(bytearray(10))  # bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
print(bytearray(range(20)))  # bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13')
# print(bytearray('Hi!')) TypeError: string argument without an encoding
print(bytearray(b'Hi!'))
bytearray.fromhex('2Ef0 F1f2  ') # skips all ASCII whitespace in the string, not just spaces