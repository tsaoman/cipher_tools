# This program can be used to find repeated trigraphs.
# This is especially useful for breaking Vignere ciphers

s = raw_input() #input string

s = ''.join(s.split()) #removes whitespace
l = len(s)
trigraphs = {} #dictionary of trigraphs

for i in range(l-2):

    n = 0
    x = s[i] + s[i+1] + s[i+2] #sets the trigraph to search

    for j in range(l-2): #navigates through string searching for set trigraph
        if x == s[j] + s[j+1] + s[j+2]:
            n += 1 #if found, increase count

    if n > 1: #if there are multiple trigraphs, add to the dictionary
        trigraphs[x]=n

print trigraphs
