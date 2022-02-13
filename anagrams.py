def is_anagram(sa,sb):
    s1 = list(sa)
    s2 = list(sb)
    s1.sort()
    s2.sort()
    
    a = s1
    b = s2
    if a == b:
        return True
    else:
        return False
    
   
is_anagram('test', 'tess')


