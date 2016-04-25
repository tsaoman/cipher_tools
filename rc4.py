# rc4.py
# Brandon Tsao

# This program does a lot of things related to the RC4 cryptosystem, including
# 1. Generating a keystream based on a binary key
# 2. Converting Binary to Decimal, and vice versa
# 3. Encrypting text using a generated keystream
# 4. Binary encoding/decoding for custom charsets

#KNOWN ERRORS
#this program will sometimes remove leading zeroes of the final bit string, sometimes creating problems with encoding.

#FUNCTION DECLARATIONS

def subroutineA(y):
    return map(int,list(bin(y)[2::]))

    # bin returns a binary string in the format 0bXXXX
    # [2::] truncates the first two characters of the string, so it returns 'XXXX' instead of '0bXXXX'
    # list() turns the string into a list (or an array) of chars ('XXXX' --> ['X','X','X','X'])
    # map is taking each element in the new list/array of chars and converting it to int (['X','X','X','X'] --> [X,X,X,X])

    # the x argument insn't used, but was kept to standardize input.

def subroutineB(x):
    return int("".join(map(str,x)),2)

    #inverse of SubroutineA
    # map is taking each element in x (ints) and coverting them to chars
    # "".join() converts a char list/array into a string using the delimiter "" (nothing)
    #int(X,Y) converts a string X into an integer, assuming X was in base Y (2 in our case)

    #this subroutines weren't really used...

def generateKey(n,key,l):
    try:
        key = ''.join(map(str,key)) #converts input to string if original input is an array/list
    except:
        key = "".join(key.split()) #removes whitespace if input is a string

    array_length = 2**n #prevents recalculation of power

    K = [0] * array_length

    for i in range(array_length): #repeat key to fill array
        j = (i*n) % len(key) #creates a new iterator for every nth character. Mod repeats the key when key runs out

        #grabs n bits from the key and appends it to the key array
        temp = ''
        for k in range(n):
            temp += key[j+k]
        K[i] = int(temp,2) #converts binary to integer, and 'appends'

    #print K #DEBUGGING:print

    S = range(array_length) #initialize / define S

    j = 0 #reset

    #algorithm as provided
    for i in range(array_length):
        j = (j + S[i] + K[i]) % (2**n)
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        #print i,j,S #DEBUGGING:print

    i = j = 0 #reset
    KS = [0] * (l-1) #initialization

    #algorithm as provided
    for r in range(l-1):
        i = (i+1) % array_length
        j = (j + S[i]) % array_length

        temp = S[i]
        S[i] = S[j]
        S[j] = temp

        t = (S[i] + S[j]) % array_length
        KS[r] = S[t]
        #print i,j,t,KS[r],S #DEBUGGING:print

    #ensures that conversion from int --> bin always returns a n fixed-length bit string
    ans = ''
    for i in KS:
        temp = bin(i)[2::]

        for j in range(n-len(temp)):
            temp = ''.join(['0',temp])

        ans += temp

    return ans #returns bit string

def encrypt(text,key):
    try:
        text = ''.join(map(str,text)) #converts input to string if original input is an array/list
    except:
        text = "".join(text.split()) #removes whitespace if input is a string

    rkey = '' #repeated key

    r = len(text)/len(key)
    for i in xrange(r): #repeats the "full" key as many times as it cans
        rkey += key

    r = len(text)-len(rkey)
    for i in xrange(r): #fills the remainder with the first letter of the key, then second, etc.
        rkey += key[i]

    return bin(int(text,2)^int(rkey,2))[2::] #bit-xors the text and repeated key, returns a bit string

def decode(text): #decodes binary into ascii using encoding specified in RC4-1
    ans = []
    encoding = dict(zip(['000','001','010','011','100','101','110','111'],['A','B','C','D','E','F','G','H'])) #encoding dictionary

    temp = []
    for i in range(0,len(text),3): #splits text into bit triplets
        temp.append(text[i:i+3])

    for item in temp: #maps from binary to ascii using the encoding dictionary
        ans += (encoding.get(item,item))

    return ''.join(ans)

#USER DEFINED VARIABLES
CT = raw_input("Plaintext or Ciphertext: ")
n = int(raw_input("n: "))
l = int(raw_input("l: "))
#key = "011 001 100 001 101"
key = raw_input("key: ")

#CALCULATED / OUTPUT VARIABLES
keystream = generateKey(n,key,l)
PT = encrypt(CT,keystream)
print PT
