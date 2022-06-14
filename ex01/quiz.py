a = tuple("ますお","マスオ")
b = tuple("わかめ","ワカメ")
c = tuple("甥","おい","甥っ子","おいっこ")
ans = input("問題:サザエの旦那の名前は?")
if ans in a:
    print("正解!!!")
else:
    print("出直してこい")
bns = input("カツオの妹の名前は?")
if bns in b:
    print("正解!!!")
else:
    print("出直してこい")
cns = input("タラオはカツオから見てどんな関係?")
if cns in c:
    print("正解!!!")
else:
    print("出直してこい")
import random 
mondai = [ans,bns,cns]
print(random.choices(mondai))
