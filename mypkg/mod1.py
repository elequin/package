def sub(a,b):
    c=a-b
    return c

def func(l):
    if len(l)==0:
        return 0
    else:
        return(l.count(min(l)))
    

def funct(l):
    if len(l)>3:
        return "within limit"
    else:
        return "limit exceded"
    
