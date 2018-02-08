#a example of dunder methods

class Polynomial:
    def __init__(self,*coeffs):
        self.coeffs=coeffs

#addition + dunder method
    def __add__(self, other):
        return  Polynomial(*(x + y for x,y in zip(self.coeffs,other.coeffs)))
#Representetion printing of the class data
    def __repr__(self):
        return ("{}".format(self.coeffs))
#lenght return
    def __len__(self):
        return len(self.coeffs)
#calling a class
    def __call__(self):
        pass

p1=Polynomial(1,2,3)
p2=Polynomial(3,4,3)
print(p1+p2)

print(len(p1))

#option to add variables to class
# p1.coeffs=1,2,3
# p2.coeffs=3,4,3