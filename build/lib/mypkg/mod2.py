def add(a,b):
    c=a+b
    return c

def sqr(a):
    c=a**2
    return c

def divs(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError as e:
        return ("an error occured", e)
