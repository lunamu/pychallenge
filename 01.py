strc = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
strn = ""
for c in strc:
    if c == ' ' or c=='.':
        print c
        strn += c
    elif c =='y':
        strn += 'a'
    elif c=='z':
        strn += 'b'
    else:
        c = chr(ord(c)+2)
        strn = strn + c

print strn 

