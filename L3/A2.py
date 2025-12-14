f1 = open('Newfile.txt', 'x')
f1.close()
import os
if os.path.exists('Newfile.txt'):
    print("File already exists")
else: 
    print("file does not exist")

f2 = open('Newfile.txt', 'w')
f2.write("My name is Sarthak and I'm 11 yrs-old")
f2.close()

os.remove('Newfile.txt')
if os.path.exists('Newfile.txt'):
    print("File exists")
else:
    print("It doesn't exist")
#os.rmdir()