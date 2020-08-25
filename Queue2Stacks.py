class _Queue2Stacks(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        self.stack2 = list(reversed(self.stack1))
        val = self.stack2.pop()
        self.stack1 = list(reversed(self.stack2))
        return val


class Queue2Stacks(object):
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


s = Queue2Stacks()

for i in range(5):
    s.enqueue(i)

for i in range(5):
    print(s.dequeue())
