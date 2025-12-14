with open('Codingal.txt', 'w') as f1:
    f1.write("My name is Sarthak and I'm 11 years-old")
f1.close()
with open('Codingal.txt', 'r') as f2:
    lines = f2.readlines()
    for line in lines:
        word = line.split()
        print(word)
f2.close()