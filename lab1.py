import sys
arg0 = sys.argv[0]
try: arg1 = sys.argv[1]
except Exception:print("Invalid filename")
f = open(arg1)
data = f.read()
f.close()
data = data.split('\n')
n1 = data.index('.circuit')
del data[0:n1+1]
n2 = data.index('.end')
del data[n2:len(data)]
x = [];z= []
for i in range(0,len(data)):
 x.append(data[i].split(' '))
 try: n3 = x[i].index('#')
 except Exception:n3 = len(x[i])
 del x[i][n3:len(x[i])]
 while '' in x[i]:
    x[i].remove('')
x.reverse()
for i in range(0,len(x)):
    x[i].reverse()
    z.append (' '.join(x[i]))
z = '\n'.join(z)
print(z)    
