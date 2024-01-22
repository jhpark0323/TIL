# 아래 함수를 수정하시오.
def even_elements(ls):
    new_list = []
    for i in ls:
        if i % 2 == 1:
            idx = ls.index(i)
            ls.pop(idx)
    new_list.extend(ls)
    return new_list



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
