from time import sleep

#declare generator
def compute():
    for x in range(10):
        yield  x

#define varialble as generator
y=compute()

#print one next iteration
print(next(y))

#print all the rest in loop
for x in compute():
    print(x)


#an example of using the Yield Keyword to run a function and each sequence will be run as next
def print_name(name):
    yield ("A: " +name)
    yield ("B: " + name)
    yield ("C: " + name)


for x in print_name("a"):
    print(x)