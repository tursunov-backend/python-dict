def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    result = {}
    
    for person in people:
        age = person['age']
        name = person['name']

        if age not in result:
            result[age] = []

        result[age].append(name)

    return result

people = [
    {'name': 'Ali', 'age': 20},
    {'name': 'Vali', 'age': 21},
    {'name': 'Hasan', 'age': 20},
    {'name': 'Husan', 'age': 21},
    {'name': 'Olim', 'age': 22},
]

print(group_by_age(people))
