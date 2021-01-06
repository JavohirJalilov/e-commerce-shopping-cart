f = open('data.json')
data = f.read()

idx1 = data.index(':')+2
idx2 = data.index(',')-1

print(data[idx1:idx2])