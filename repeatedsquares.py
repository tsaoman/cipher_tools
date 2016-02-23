#user inputs
#b^n mod m
b = 17
n = 53
m = 97

#program
r = 1
while 1:
    #print "b:",b
    #print "a:",r,"\n"

    if n % 2 == 1:
        r = r * b % m
    n /= 2
    if n == 0:
        break
    b = b * b % m

print r
