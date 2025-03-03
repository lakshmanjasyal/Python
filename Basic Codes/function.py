def hello_func():
    pass # pass is a placeholder for future code
print(hello_func) # <function hello_func at 0x7f8b1c3b7d30>
print(hello_func()) 


def hello1_func():
    print('Hello Function!')
hello1_func() # Hello Function!

def hello2_func():
    return 'Lakshman'
name=hello2_func()
print(name.upper())


def hello3_func(greeting,name):
    return '{} {}'.format(greeting,name)
name=hello3_func('Hi','Lakshman')
print(name)

def student_info(*args,**kwargs):
    print(args) #positional arguments
    print(kwargs)# arbitrary arguments and keyword arguments
student_info('Math','Art',name='Lakshman',age=25)

#Not exactly the same as above but if we use * and ** in the function definition, it will work the same way
courses=['Math','Art'] #list
info={'name':'Lakshman','age':25} #dictionary
student_info(*courses,**info) 




