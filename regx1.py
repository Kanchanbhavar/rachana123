"""import re
a1=re.compile("ab")
reobj=a1.finditer("abaaaba")
for x in reobj:
    print(x.start()," ",x.group())
    import re"""


import re
reobj=re.finditer("a(2)","ab")
for x in reobj:
    print(x.start(),"....",x.group())
    #print(x.end(),"....",x.group())