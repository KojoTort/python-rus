
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

def выбор(a, b):
	return a or b 
	
def и (a, b):
	return a and b 
	
	
def словарь(**kwargs):
	return kwargs
	
	
	
def список(*args):
	return list(args)
	
	

class класс:

	def __init__(self, x, y):
		self.x = x 
		self.y = y 
		
		
	def method(self): 
		return self.x + self.y 
		
		
		
class структура:
	def __init__(self, x, y):
	
		self.x = x 
		self.y = y 
		
def число(x):
	return int(x)
	
	
	
def строка(x):
	return str(x) 
	
	
def замороженый_сет(*args):
	return frozenset(args)
	
	
def число_с_точкой(x):
	return float(x)
	
    
def  ввести(promt= ' '):
    return input(promt)


	
