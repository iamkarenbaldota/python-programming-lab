#find maximum of 3 numbers
def max(a,b,c):          #define function
 if(a>b and a>c):        #starts if loop
  terminal
 elif(b>a and b>c):
  return b               #returns value of b
 else:
  return c               #returns value of c
print(max(23,17,65))     #prints final output
