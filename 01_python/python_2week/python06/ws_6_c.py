data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for dictionary in data:
    for key in key_list:
        #print(f"{key}은/는 {dictionary.get(key, 'unknown')}입니다.")
        print(f"{key}은/는 {dictionary.setdefault(key, 'unknown')}입니다.")
    print()

# 둘중 아무거나 하나만 쓰면 안되나용?