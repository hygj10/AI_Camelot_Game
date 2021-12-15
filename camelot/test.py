state = [[2, 5], [7, 9], [11, 12]]
nstate = [i[:] for i in state]
g = []
for i in state:
    g.append(i)
print(nstate, g)