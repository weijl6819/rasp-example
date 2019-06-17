import os 

orig_system = os.system 

def func(x):
    print("wtf")
    orig_system(x)

os.system = func

os.system("whoami")