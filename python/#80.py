def find_digit(n):
    app = ''
    while len(app)<100:
        digit = 9
        for i in range(10):
            A = int(app + str(i))**2
            if i == 0:
                scale = 10**(2*(len(str(app))+1 - len(str(int( n**(0.5))))))
            N = n*scale
            if i == 0:
                scale2 = 10**len(str(abs(N-A)))
            # print(i, (N-A)/scale2, N, A)
            if N-A < 0:
                digit = i-1
                break
        app += str(digit)
    return app

squares = [x*x for x in range(int(101**(1/2))+1)]
total = 0


# for n in range(101):
    # if n not in squares:
        # digits = ''
        # while len(digits := find_digit(n, digits))<=100:
            # pass
        # digital_sum = (sum(list(map(lambda x: int(x), digits))))
        # print(n, digital_sum)
        # total += digital_sum
# print(total)

total =0
for i in range(100):
    if i not in squares:
        digits = find_digit(i)
        digital_sum = (sum(list(map(lambda x: int(x), digits))))
        total += digital_sum

print(total)
