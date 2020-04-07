
import sys
print(sys.version)

# def hex2bin(HexInputStr, outFormat=4):
#     '''This function accepts the following two args.
#     1) A Hex number as input string and
#     2) Optional int value that selects the desired Output format(int value 8 for byte and 4 for nibble [default])
#     The function returns binary equivalent value on the first arg.'''
#     int_value = int(HexInputStr, 16)
#     if(outFormat == 8):
#         output_length = 8 * ((len(HexInputStr) + 1 ) // 2) # Byte length output i.e input A is printed as 00001010
#     else:
#         output_length = (len(HexInputStr)) * 4 # Nibble length output i.e input A is printed as 1010


#     bin_value = f'{int_value:0{output_length}b}' # new style
#     return bin_value

# print(hex2bin('3Fa', 8)) # prints 0000001111111010