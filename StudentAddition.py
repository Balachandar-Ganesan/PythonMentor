
# Online Python - IDE, Editor, Compiler, Interpreter

def start(lstStudentsFullList):
    def intEnterNumber():
        intNumber=int(input("Enter Number Of Students"))
        return intNumber
    intNoOfStudents = intEnterNumber()
    lstStudents=lstStudentsFullList
    
    for intCounter in range(intNoOfStudents):
        strName=input("Enter Name of Student")
        lstStudents.append(strName)
    strContinue =input("Do You Want to Continue Y/N ?")
    if(strContinue=="Y"):
            start(lstStudents)
    else:
        return lstStudents
    return lstStudents

lstStudents=[]
start(lstStudents)
print(lstStudents)