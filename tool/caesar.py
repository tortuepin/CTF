import string
s = input("input\n")
retstring = ""
for i in range(26):
    for c in s:
        if not c.isalpha():
            retstring += c
            continue
        if i + ord(c) > 122:
            i = i - 26
        c = ord(c) + i
        retstring += chr(c)
    retstring += "\n"
    
print(retstring)
print("(".isalpha())
