def TellRunner(text):
    print("Come For "+text)

TellRunner("Two")
AnotherFunc=TellRunner
del TellRunner
AnotherFunc("a Single")
#TellRunner("No more runs")
print(AnotherFunc.__name__)