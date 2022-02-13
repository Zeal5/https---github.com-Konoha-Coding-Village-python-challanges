#add a dot after each letter
def add_dots(s):
    s_dot = '.'.join(s)
   

    return s_dot

#remove dot after each letter
def remove_dots(s):
    s_nodots = ''
    for i in s :
        if i == '.':
            pass
        else:
            s_nodots += i
    return s_nodots 

#should return the same string as input
remove_dots(add_dots(input()))

    







