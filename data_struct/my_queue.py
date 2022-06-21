
class MyStackOverflow(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Queue:
    def __init__(self, size=5) -> None:
        self.s = -1
        self.e = -1
        self.size = size
        self.lst = [-1 for _ in range(self.size)]

    def enqueue(self, val):
        if self.e + 1 == self.size and self.s == -1:
            raise MyStackOverflow('Full')

        self.e = (self.e + 1) % self.size

        if self.s == self.e:
            raise MyStackOverflow('Full')

        self.lst[self.e] = val
        print(f's: {self.s} e: {self.e} value: {self.lst}')

    def dequeue(self):
        if self.e == -1:
            raise MyStackOverflow('Empty')

        self.s = (self.s + 1) % self.size

        if self.s == self.e:
            raise MyStackOverflow('Empty')

        self.lst[self.s] = -1
        print(f's: {self.s} e: {self.e} value: {self.lst}')

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    # q.enqueue(5.1)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(6)
    q.dequeue()
    q.dequeue()
    q.enqueue(7)
    q.dequeue()
    q.dequeue()
    q.dequeue()