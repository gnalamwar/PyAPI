from multiprocessing import Process, Queue

def tripler(mylist, q):
    """
    function to triple items in a given list
    """
    # append triples of mylist to queue
    for num in mylist:
       q.put(num * 3)

