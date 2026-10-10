#multithreading

from threading import Thread,Lock,Semaphore
'''for i in range(65,91):
    print(i)
def alpha():
    for i in range(65,91):
        print(chr(i))
t=Thread(target=alpha,name='alpha')     #target=alpha is the function name and is used to call the function inside the thread
t.start()                           #start() is used to start the thread
t.join()        
'''


'''l=Semaphore(2)             #semaphore is used to control how many threads can access a resource at sametime. In this case, 2 threads can access the resource at same time.
def str_reader(f):
    l.acquire()              #acquire() is used to get the lock for the thread    # l=lock() is used to prevent multiple threads from accessing the same resource at the same time
    for i in f:
        print(i)
    l.release()                                                  #release() is used to release the lock for the thread
t=Thread(target=str_reader,name='numbers',args=('0123456789',))
t1=Thread(target=str_reader,name='alpha',args=('abcdefghij',))
t.start()
t1.start()
t.join()
t1.join()'''



'''class MyThread(Thread):

    def __init__(self,data):
        super().__init__()
        self.data=data
    def run(self):
        for i in self.data:
            print(i)
t=MyThread('0123456789')
t.start()
t.join()  '''              




'''class MyThread(Thread):

    def __init__(self,f,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.f=f
        

    def run(self):
     
        for i in self.f:
            print(i)
         

t = MyThread('0123456789')
t1=MyThread('abcdefghij')
t.start()
t1.start()'''
        


'''class MyThread(Thread):

    def __init__(self,f,j,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.f=f
        self.j=j

    def run(self):
        print(self.j)
        for i in self.f:
            print(i)
         

t = MyThread('0123456789',10)
t1=MyThread('abcdefghij',20,name='alpha',daemon=True)


t.start()
t1.start()

t.join()
t1.join()'''



