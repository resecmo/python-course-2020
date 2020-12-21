def accepts(*types):
    def inner(func):
        def wrap(*args):
            if len(args) != len(types):
                raise RuntimeError()  # todo
            for (arg_, type_) in zip(args, types):
                if not (type_ is None and arg_ is None) and not (type_ is not None and isinstance(arg_, type_)):
                    raise TypeError(f"{arg_} should be of type {type_}, not {type(arg_)}")
            return func(*args)
        return wrap
    return inner


def returns(type_):
    def inner(func):
        def wrap(*args):
            result = func(*args)
            if not (type_ is None and result is None) and not (type_ is not None and isinstance(result, type_)):
                raise TypeError(f"{result} should be of type {type_}, not {type(result)}")
            return result
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
