sum([sum([(int(i))**5 for i in str(n)]) for n in range(2,7*9**5) if sum([(int(i))**5 for i in str(n)]) == n ])
