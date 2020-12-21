class ConsoleIterator:
    def __init__(self):
        self._numbers = []

        # flag to denote that no error was encountered; if false, __next__() still works until self.numbers is empty
        self.ok = True

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if len(self._numbers) > 0:
                return self._numbers.pop(0)
            elif self.ok:
                try:
                    input_string = input().split()
                except EOFError:
                    raise StopIteration

                try:
                    for item in input_string:
                        self._numbers.append(int(item))
                except ValueError:
                    self.ok = False
            else:
                raise StopIteration


if __name__ == "__main__":
    total_sum = 0

    for number in ConsoleIterator():
        print(number)
        total_sum = total_sum + number

    print(f'Sum of entered numbers is {total_sum}')
