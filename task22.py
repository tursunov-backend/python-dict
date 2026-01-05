def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    group = {}
    for student in students:
        group_name = student['group']
        if group_name not in group:
            group[group_name] = []

        group[group_name].append(student['name'])
    return group

students = [
    {
        'name': 'Ali',
        'group': 'A'
    },
        {
        'name': 'Vali',
        'group': 'B'
    },
        {
        'name': 'Sami',
        'group': 'A'
    },
        {
        'name': 'Gani',
        'group': 'C'
    },
        {
        'name': 'Abu',
        'group': 'B'
    }
]
result = group_students(students)
print(result)
