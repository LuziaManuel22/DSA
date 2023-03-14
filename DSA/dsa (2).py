import random as r

class Queue:
    elements = None
    def __init__(self) -> None:
        self.elements = []

    def enqueue(self, n):
        self.elements.append(n)
    def dequeue(self):
        self.elements.pop(0)

    def printQueue(self):
        print(*self.elements, sep="->")

    def isEmpty(self)->bool:
        return len(self.elements) == 0

    def front(self):
        return self.elements[0]

def cust_arr_event(c_id, event_time)->int:
        global cust_id 
        
        if c_id == None:
            cust_id = 1
        else:
            cust_id =  c_id

        event_time = wall_clock + iat * r.random()

        return event_time

def cust_dep_event(c_id, event_time)->int:
        global cust_id
        
        if c_id == None:
            cust_id = 0
        else:
            cust_id = c_id
       
        return event_time

if __name__ =="__main__":
    q = Queue() #initialize the queue
    wall_clock = 0
    teller = "free"
    bank_closing_time = 600
    wait_times = []
    iat =10
    st = 16

    cust_id = 0
    event_time = 0
    next_event = 0

    while wall_clock <= bank_closing_time  and  q.isEmpty():
        cust_dep= cust_dep_event(None, 0)
        cust_arr= cust_arr_event(None, 0)
        if cust_arr > cust_dep:
            event_time = event_time + 1 #computing the next time.
        wall_clock = event_time
        cust_id = cust_id
  
        if next_event <= cust_arr and wall_clock <= 600:
            q.enqueue((cust_id, wall_clock))
            if teller == "free":
                cust_dep = cust_dep_event(cust_id, wall_clock + st * r.random())
                teller = "busy"
            cust_id = cust_id + 1
            next_event = cust_arr_event(cust_id, wall_clock + iat * r.random())

        if next_event == cust_dep:
            (cust_id, arr_time) = q.dequeue()
            wait_times.append((cust_id, arr_time, wall_clock))
            if not q.isEmpty():
                cust_id = q.front()[0]
                cust_dep = cust_dep_event(cust_id, wall_clock + st * r.random())
                teller ="busy"
    print(wait_times)