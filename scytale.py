#scytale.py
#by Brandon Tsao

#iterates over i letter skips and then prints the resultig string, allowing for user to identify words
#the number of skips is displayed to the user can input it into the next function...
def find_step(ct):
    i = 1
    l = len(ct) / 2

    while(i < l):
        print i, ct[::i]
        i += 1

#iterates over a string, appending the plaintext string with chunks of the cipher text with appropiately n skipped letters
def decrypt(ct, n):
    i = 0
    pt = ""

    while (i < n):
        pt += ct[i::n]
        i += 1

    return pt

ct = raw_input("Enter cipher txt: ")
''.join(i for i in ct if i.isalnum()) #remove whitespace, punctuation, and special characters

print find_step(ct)

n = int(raw_input("Enter number of skips: \n"))

print decrypt(ct, n)
