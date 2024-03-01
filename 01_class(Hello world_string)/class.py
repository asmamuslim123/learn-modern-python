name : tuple[str,int,float] = ('pakistan','7','3.0')
print(name) #print
print(type(name)) #type
print(id(name)) #physcial address
print([i for i in dir(name) if "--" not in i]) #methods and attributes