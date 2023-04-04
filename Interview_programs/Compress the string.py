#input=aabbcccdddd
#output=a2bac3d4

s="aabbccc"
n=len(s)
c=0
k=''
for i in range(n-1):
    if s[i]==s[i+1]:
        c=c+1

    else:
        k=k+s[i]+str(c)

print(k)