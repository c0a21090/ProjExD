import random 
taisyou = list()
hyouzi = list()
alpha = [chr(i) for i in range(65,91)]
print("対象文字:")
for j in range(10):
    taisyou.append(random.choice(alpha))
print(taisyou)
print("表示文字:")
random.shuffle(taisyou)
del taisyou[0]
del taisyou[0]
for o in taisyou:
    hyouzi.append(o)
print(hyouzi)
sabunn = set(taisyou) ^ set(hyouzi)
sabunnsuu = len(sabunn)
ans = input("欠損文字はいくつあるでしょうか?:")
if ans == sabunnsuu:
    print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
else:
    print("不正解です。またチャレンジしてください")
#iti = input("1つ目の文字を入力してください:")
#ni = input("2つ目の文字を入力してください:")


