'''
Utility Classes
'''
# Last in First Out
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack())

    def __str__(self):
        return str(self.stack)


# First in First out 
class Queue:

    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.insert(0,item)
    
    def pop(self):
        return self.queue.pop()
    
    def isEmpty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)