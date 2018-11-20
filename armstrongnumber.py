def armn(x):
   sum=0
   t=x
   while t>0:
         i=t%10
         sum+= i**3
         t=t//10
   if sum==x:
     print('Armstong number')
   else:
     print('not a Armstrong number')
print(armn(x))
