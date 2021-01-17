#!/usr/bin/env python
# coding: utf-8

# In[1]:


import threading, time, random, queue

class Prod:
    def __init__(self):
        self.next = 0
        
    def run(self):
        global q1, q2, q3
        while(True):
            if (not (q1.full() or q2.full() or q3.full())):
                if (q1.qsize() == q2.qsize() == q2.qsize()):
                    choice = random.choice([q1,q2,q3])
                elif (q1.qsize() == q2.qsize()):
                    choice = random.choice([q1,q2])
                elif (q2.qsize() == q3.qsize()):
                    choice = random.choice([q3,q2])
                elif (q1.qsize() == q3.qsize()):
                    choice = random.choice([q3,q1])
                else:
                    arr = [q1,q2,q3]
                    choice = q1
                    for i in arr:
                        if i.qsize() < choice.qsize():
                            choice = i
                f = random.randint(1,10)
                dic = {q1: 'q1', q2: 'q2', q3: 'q3'}
                choice.put(f)
                print("Added " + str(f) + " to " + dic[choice])
                self.next += random.random()
                time.sleep(random.random())

class Comnsumer:
    def __init__(self, q, name, cname):
        self.queue = q
        self.cname = cname
        self.name = name
        self.next = 0

    def run(self):
        while(True):
            if (not self.queue.empty()):
                f = self.queue.get()
                print(self.cname + " removed " + str(f) + " from " + self.name)
                self.next += random.random()
            elif self.queue.empty():
                print('Queue emtpy, consumer is waiting for product.')
            time.sleep(random.random())

if __name__ == '__main__':
    q1 = queue.Queue(random.randint(1,10))
    q2 = queue.Queue(random.randint(1,10))
    q3 = queue.Queue(random.randint(1,10))
    p = Prod()
    c1 = Comnsumer(q1, "q1", "Consumer1")
    c2 = Comnsumer(q2, "q2", "Consumer2")
    c3 = Comnsumer(q3, "q3", "Consumer3")
    pt = threading.Thread(target=p.run, args = ())
    ct1= threading.Thread(target=c1.run, args = ())
    ct2= threading.Thread(target=c2.run, args = ())
    ct3= threading.Thread(target=c3.run, args = ())
    pt.start()
    ct1.start()
    ct2.start()
    ct3.start()


# 
