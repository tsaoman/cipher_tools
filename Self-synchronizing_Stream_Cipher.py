#sssc.py

CT = raw_input("Enter CT: ") #Cipher Text (binary string of length n)
K = raw_input("Enter Key: ") #Key Stream (binary string of length n)

n = len(CT)

PT = [0] * (n+2)

for i in range(n):
    if PT[i+1] == 0:
        PT[i+2] = int(CT[i])^int(K[i])^int(PT[i])
    else:
        PT[i+2] = int(CT[i])^int(K[i])^int(PT[i-1])

#print PT #prints as a list
print ''.join(map(str,PT))[2::] #prints nicely
