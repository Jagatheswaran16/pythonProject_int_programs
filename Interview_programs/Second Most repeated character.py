s=input("enter the word")
k={}

for i in s:
    if i in  k:
        k[i]=k[i]+1

    else:
        k[i]=1

r=sorted(k, key=k.get, reverse=True)
print("second most repated" , r[1])