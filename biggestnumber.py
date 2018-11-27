#find maximum of 3 numbers
def max(a,b,c):          #define function
 if(a>b and a>c):        #starts if loop
  terminal
 elif(b>a and b>c):
  return b               
 else:
  return c
print(max(23,17,65))    #prints final output
