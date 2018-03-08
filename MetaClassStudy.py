import dis


#
#all classes without definition are taken from !!type!!
#now we can declare that the class will be not created using type
#but using some other thing other than DIRECTLY type
#here we declarre a class that is instance of class type
#
class BaseMeta(type):
    #here we define what will happen when we instantiate
    # a class from the class we created (BaseMeta)
    def __new__(cls, name, bases, body):
       #print the contents of the class we can put here any function
       #that will be ran before the instantiation of the below subclass
        print('BaseMeta.__new__', cls, name, bases, body)
       #catch if not exists function
        # if not 'bar' in body:
        #     print("bad user class")

        #here we actualy return the newly created class
        return super().__new__(cls, name, bases, body)

#Duplicated from above
#all classes without definition are taken from !!type!!
#now we can declare that the class will be not created using type
#but using some other thing other than DIRECTLY type
#here we define it to be created by BaseMeta
class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()
    #method that runs when subclass is being initiated
    def __init_subclass__(cls, **kwargs):
        print("inited ",cls,kwargs)
        return super().__init_subclass__( **kwargs)

#check if the foo exists in Base method
#this check can be ran before the deployment
#assert hasattr((Base,'foo'),"no such method")


#derive subclass
class Derived(Base):
    def bar(self):
        return self.foo()


#dissaemble class
# dis(_)

d1=Derived()



#another metaclass examplethat checks if a class inherits from more than 1 class if so it throws error
class mytype(type):
    def __new__(cls, clsname, bases,clsdict):
        if(len(bases)>1):
            raise  TypeError("No")
        return super().__new__(cls, clsname, bases,clsdict)


class Base(metaclass=mytype):
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(A,B):
    pass
