q = 10    #グローバル変数の定義
w = 2     #グローバル変数の定義
import random    #ランダムモジュール
taisyou = list()   #空のリストの作成
hyouzi = list()    #空のリストの作成
alpha = [chr(i) for i in range(65,91)]  #a~zを変数に入れる
print("対象文字:")
for j in range(q):  #q回a~zの中からランダムに割らんでリストに入れる
    taisyou.append(random.choice(alpha))
print(taisyou)
print("表示文字:")
random.shuffle(taisyou)   #要素をシャッフルする
del taisyou[0]   #一番目前の要素を削除する
del taisyou[0]  #一番目前の要素を削除する
for o in taisyou:    #削除後の8個の要素を別のリストに入れる
    hyouzi.append(o)
print(hyouzi)
ans = input("欠損文字はいくつあるでしょうか?:")  #入力した値を変数に入れる
if ans == w:   #判定
    print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
else:
    print("不正解です。またチャレンジしてください")
iti = input("1つ目の文字を入力してください:")
ni = input("2つ目の文字を入力してください:")


