def ArmN(x):                         #define function
 sum=0
 t=x
 while (t>0):                        #starts while loop
    d=t%10                           #extracts last digit
    sum+=d**3                        #cube of extracted digit
    t=t//10                          #gives quotent of the input
 if sum==x:                          #checks if sum equals input
    return "Armstrong Number"
 else:
    return "Not Armstrong Number"
x=int(input())
print(ArmN(x))
