import multiprocessing
from multiprocessing import Value

import time
#from globalvar import *
a=Value('f', 8)
#toto=8

def worker(a):
    try:
        name = multiprocessing.current_process().name
        for i in range(1,100):
            a.acquire()
            a.value=i
            a.release()
            print ("worker=",a.value)
            time.sleep(3)
    except Exception as e:
        print (e)
        a.release()

def my_service(az):
    name = multiprocessing.current_process().name
    # print (name,"Starting")
    # time.sleep(3)
    # print (name, "Exiting")
    while True:
        try:
            az.acquire()
            print ("my_service=",az.value)
            az.release()
            time.sleep(2)
        except Exception as e:
            print (e)
            az.release()

if __name__ == '__main__':
    #Process(target=worker).start()
    service = multiprocessing.Process(name='my_service', target=my_service,args=(a,))
    worker_1 = multiprocessing.Process(name='worker 1', target=worker,args=(a,))
    worker_2 = multiprocessing.Process(target=worker,args=(a,)) # use default name

    worker_1.start()
    worker_2.start()
    service.start()