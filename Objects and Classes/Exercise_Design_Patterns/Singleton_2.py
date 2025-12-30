def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper

@singleton
class Singleton:

     def __init__(self):
         pass

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
print(s1)
print(s2)
if s1 == s2:
    print("Same")
else:
    print("Different")

print(id(s1))
print(id(s2))
