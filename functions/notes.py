#declaring a function
def display():
    print('This is a sample code')

#call a function
display()

def calc():
    return 3*4 #function return 
b = calc() #function expression
print(b)

#function with parameters
def details(name, age):
    print('Name : ',name, ' Age : ', age)
details('Sam', 10)