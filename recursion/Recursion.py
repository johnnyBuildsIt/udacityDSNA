import copy

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

    def is_palindrome(self, string):
        if len(string) == 1 or len(string) == 0:
            return True
        if string[0] == string[-1]:
            return self.is_palindrome(string[1:-1])
        else:
            return False

    def add_one(self, arr):
        return self.add_one_recursive(arr, -1)

    def add_one_recursive(self, arr, index):
        if index < -len(arr):
            arr = [0 for i in range(-index)]
            arr[0] = 1
            return arr

        summ = arr[index] + 1
        if summ < 10:
            arr[index] = summ
            return arr
        else:
            arr[index] = 0
            return self.add_one_recursive(arr, index - 1)

    def permute(self, in_list):
        out_list = []

        if len(in_list) == 0:
            out_list.append([])
            return out_list
        else:
            first_item = in_list[0]
            permuted_rest_of_list = self.permute(in_list[1:])

            for sub_list in permuted_rest_of_list:
                for i in range(0, len(sub_list)+1):
                    cur_list = copy.deepcopy(sub_list)
                    cur_list.insert(i, first_item)
                    out_list.append(cur_list)

        return out_list
