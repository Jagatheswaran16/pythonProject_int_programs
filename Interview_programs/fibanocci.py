s= int(input("enter a num"))
n1,n2=0,1
c=0
while c<s:
    print(n1)
    p=n1+n2
    n1=n2
    n2=p
    c=c+1
