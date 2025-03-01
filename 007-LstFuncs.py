def TellRunner(text):
    return("Come For "+text)

funcList =[TellRunner,str.lower,str.capitalize]

for func in funcList:
        print(func("Two Runs"))