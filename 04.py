import urllib2
base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
next = base+"63579"
for i in range(0, 400):
    response = urllib2.urlopen(next)
    html = response.read()
    print html
    nothing = ""
    for c in html:
        if c.isdigit():
            nothing += c
    next = base+nothing
            
            
    

