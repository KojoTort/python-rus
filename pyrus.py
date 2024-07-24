
def печать(message):
    
    print(message)


definitions = {}
def определение(name, func):
  
    definitions[name] = func


def если(cond, then, else_):
    
    if cond:
        return then()
    else:
        return иначе_функция(else_)


def иначе_функция(func):
    
    return func()


def пока(cond, func):
    
    while cond():
        func()

def для(iterable, func):
    
    for item in iterable:
        func(item)


def перечисление(*args):
 
    return args

def иначе_если(cond, then, else_):
    
    if cond:
        return then()
    else:
        return иначе_функция(else_)