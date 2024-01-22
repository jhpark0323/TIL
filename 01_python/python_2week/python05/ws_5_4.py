# 아래 함수를 수정하시오.
def capitalize_words(word):
    word_split = word.split()
    new_word = []
    for word in word_split:
        capital = word[0].upper()
        capital = capital + word[1:]
        new_word.append(capital)
    return ' '.join(new_word)

result = capitalize_words("hello, world!")
print(result)
