# index operator [] = gives access to a sequence's element (str,tuples,list)

name = "prashast Srivastava!!"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[:8].upper()
last_name = name[9:19].upper()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)