a = 0xea600669f6f16b3a2ad05d4b6d9b23911c8cc432fddd8d34a68d88af3d787b7eebf6cd1b720812086758ce56e24ab819ccd8fb5eedb1cae9f6f895667d7f89d0454b828777ecabc040a649c8956e78ec1c721370663065cbc343deabad9eb6f2aceab6bfed5bebe543aa3672cddf915c5b564848f4e6ec
b = 0xea600669f6f16b3a2ad05d4b6d9b23911c8cc432fddd8d34a68d88af3d787b7eebf6cd1b720812086758ce56e24ab819ccd8fb5eedb1cae9f6f895667d7f89d0454b828777ecabc040a649c8956e78ec1c721370663065cbc343deabad9eb6f2aceab6bfed5bea6543aa3672cddf915c5b564848f4e6ec

# Convert variables to binary strings
a_bin = bin(a)[2:]
b_bin = bin(b)[2:]

# Find index of first differing bit
index = 0
while index < len(a_bin) and index < len(b_bin):
    if a_bin[index] != b_bin[index]:
        break
    index += 1

print("Difference at index:", index)
