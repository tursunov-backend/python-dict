def count_names(names: list[str]) -> dict[str, int]:
    result = {}
    for name in names:
        result[name] = names.count(name)

    return result    

names = ['ali', 'vali', 'ali', 'vali', 'ali', 'gani', 'sami', 'sami']    
result = count_names(names=names)
print(result)