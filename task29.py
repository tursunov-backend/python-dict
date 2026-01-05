def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    result = []

    for user in users:
        if user["active"] == True:
            result.append(user["name"])

    return result



users = [
    {'id': 1, 'name': 'Ali',   'active': False},
    {'id': 2, 'name': 'Vali',  'active': True},
    {'id': 3, 'name': 'Hasan', 'active': False},
    {'id': 4, 'name': 'Husan', 'active': True},
    {'id': 5, 'name': 'Olim',  'active': True},
    {'id': 6, 'name': 'Akmal', 'active': True},
    {'id': 7, 'name': 'Sardor','active': False},
    {'id': 8, 'name': 'Jasur', 'active': True},
]

result = get_active_users(users=users)
print(result)


  