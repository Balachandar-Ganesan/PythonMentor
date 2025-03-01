class Test:
    def __init__(self):
        self.FirstName ="Bala"
        self.__LastName = "Ganesan"
        
t=Test()
print(dir(t))
print(t.FirstName)
print(t._Test__LastName)
