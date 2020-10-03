def accepts(*types):
    def inner(func):
        def wrap(*args):
            if len(args) != len(types):
                raise RuntimeError()  # todo
            for (_arg, _type) in zip(args, types):
                if not isinstance(_arg, _type):
                    raise TypeError(f"{_arg} should be of type {_type}, not {type(_arg)}")
            return func(*args)
        return wrap
    return inner


def returns(_type):
    def inner(func):
        def wrap(*args):
            ret = func(*args)
            if not isinstance(ret, _type):
                raise TypeError(f"{ret} should be of type {_type}, not {type(ret)}")
            return ret
        return wrap
    return inner


@accepts(str, int)
@returns(None)
def show_what_i_have(asset: str, quantity: int) -> None:
    if quantity > 1:
        asset = asset + 's'
    print(f"I have {quantity} {asset}!")


show_what_i_have("buck", 100)
show_what_i_have(1, "pencil")
