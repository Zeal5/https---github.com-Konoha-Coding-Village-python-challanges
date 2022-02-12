
def add_dots(s):
    s_dot = '.'.join(s)
   

    return s_dot
#print(add_dots('TEST'))

def remove_dots(s):
    s_nodots = ''
    for i in s :
        if i == '.':
            pass
        else:
            s_nodots += i
    return s_nodots 
#print(remove_dots('T.E.S.T'))

remove_dots(add_dots('abcde'))

    







