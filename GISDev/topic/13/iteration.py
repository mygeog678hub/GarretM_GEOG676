class TriangularNums:
    # Calculate triangular numbers with x = t(t+1)/2

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.t = 1
        return self

    def __next__(self):
        if self.t > self.n:
            raise StopIteration

        x = self.t * (self.t + 1) / 2
        self.t += 1

        return int(x)


n = int(input("Enter the nth term: "))

for x in TriangularNums(n):
    print(x)