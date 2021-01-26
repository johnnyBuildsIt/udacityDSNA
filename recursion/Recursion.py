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
                for i in range(0, len(sub_list) + 1):
                    cur_list = copy.deepcopy(sub_list)
                    cur_list.insert(i, first_item)
                    out_list.append(cur_list)

        return out_list

    def get_characters(self, num):
        if num == 2:
            return "abc"
        elif num == 3:
            return "def"
        elif num == 4:
            return "ghi"
        elif num == 5:
            return "jkl"
        elif num == 6:
            return "mno"
        elif num == 7:
            return "pqrs"
        elif num == 8:
            return "tuv"
        elif num == 9:
            return "wxyz"
        else:
            return ""

    def keypad(self, num):
        if num <= 1:
            return [""]
        elif 1 < num <= 9:
            return list(self.get_characters(num))

        last_num = num % 10
        last_num_letters = self.get_characters(last_num)
        upper_letters = self.keypad(num // 10)

        output = []
        for letters in upper_letters:
            for letter in last_num_letters:
                output.append(letters + letter)

        return output

    def staircase(self, steps):
        if steps == 1:
            return 1
        elif steps == 2:
            return 2
        elif steps == 3:
            return 4

        return self.staircase(steps - 1) + self.staircase(steps - 2) + self.staircase(steps - 3)

    def staircase_cache(self, steps):
        cache = {}
        return self.staircase_cache_helper(steps, cache)

    def staircase_cache_helper(self, steps, cache):
        if steps == 1:
            return 1
        elif steps == 2:
            return 2
        elif steps == 3:
            return 4
        else:
            if steps - 1 in cache:
                steps_minus_one =  cache[steps - 1]
            else:
                steps_minus_one = self.staircase_cache_helper(steps - 1, cache)

            if steps - 2 in cache:
                steps_minus_two = cache[steps - 2]
            else:
                steps_minus_two = self.staircase_cache_helper(steps - 2, cache)

            if steps - 3 in cache:
                steps_minus_three = cache[steps - 3]
            else:
                steps_minus_three = self.staircase_cache_helper(steps - 3, cache)

        return steps_minus_one + steps_minus_two + steps_minus_three

