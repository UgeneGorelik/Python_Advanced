from inspect import getsource
from time import  time

def timer1(func,x,y):
    before=time()
    after=time()
    rv=func(x,y)
    print("elapsed: ",after-before)
    return rv

#here we are crating new function that wrapps the original
#func function we have got
def timer(func):
    #here args/kwargs define we can get any variables
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed', after - before)
        return rv
    return f


#another example of Decorator of function
#for running function 2 times
n = 2

def ntimes(f):
    def wrapper(*args, **kwargs):
        for _ in range(n):
            print('running {.__name__}'.format(f))
            rv = f(*args, **kwargs)
        return rv
    return wrapper

#@defines the what will decorate the function
#timer
@ntimes
def add(x,y):
    return x + y
#here we define a new function that defines
#add as being wrapoed in timer
#add=timer(add)

# #print details of the finction
# print(add.__defaults__)
# print(add.__code__)
# print(add.__code__.co_varnames)
# print(getsource(add))


add(1,2)