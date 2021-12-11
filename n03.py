text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
word_array = text.replace(',', '').replace('.', '').split(' ')
word_len_array = [len(w) for w in word_array]
print(word_len_array)
