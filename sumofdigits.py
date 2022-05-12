n=int(input("enter the number: "))
tot=0
while(n>0):
    r=n%10
    tot=tot+r
    n=n//10
print("the total sum of digits is:",tot)

    