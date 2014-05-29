handle = open('02source')
c = ""
for line in handle.readlines():
    c += line

for ch in c:
    if ord(ch)>=48 and ord(ch) <= 57:
        print ch
    elif ord(ch)>=65 and ord(ch) <= 90:
        print ch
    elif ord(ch)>=97 and ord(ch) <= 122:
        print ch

