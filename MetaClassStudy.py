import dis

class BaseMeta(type):
    def __new__(cls, name, bases, body):
       #print the contents of the class
        print('BaseMeta.__new__', cls, name, bases, body)
       #catch if not exists function
        # if not 'bar' in body:
        #     print("bad user class")
        return super().__new__(cls, name, bases, body)

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