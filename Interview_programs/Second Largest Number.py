a=[4,3,5,1,7,9,40,2,3,8]
n=len(a)
for i in range (0,n-1):
    for j in range(0, n-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1]= a[j+1], a[j]

print("second largest number", a[-2])