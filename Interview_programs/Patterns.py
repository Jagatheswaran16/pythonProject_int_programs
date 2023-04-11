def test(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("5", end="")
        print("\r")

test(6)
print("done")
