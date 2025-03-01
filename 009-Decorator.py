def UpperCase(func):
    def Wrapper(Name):
        result =func(Name)
        decResult=result.upper()
        return decResult
    return Wrapper
@UpperCase
def greet(strGenCName):
    return "Hi " + strGenCName

print(greet(" Balachandar "))
