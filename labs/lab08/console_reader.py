class ConsoleIterator:
    def __iter__(self):
        self._numbers = []
        self.ok = True
        return self

    def __next__(self):
        while True:
            if len(self._numbers) > 0:
                return self._numbers.pop(0)
            elif self.ok:
                input_string = input().split()
                try:
                    for item in input_string:
                        self._numbers.append(int(item))
                except ValueError:
                    self.ok = False
            else:
                raise StopIteration


total_sum = 0

for number in ConsoleIterator():
    print(number)
    total_sum = total_sum + number

print(f'Sum of entered numbers is {total_sum}')
