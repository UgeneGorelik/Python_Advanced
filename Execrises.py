# wrap a finction with printing function name

from contextlib import contextmanager

def Loogger(foo):
    def f(*args,**kwargs):
        print("running function:"+f.__name__)
        rv=foo(*args,**kwargs)
        return rv
    return f

@Loogger
def Conc(a,b):
    return a + b



#fibonacci with memoization

def memoize(foo,d={}):

    def f(n):
        rv = foo(n)
        if n not in d:
            d[n]=rv
            return foo(n)
        else:
            return d[n]
    return f

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#fibonacci using Generator

def FibGenerator(n,a=0,b=1):
    for x in range(n):
        yield a
        a,b=b,a+b

#create custom Iterator custom __next__ and __iter__
class CustomGenerator:
     def __init__(self):
         self.n = 0
     def __iter__(self):
        return  self
     def __next__(self):
        self.n+=1
        return self.n

#metaclass that keeps all the attributes lowercase
class LowerAttrMeta(type):
    def __new__(lower_metaclass,future_name,future_parents,future_attrs):
        lower_attributes= {}
        for name,val in future_attrs.items():
            if not name.startswith('__'):
                lower_attributes[name.lower()] =val
            else:
                lower_attributes[name] = val
        return type(future_name,future_parents,lower_attributes)

class A(metaclass=LowerAttrMeta):
        C = 10
        @staticmethod
        def Foo():
            print("pp")
            return 3


#Contex manager file open

class Open_file():
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


#context mangager as decorator for opening and editing files

@contextmanager
def open_file_dec(file,mode):
    f=open(file,mode)
    yield f
    f.close()



if __name__=="__main__":
    #print(Conc("a","b"))
    # print(fib(10))
    # x=FibGenerator(15)
    # print(next(x))
    # print(next(x))
    # print(next(x))
    # print(next(x))
    # x=CustomGenerator()
    ## i=iter(x)
    # print(next(x))
    # print(next(x))
    # A.foo()
    # with Open_file('tst.txt', 'w') as f:
    #     f.write('Tesitng')
    #
    # with Open_file('tst.txt', 'r') as f:
    #     for x in f:
    #         print(x)
    with open_file_dec('tst.txt', 'r') as f:
     for x in f:
             print(x)