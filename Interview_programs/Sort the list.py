l=[5,4,3,6,2,1]
n=len(l)

for i in range(n-1):
    for j in range(0, n-i-1):
        if l[j]>l[j+1]:
            l[j], l[j+1]= l[j+1], l[j]

print(l)