def merge_dicts(a: dict, b: dict) -> dict:
    result = a.copy()
    result.update(b)
    return result
a = {'text': 'salom', 'son': 10}
b = {'son': 20, 'matn': 123}

print(merge_dicts(a, b))
