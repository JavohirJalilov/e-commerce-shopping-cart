f = open('data.json')
data = f.read()

idx1 = data.index(':')+2
idx2 = data.index(',')-1

idx3 = data.index('$',idx2)+1
idx4 = data.index(',',idx3)-1

print(data[idx3:idx4])