class StackArray:

    def __init__(self, initialize_size=10):
        self.arr = [None for _ in range(initialize_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, element):
        if self.next_index == len(self.arr):
            print("Stack full, increasing size...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = element
        self.next_index += 1
        self.num_elements += 1

    def _handle_stack_capacity_full(self):
        prev_arr = self.arr

        self.arr = [None for _ in range(len(prev_arr) * 2)]
        for index, element in enumerate(prev_arr):
            self.arr[index] = element

    def size(self):
        return self.num_elements

    def is_empty(self):
        if self.num_elements == 0:
            return True
        return False

    def pop(self):
        if self.is_empty():
            return None

        self.next_index -= 1
        self.num_elements -= 1
        element = self.arr[self.next_index]
        self.arr[self.next_index] = None
        return element


