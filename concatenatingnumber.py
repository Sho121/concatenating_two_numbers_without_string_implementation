#concatenating two numbers without string implementation
import math
result=0
add=dict()
count=dict()
n=int(input("Enter the number: "))
d=(int(math.log(n,10)))+1
for s in range(1,(d+1)):
    add[s]=0
i=1 
#adding i digit numbers to add{} and storing the no of i digit numbers to count{}   
while(i<=len(add)):
    c=0
    for j in range(1,n+1):
        if ((int(math.log(j,10)))+1)==i:
            add[i]=(add[i])*(pow(10,i))+j
            c=c+1
        else:
            continue
    count[i]=c 
    i=i+1
#producing the result while multiplyng (l+1) no. of zeros to value of add[l]   
for l in range(1,len(add)+1):
       if l==len(add):
           result=result+add[l]
       else:
          result=result+(add[l]*pow(10,(l+1)*count[l+1]))
print(result)         
 
