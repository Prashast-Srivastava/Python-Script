# scope = The region where that a variable is recognised
#         A variable is only available from inside the region it is created
#         A global and a local scoped variable can be created

# L --> local
# E --> enclosing
# G --> global
# B --> built-in

name = "Prashast"  # global scope (available inside and outside the function)

def display_name():
    name = "Srivastava"   # local scope (only available in this function)
    print(name)

# display_name()
print(name)
display_name()
