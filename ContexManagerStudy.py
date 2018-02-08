from sqlite3 import connect



#with means in the below example:
#open file and close file when done
#means with keyword means start with something
#and in the end end with something

with open('tst.txt') as f:
    pass

#we declare a class that will runn using context manager type implementation

class temptable:
    def __init__(self,cur):
        self.cur=cur
    #this will happen  on instantiating the class
    def __enter__(self):
        print("__enter__")

       #sqllite create table
        self.cur.execute('create table points(x int, y int)')

    #this happen when instantation ends
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("_exit_")
        #sqllite drop table
        self.cur.execute('drop table points')

with connect('test.db') as conn:
        #declare Sqllite cursor for running DB queries

        cur = conn.cursor()
        #here we start instantiationg the temptable class so __enter__ from the temptable class will run
        with temptable(cur):
            #run insert to DB query
            cur.execute('insert into points (x, y) values(1, 1)')
            cur.execute('insert into points (x, y) values(1, 2)')
            cur.execute('insert into points (x, y) values(2, 1)')
            cur.execute('insert into points (x, y) values(2, 2)')
            # run select to DB query
            for row in cur.execute("select x, y from points"):
                print(row)
            for row in cur.execute('select sum(x * y) from points'):
                print(row)
        # here we end  instantiationg the temptable class so exit from the temptable class will run