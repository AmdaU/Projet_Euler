import matplotlib.pyplot as plt

xs,ys = [],[]

for x in range(10000):
    for y in range(200):
        if len(str(x**y)) == y:
            xs.append(x)
            ys.append(y)


plt.plot(xs,ys,".")
