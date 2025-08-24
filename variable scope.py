# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created


name = "Lebron" # global scope (available inside and outside the functions)

def display_name():
    name = "James"   # a local scope (available only inside this function)
    print(name)

display_name()
print(name)



#    L.E.G.B rule
#    L = Local
#    E = Enclosing
#    G = Global
#    B = Built-in