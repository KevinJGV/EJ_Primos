nums = []
primos = []
for i in range(2,1000):
    primos.append(i)
    nums.append(i)
    bandera = False
    for k in nums:
        for j in nums:
            if j * k == i:
                if j != i or k != i:
                    primos.pop()
                    bandera = True
                    break
            elif j * k > i:
                break
        if bandera:
            break
print(primos)