handle = open('03source')
strc = ""
for lines in handle.readlines():
    strc += lines
result = ""
for i in range(0, len(strc)):
    if strc[i].islower():
        if strc[i-4].islower() and strc[i-3].isupper() and strc[i-2].isupper() and strc[i-1].isupper() and strc[i+1].isupper() and strc[i+2].isupper() and strc[i+3].isupper() and strc[i+4].islower():
            result += strc[i]

print result
        
