def factorize(x, factors, factor_canditate):
    while(factor_canditate*factor_canditate <= x):
        if (res := divmod(x,factor_canditate))[1] == 0:
            x = res[0]
            factors.append(factor_canditate)
            factor_canditate = 1
        factor_canditate += 1
    return factors + [x]

n, nums = 2, [0,0,0,0]

while not all(num == 4 for num in nums):
    n+=1
    nums.append(len(set(factorize(n, [], 2))))
    nums.pop(0)

print(n-3)

