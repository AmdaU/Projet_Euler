#génére toute les permutations d'un string

p = lambda s:[i+j for i in s for j in p(s.replace(i,"",1))] if len(s)>1 else s

p('123')
