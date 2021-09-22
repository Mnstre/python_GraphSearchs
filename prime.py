def PYT(): return 'Python'
def CPP(): return 'C++'
def LUA(): return 'LUA'
def ASYa(): return 'Assembly'

def switch(x):
    switcher = {
        0: 'PYT',
        1: 'CPP',
        2: 'LUA',
        3: 'ASY'
    }[x]

valor = input("""
Entrada:\n
a . Python
b . C++
c . LUA
d . Assembly
""")
vFunction = switch(int(valor))
print(vFunction)