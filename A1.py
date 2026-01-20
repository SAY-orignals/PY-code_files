a = {}
print(a)
b = {1: 'ball',2: 'call'}
print(b)
c = {'name': 'Sarthak',1: [2,5,4], 'age':11}
print(c)
print(c['name'])
#update(one key)
c['age'] = 12
print("updated: ",c)
c['country'] = 'Qatar'
print("added: ",c)
c.pop('name')
print("Deleted: ",c)

c.get('age')
print("accessed: ",c)
print("New: ",c)
c.clear()
print("cleared: ",c)