text1 = 'パトカー'
text2 = 'タクシー'

answer = "".join([a+b for a, b in zip(text1, text2)])
print(answer)
print(answer == 'パタトクカシーー')
