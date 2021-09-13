def PYT(): return 'Python'
def CPP(): return 'C++'
def LUA(): return 'LUA'
def ASS(): return 'Assembly'

def switch(x):
    switcher = {
        0: "PYT",
        1: "CPP",
        2: "LUA",
    }[x]

valor = input("""
Entrada:\n
a . Python
b . C++
c . LUA
d . Assembly
""")
vFunction = switch(valor)
vFunction()