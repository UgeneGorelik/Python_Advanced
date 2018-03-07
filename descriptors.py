class Descriptor(object):
    def __get__(self, instance, owner):
        print('getting')
        if instance is None:
            raise  AttributeError('can be acssed only by imstance')
        return self.val

    def __set__(self, instance, value):
        print('setting')
        self.val=value

    def __delete__(self,instance):
        print('deleting')
        del  self.val


class Thing(object):
    name=Descriptor()

    def __init__(self,name):
        self.name=name

t=Thing(1)

print(t.name)
