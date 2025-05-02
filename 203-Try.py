import traceback

def Dividebyzero():
    print(4/0)

def Calldividebyzero():
    Dividebyzero()
try:
    Calldividebyzero()
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()