class Singleton:
     __instance = None

     def __init__(self):
         if Singleton.__instance is not None:
             raise Exception("This class is a singleton.")

     @classmethod
     @property
     def get_instance(cls):
         if cls.__instance is None:
             cls.__instance = cls()
         return cls.__instance

s1 = Singleton.get_instance
s2 = Singleton.get_instance

print(s1 is s2)
print(s1)
print(s2)
if s1 == s2:
    print("Same")
else:
    print("Different")

print(id(s1))
print(id(s2))
