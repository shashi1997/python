i=int(input("Enter a number:"))
fact=1
print("the factorial of",i,"is:")
for x in range(1,i+1):
    fact *=x
print(fact)
