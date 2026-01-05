def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group = {}
    for idx, num in enumerate(numbers):
        if num not in group.keys():
            group[num] = []

        group[num].append(idx)

    return group        



nums = [1, 2, 3, 4, 3, 4, 2, 2, 1, 11, 13, 3, 11]
result = group_indices(numbers=nums)
print(result)
