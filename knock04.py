text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. ' \
       'Arthur King Can. '
word_array = text.replace('.', '').split(' ')
answer = {}
for i, word in enumerate(word_array):
    if i + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        answer[i] = word[0]
    else:
        answer[i] = word[:2]
print(answer)
