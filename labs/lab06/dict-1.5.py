class Dict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

    def __add__(self, other):
        if isinstance(other, (Dict, dict)):
            pass  # todo
        else:
            raise ValueError(f"")  # todo

    def add(self, other):
        return self + other


a = Dict({'g': 7})
a[6] = 7

print(a)
