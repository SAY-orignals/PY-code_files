print("increasing pattern: ")
for r in range(1,9):
    for c in range(r):
        print('*',end=' ')
    print(' ')
print('decreasing pattern: ')
for r in range(9,1,-1):
    for c in range(r):
        print('*',end=' ')
    print(' ')