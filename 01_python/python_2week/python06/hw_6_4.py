# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, key_, value_):
    new_dict = dictionary.copy()
    new_dict[key_] = value_
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
