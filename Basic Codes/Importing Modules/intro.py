# Ensure mymodule.py is in the same directory or install the module if it's external

# from MyModule import *
# import MyModule as mm


from MyModule import find_index, test 
courses=['Math','Art','Science','History','Geography']
index=find_index(courses,'Geography')
print(index)
print(test)

# print(sys.path) #['/home/lakshman/Python/Basic Codes/Importing Modules', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/lakshman/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
# sys.path.append('/home/lakshman/Python/Basic Codes/Importing Modules')