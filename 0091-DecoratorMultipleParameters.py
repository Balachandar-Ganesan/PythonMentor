def UpperCase(func):
    def Wrapper(*args,**kwargs):
        result =func(*args,**kwargs)
        decResult=result.upper()
        return decResult
    return Wrapper
@UpperCase
def greet(strGenCName):
    return "Hi " + strGenCName
@UpperCase
def greetFullName(strGenCFName,strGenCLName):
    return "Hi " + strGenCFName + "," +strGenCLName

print(greet(" Balachandar "))
print(greetFullName(" Balachandar ","Ganesan"))
