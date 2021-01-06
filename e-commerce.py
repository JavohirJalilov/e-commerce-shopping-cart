f = open('data.json')
data = f.read()

idx1 = data.index(':')+2
idx2 = data.index(',')-1

idx3 = data.index('$',idx2)+1
idx4 = data.index(',',idx3)-1

idx5 = data.index(':',idx4)+1
quantity = int(data[idx5:-1])

string = '[' + data[idx1:idx2] + ',' + data[idx3:idx4] +','+ str(quantity) + ']'

print(string)