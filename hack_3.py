"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman "output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):

    
    s = s.replace('a', '@')
    s = s.replace('e', '3')
    s = s.replace('i', '¡')
    s = s.replace('o', '0')
    s = s.replace('u', 'v') 
    s = s.replace('n', 'N')
    s = s.replace('q', 'Q')
    s = s.replace('x', 'X')  
    if s:
        s = s[0].upper() + s[1:]
    
    return s

    
