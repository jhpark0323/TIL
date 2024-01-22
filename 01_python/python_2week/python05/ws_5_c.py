def restructure_word(word, arr):
    for word_str in word:
        if word_str.isdecimal():
            for _ in range(int(word_str)):
                arr.pop()
        else:
            if word_str in arr:
                arr.remove(word_str)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = [i for i in original_word]
print(arr)

result = restructure_word(word, arr)
print(result)

print(''.join(result))