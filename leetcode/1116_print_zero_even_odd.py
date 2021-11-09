from threading import Semaphore, Condition


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_sema = Semaphore()
        self.even_sema = Semaphore(0)
        self.odd_sema = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zero_sema.acquire()
            printNumber(0)
            (self.even_sema if i % 2 else self.odd_sema).release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_sema.acquire()
            printNumber(i)
            self.zero_sema.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_sema.acquire()
            printNumber(i)
            self.zero_sema.release()


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cod = Condition()
        self.sema = 0

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cod:
            for i in range(self.n):
                while self.sema:
                    self.cod.wait()
                printNumber(0)
                self.sema = 1 if i % 2 else 2
                self.cod.notify_all()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cod:
            for i in range(2, self.n + 1, 2):
                while self.sema - 1:
                    self.cod.wait()
                printNumber(i)
                self.sema = 0
                self.cod.notify_all()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cod:
            for i in range(1, self.n + 1, 2):
                while self.sema - 2:
                    self.cod.wait()
                printNumber(i)
                self.sema = 0
                self.cod.notify_all()


def printNumber(x):
    print(x)
