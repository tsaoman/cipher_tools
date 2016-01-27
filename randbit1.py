import math

s = []
s.append(136)
m = 167

k = [0] * 16 #generates key of length 16

for i in range(15):
    s.append(int((math.pow(s[i],2)%m)))

for i in range(16):
    if s[i] % 2:
        k[i] = 1
    else:
        k[i] = 0

print s
print ''.join(map(str,k)) #prints nicely
