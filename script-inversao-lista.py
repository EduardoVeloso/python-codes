v = []
for i in range(0,10):
    v.append(i)
print(v)
for j in range(int(len(v)/2)):
    temp = v[j]
    v[j] = v[len(v)-1-j]
    v[len(v)-1-j] = temp
print(v)
