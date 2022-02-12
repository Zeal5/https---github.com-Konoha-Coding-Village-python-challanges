import string
alphabets = string.ascii_letters


def LongestWord(sen):
    new_sen = sen.split()
    new_word = ''
    for letters in new_sen:
        new_word += ' '
          
        for letter in letters:
            
            if letter in alphabets:
                new_word += letter
            else:
                pass
    max = 0    
    for i in new_word.split():
        
        if len(i)>max:
            max = len(i)
            x = i
    
    return(x)        
       
print(LongestWord(input()))
    
