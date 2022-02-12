def only_ints(x,y):

  if type(x)  == int and type(y) == int :
    print(True)
  else:
    print(False)
   
only_ints(int(input('input first int: ')),int(input('input second int: ')))