#sssc.py

CT = raw_input("Enter CT: ") #Cipher Text (binary string of length 16)
K = raw_input("Enter Key: ") #Key Stream (binary string of length 16)

PT = [0] * 18

for i in range(16):
    if PT[i+1] == 0:
        PT[i+2] = int(CT[i])^int(K[i])^int(PT[i])
    else:
        PT[i+2] = int(CT[i])^int(K[i])^int(PT[i-1])

#print PT #prints as a list
print ''.join(map(str,PT))[2::] #prints nicely
