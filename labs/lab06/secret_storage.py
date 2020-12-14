from typing import Any, Dict


class Storage:
    def __init__(self, data: Dict[str, Any]):
        self._data = data
        self._reserve_data = {
            "potato": 100,
        }
        self.__secret_data = {
            "supplier": "johnny",
        }

    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        elif key in self._reserve_data:
            return self._reserve_data[key]
        else:
            raise KeyError("Invalid key")

    @property
    def _secret_data(self):
        raise AttributeError("'Storage._secret_data' is way too secret")

    @_secret_data.setter
    def _secret_data(self, arg):
        self.__secret_data = arg


storage = Storage({'apple': 2})
print(storage['apple'])
print(storage['potato'])
try:
    print(storage['supplier'])
except KeyError as e:
    print(e)

try:
    print(storage._secret_data)
except AttributeError as e:
    print(f"got an exception: \"{e}\"")

