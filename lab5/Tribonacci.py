class Tribonacci:
    def __init__(self):
        self.a, self.b, self.c = 0, 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 35:
            raise StopIteration
        else:
            result = self.a
            self.a, self.b, self.c = self.b, self.c, self.a + self.b + self.c
            self.count += 1
            return result


tribonacci = Tribonacci()
for number in tribonacci:
    print(number)
