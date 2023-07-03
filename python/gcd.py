import matplotlib.pyplot as plt

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

n = 6**4

x = range(1,n)

y = [gcd(xe,n) for xe in x]


x1 = [(xe, ye) for xe, ye in zip (x,y) if ye % 2 == 0 and not ye % 3 == 0]
x2 = [(xe, ye) for xe, ye in zip (x,y) if ye % 3 == 0 and not ye % 2 == 0]
x3 = [(xe, ye) for xe, ye in zip (x,y) if ye % 3 == 0 and ye % 2 == 0]

plt.yscale('log')
# plt.plot(x1, 'b.')
# plt.plot(x2, 'r.')
# plt.plot(x3, 'k.')
plt.plot(x,y, '.')

plt.show()
