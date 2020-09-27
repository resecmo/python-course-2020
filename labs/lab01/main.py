s = input()
if '.' in s:
    n = set(map(lambda x: float(x) ** 2, s.split()))
else:
    n = set(map(lambda x: int(x) ** 2, s.split()))
print(*sorted(n))
