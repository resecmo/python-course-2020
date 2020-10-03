def author(_author):
    def inner(func):
        func.author = _author
        return func
    return inner


@author("Captain Friedrich Von Schoenvorts")
def add2(num: int) -> int:
    return num + 2


print(add2.author)
