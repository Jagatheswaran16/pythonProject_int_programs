s= input("enter a string")

k={}

for i in s:
    if i in k:
        k[i]=k[i]+1
    else:
        k[i]=1

result=max(k, key=k.get)
print("repeated character=", result, "Count=", k[result])
