class Recursion:

    def sum_ints_upto(self, n):
        if n == 1:
            return 1
        return n + self.sum_ints_upto(n - 1)

    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

    def reverse_string(self, string, i):
        if -len(string) == i:
            return string[i]
        return string[i] + self.reverse_string(string, i - 1)
