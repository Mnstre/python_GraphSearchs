def PYT():
    print("Python")
    return 0
def CPP():
    print("C++")
    return 0
def LUA():
    print("LUA")
    return 0
def ASS():
    print("Assembly")
    return 0

def switch(x):
    return {
        'a': print(PYT),
        'b': print(CPP),
        'c': print(LUA),
        'd': print(ASS),
    }[x]

valor = input("""
Entrada:\n
a . Python
b . C++
c . LUA
d . Assembly
""")
switch(valor)