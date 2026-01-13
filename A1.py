class parrot:
    species = 'birds'
    def __init__(self,name,age):
        self.name = name
        self.age = age
blu = parrot("blu",20)
woo = parrot("woo",25)
print("specieis of parrot 1 and 2 is", blu.species)
print('name of parrot 1 is ' ,blu.name,' and its age is ',blu.age,'.')
print('name of parrot 2 is ' ,woo.name,' and its age is ',woo.age,'.')