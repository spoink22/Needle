import sys
num = int(sys.argv[1])
binary = bin(num)
hexadecimal = hex(num)

#I don't know if this part is necessary, but since the rest of the code is so simple, I thought I'd add a bit more to show off.
#This part just cleans up the output a bit.
finBin = str(binary).replace('0b','')
finHex = str(hexadecimal).replace('0x','')

print "Decimal: " + str(num)
print "Binary: " + finBin
print "Hexadecimal: " + finHex
