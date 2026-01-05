class Fibonacci:

    def fib(self, number):
        a = 0
        b = 1

        for _ in range(number):
            print(a, end=" ")

            temp = a + b
            a = b
            b = temp

fib_instance = Fibonacci()
fib_instance.fib(10)
