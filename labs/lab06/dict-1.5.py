class Dict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __add__(self, other):
        if isinstance(other, (Dict, dict)):
            for item in other.items():
                self[item[0]] = self[item[1]]
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def add(self, other):
        return self + other

    @staticmethod
    def from_default(default_dict):
        if isinstance(default_dict, dict):
            return Dict(default_dict)
        else:
            raise ValueError(f"Dict.from_default() expected a dict, got {type(default_dict)}")


def test():
    a = Dict({'g': 7})
    a[6] = 7
    print(a)
    print(Dict(color='red', state='aggressive'))
    print(Dict.from_default({'time': '1:21', 'doing': 'writing hw'}))
    print(Dict({'time': '1:21', 'doing': 'writing hw'}))
    print(type(a))


if __name__ == "__main__":
    test()
