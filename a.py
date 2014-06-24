import pickle
handle = open('05source')
jc = pickle.Unpickler(handle)
c = jc.load()
strc = ''
for i in range(0, len(c)):
    strc = ''
    for j in range(0, len(c[i])):
        for k in range(0, c[i][j][1]):
            strc+=c[i][j][0]
    print strc
