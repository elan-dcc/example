import numbers

def add(a, b):
    if isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
        return a+b
    else: raise TypeError

print(add(2,3))
print(add('monkey', 'business'))