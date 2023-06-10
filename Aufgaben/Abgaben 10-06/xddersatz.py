import binascii

input_file = 'signatur.der'
output_file = 'binary_file.bin'

with open(input_file, 'r') as f:
    hex_data = f.read().replace(" ","").replace('\n', '')

binary = bytes.fromhex(hex_data)
binary_data = binascii.unhexlify(hex_data)

with open(output_file, 'wb') as f:
    f.write(binary)

# ascii_representation = binary_data.decode('ascii')
# print(ascii_representation)