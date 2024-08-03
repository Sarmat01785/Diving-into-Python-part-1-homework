'''
Задача 2

 В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
 Не учитывать знаки препинания и регистр символов. 
 За основу возьмите любую статью из википедии или из документации к языку.
'''


text = (
    "Задача 2 В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых."
    "Не учитывать знаки препинания и регистр символов."
    "За основу возьмите любую статью из википедии или из документации к языку."
    "Не учитывать знаки препинания и регистр символов."
    "За основу возьмите любую статью из википедии или из документации к языку."
)

words = [word.lower().strip(".?!:;") for word in text.split()]

word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print("Топ-10 самых частых слов:")
for word, count in sorted_words[:10]:
    print(f"{word}: {count}")