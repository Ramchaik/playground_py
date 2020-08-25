class _Stack2Queue(object):
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, element):
        self.q1.insert(0, element)

    def pop(self):
        n = len(self.q1)
        for i in range(n):
            if i < n - 1:
                self.q2.insert(0, self.q1.pop())
            else:
                val = self.q1.pop()
                self.q1 = self.q2
                return val


class Stack2Queue(object):
    def __init__(self):
        self.empty_q = []
        self.all_elements_q = []

    def push(self, element):
        self.empty_q.insert(0, element)

        while self.all_elements_q:
            self.empty_q.insert(0, self.all_elements_q.pop())

		# Swapping
        self.empty_q, self.all_elements_q = self.all_elements_q, self.empty_q

    def pop(self):
        return self.all_elements_q.pop()


s = Stack2Queue()

for i in range(5):
    s.push(i)

for i in range(5):
    print(s.pop())
