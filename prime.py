x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
print("the prime numbers between",x,"and",y,"are:")
for n in range(x,y+1):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            print(n)
